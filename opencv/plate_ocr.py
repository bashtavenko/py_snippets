"""
Full-blown licence plate OCR.
"""
import re

import cv2
import pytesseract
from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_string("image", "testdata/ny_plate.png", "Path to an image")
flags.DEFINE_bool("no_plate_detect", False, "Run OCR on full image (skip ROI detection)")
flags.DEFINE_bool("show", False, "Show debug windows")
flags.DEFINE_integer("psm", 7, "Tesseract page segmentation mode (PSM)")
flags.DEFINE_integer("oem", 3, "Tesseract OCR engine mode (OEM)")
flags.DEFINE_string(
    "whitelist",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "Allowed characters for OCR (tessedit_char_whitelist)",
)


def find_plate_roi(bgr):
    """
    Very simple heuristic:
    - edge detect
    - find contours
    - pick a likely rectangular contour (license plate-ish)
    Returns ROI image (BGR) or None.
    """
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edges = cv2.Canny(gray, 30, 200)

    cnts, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:20]

    h, w = gray.shape[:2]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) != 4:
            continue

        x, y, cw, ch = cv2.boundingRect(approx)
        area = cw * ch
        aspect = cw / float(ch)

        # Loose filters: tweak as needed
        if area < 0.01 * (w * h):
            continue
        if not (2.0 <= aspect <= 6.5):
            continue

        return bgr[y: y + ch, x: x + cw]

    return None


def _preprocess_variants_for_ocr(bgr_or_gray):
    if len(bgr_or_gray.shape) == 3:
        gray = cv2.cvtColor(bgr_or_gray, cv2.COLOR_BGR2GRAY)
    else:
        gray = bgr_or_gray

    # Upscale small plates: Tesseract likes bigger glyphs
    h, w = gray.shape[:2]
    scale = 2.5 if max(h, w) < 900 else 1.5
    gray = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    thr = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Clean small gaps / noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Often plates are dark text on bright bg, but sometimes inverted
    return [("thr", thr), ("thr_inv", cv2.bitwise_not(thr))]


def ocr_text(bgr_or_gray):
    config = (
        f"--oem {FLAGS.oem} --psm {FLAGS.psm} "
        f"-c tessedit_char_whitelist={FLAGS.whitelist}"
    )

    best_text = ""
    best_conf = -1.0
    best_img = None

    for _name, img in _preprocess_variants_for_ocr(bgr_or_gray):
        data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)

        parts = []
        confs = []
        for txt, conf in zip(data.get("text", []), data.get("conf", [])):
            txt = (txt or "").strip()
            if not txt:
                continue
            try:
                c = float(conf)
            except (TypeError, ValueError):
                continue
            if c < 0:
                continue
            parts.append(txt)
            confs.append(c)

        raw = "".join(parts)
        cleaned = re.sub(r"[^A-Z0-9]", "", raw.upper())
        avg_conf = (sum(confs) / len(confs)) if confs else -1.0

        if cleaned and avg_conf > best_conf:
            best_text = cleaned
            best_conf = avg_conf
            best_img = img

    return (best_text, best_img)


def main(_argv):
    bgr = cv2.imread(FLAGS.image, cv2.IMREAD_COLOR)
    if bgr is None:
        raise SystemExit(f"Could not read image: {FLAGS.image}")

    candidates = []
    if not FLAGS.no_plate_detect:
        roi = find_plate_roi(bgr)
        if roi is not None:
            candidates.append(("roi", roi))
    candidates.append(("full", bgr))  # fallback

    best_text = ""
    best_img = None
    for _name, cand in candidates:
        text, thr = ocr_text(cand)
        if text:
            best_text = text
            best_img = thr
            break

    print(best_text if best_text else "(no text detected)")

    if FLAGS.show:
        cv2.imshow("input", bgr)
        if best_img is not None:
            cv2.imshow("best_thr", best_img)
        cv2.waitKey(0)


if __name__ == "__main__":
    app.run(main)
