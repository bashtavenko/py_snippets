"""
Basic OCR with Tesseract
"""
import cv2
import pytesseract
from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_string("image", "testdata/sample.jpeg", "Path to an image")

# https://github.com/madmaze/pytesseract
def run(_argv):
    bgr = cv2.imread(FLAGS.image)
    if bgr is None:
        raise SystemExit(f"Could not read image: {FLAGS.image}")

    text = pytesseract.image_to_string(FLAGS.image).strip()
    print(text if text else "(no text detected)")


if __name__ == "__main__":
    app.run(run)
