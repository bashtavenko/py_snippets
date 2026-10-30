"""
Examples of contours detection and preprocessing
"""
import cv2
import numpy as np

SIZE = 512


def generate():
    rng = np.random.default_rng(7)
    clean = np.zeros((SIZE, SIZE), np.uint8)
    cv2.circle(clean, (130, 150), 70, 255, -1)
    cv2.rectangle(clean, (300, 80), (440, 220), 255, -1)
    cv2.rectangle(clean, (100, 330), (420, 430), 255, -1)
    d = clean.copy()
    cv2.line(d, (200, 150), (300, 150), 255, 1)  # bridge between circle and square
    cv2.line(d, (130, 220), (130, 330), 255, 1)  # bridge between circle and bar
    cv2.line(d, (100, 380), (420, 380), 0, 1)  # crack through the bar
    noise = rng.random(d.shape) < 0.005  # salt on background, pepper inside shapes
    d[noise & (clean == 0)] = 255
    d[noise & (clean > 0)] = 0
    return clean, d


def solve(distorted):
    # Remove salt and pepper noise
    result = cv2.medianBlur(distorted, 3)

    # Find areas of contours
    contours, _ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area = cv2.contourArea(contours[0])
    print(f"Area: {area}")

    return result


def main():
    clean, distorted = generate()
    current = solve(distorted.copy())
    cv2.imshow("clean | distorted | current)", np.hstack([clean, distorted, current]))
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
