import cv2
import sys

if __name__ == '__main__':
    src1 = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    src2 = cv2.imread(sys.argv[2], cv2.IMREAD_COLOR)
    
    if len(sys.argv) == 9 and not src1 is None and not src2 is None:
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        w = int(sys.argv[5])
        h = int(sys.argv[6])
        alpha = float(sys.argv[7])
        beta = float(sys.argv[8])
        
        roi1 = src1[x:(x + w), y:(y + h)]
        roi2 = src2[0:w, 0:h]
        
        cv2.addWeighted(roi1, alpha, roi2, beta, 0.0, roi1)
        
        cv2.namedWindow('Alpha Blend', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Alpha Blend', src1)  # Book has src2 as second
                                         # argument.
        cv2.waitKey(0)
