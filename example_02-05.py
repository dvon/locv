import cv2
import sys

def example2_5(image):
    cv2.namedWindow('Example 2-5 (in)', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Example 2-5 (out)', cv2.WINDOW_AUTOSIZE)
    
    cv2.imshow('Example 2-5 (in)', image)
    
    out = cv2.GaussianBlur(image, (5, 5), 3, 3)
    out = cv2.GaussianBlur(out, (5, 5), 3, 3)
    
    cv2.imshow('Example 2-5 (out)', out)
    
    cv2.waitKey(0)

# Book has only example2_5 function.
if __name__ == '__main__':
    example2_5(cv2.imread(sys.argv[1]))
