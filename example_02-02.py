from cv2 import *
import sys

if __name__ == '__main__':
    img = imread(sys.argv[1], IMREAD_UNCHANGED)
            # Book has -1 for second argument.

    if img is None:
        exit(-1)

    namedWindow('Example 2-1', WINDOW_AUTOSIZE)
    imshow('Example 2-1', img)
    waitKey(0)
    destroyWindow('Example 2-1')
