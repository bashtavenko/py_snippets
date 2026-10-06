"""
EasyOCR with bounding box visualization.
Draws the detected boxes and text on the image and saves it to an output dir.
https://github.com/jaidedai/easyocr
"""
import os

import cv2
import easyocr
import numpy as np
from absl import app, flags, logging

FLAGS = flags.FLAGS

flags.DEFINE_string("image", "testdata/21.jpeg", "Path to an image")
flags.DEFINE_string("output_dir", "output", "Directory to save the annotated image")

GREEN = (0, 255, 0)


def run(_argv):
    img = cv2.imread(FLAGS.image)
    if img is None:
        raise app.UsageError(f"Could not read image: {FLAGS.image}")

    reader = easyocr.Reader(["en"])
    results = reader.readtext(img)

    for bbox, text, conf in results:
        logging.info("Detected: %s (confidence: %.2f%%)", text, conf * 100)

        pts = np.array(bbox, dtype=np.int32).reshape((-1, 1, 2))
        cv2.polylines(img, [pts], isClosed=True, color=GREEN, thickness=1)

        # Show recognized text
        x, y = int(bbox[0][0]), int(bbox[0][1])
        y_text = y - 5 if y > 15 else int(bbox[2][1]) + 15
        cv2.putText(img, f"{text} ({conf:.2f})", (x, y_text),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, GREEN, 1, cv2.LINE_AA)

    os.makedirs(FLAGS.output_dir, exist_ok=True)
    name, ext = os.path.splitext(os.path.basename(FLAGS.image))
    out_path = os.path.join(FLAGS.output_dir, f"{name}_annotated{ext}")
    cv2.imwrite(out_path, img)
    logging.info("Saved annotated image to %s", out_path)


if __name__ == "__main__":
    app.run(run)