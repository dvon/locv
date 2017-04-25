import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow('Example 1', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Example 2', cv2.WINDOW_AUTOSIZE)

    img1 = cv2.imread(sys.argv[1])  # Book has img instead of img1.
    cv2.imshow('Example 1', img1)

    img2 = cv2.pyrDown(img1)
    cv2.imshow('Example 2', img2)

    cv2.waitKey(0)
