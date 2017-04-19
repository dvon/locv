import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow('Example 2-3', cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(sys.argv[1])  # cap = cv2.VideoCapture()
                                         # cap.open(sys.argv[1])
    while True:
        r, frame = cap.read()

        if not r:  # if frame is None:
            break
        
        cv2.imshow('Example 2-3', frame)
 
        if cv2.waitKey(33) != 255:  # waitKey(n > 0) supposed to
            break                   # return -1 if no key pressed
                                    # within n ms.  Python treats
                                    # return value as unsigned byte
                                    # (I think), so -1 becomes 255.
