import cv2
import sys

if __name__ == '__main__':
    cap = cv2.VideoCapture(sys.argv[1])

    f = int(cap.get(cv2.CAP_PROP_FOURCC))  # I tried four different
                                           # video files, but all I
                                           # ever get is zero here.

    fourcc = f.to_bytes(4, byteorder='little').decode()
            # Book assumes little-endian byte order so I did too.
