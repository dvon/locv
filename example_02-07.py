import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow('Example Gray', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Example Canny', cv2.WINDOW_AUTOSIZE)

    img_rgb = cv2.imread(sys.argv[1])

    img_gry = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Example Gray', img_gry)

    img_cny = cv2.Canny(img_gry, 10, 100, 3, L2gradient=True)
            # Book just has True as last argument, but Python
            # method has an additional parameter after the
            # aperture size (the 3).  So I needed to add
            # L2gradient= (or to just remove the fifth argument,
            # that also works).

    cv2.imshow('Example Canny', img_cny)

    cv2.waitKey(0)
