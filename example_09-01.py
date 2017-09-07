import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow(sys.argv[1], cv2.WINDOW_AUTOSIZE)
    img = cv2.imread(sys.argv[1])
    cv2.imshow(sys.argv[1], img)

    while True:
        if cv2.waitKey(100) == 27:
            break

    cv2.destroyWindow(sys.argv[1])
    exit(0)
