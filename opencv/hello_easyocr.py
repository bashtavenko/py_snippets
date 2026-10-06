"""
Basic OCR with EasyOCR
https://github.com/jaidedai/easyocr
"""
import easyocr
from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_string("image", "testdata/21.jpeg", "Path to an image")

def run(_argv):
    reader = easyocr.Reader(["en"])
    results = reader.readtext(FLAGS.image)

    for bbox, text, conf in results:
        print(f"Detected: {text} (confidence: {conf:.2%})")

if __name__ == "__main__":
    app.run(run)
