import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow('Example 2-8', cv2.WINDOW_AUTOSIZE)
    img_rgb = cv2.imread(sys.argv[1])

    img_gry = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_pyr = cv2.pyrDown(img_gry)
    img_pyr2 = cv2.pyrDown(img_pyr)
    img_cny = cv2.Canny(img_pyr2, 10, 100, 3, L2gradient=True)
            # Added L2gradient= (see longer comment in
            # example_02-07.py).

    cv2.imshow('Example 2-8', img_cny)
    cv2.waitKey(0)
