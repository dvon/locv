import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow('Example 2-10', cv2.WINDOW_AUTOSIZE)

    if len(sys.argv) == 1:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(int(sys.argv[1]))

    if not cap.isOpened():
        print("Couldn't open capture.", file=sys.stderr)
        exit(-1)

    # From example 2-3...
    while True:
        r, frame = cap.read()

        if not r:
            break

        cv2.imshow('Example 2-10', frame)

        if cv2.waitKey(33) != 255:
            break
