import cv2
import sys

if __name__ == '__main__':
    img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
            # Book has -1 for second argument.

    if img is None:
        exit(-1)

    cv2.namedWindow('Example 2-1', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Example 2-1', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Example 2-1')
