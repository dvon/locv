import cv2
import numpy
import sys

def sum_rgb(src):
    # Split image onto the color planes.
    planes = cv2.split(src)
    b, g, r = planes
    
    # Accumulate separate planes, combine and threshold.
    s = numpy.zeros(b.shape, dtype=numpy.float32)
    s = cv2.accumulate(b, s)
    s = cv2.accumulate(g, s)
    s = cv2.accumulate(r, s)

    s = s / 3  # Need this if you want output to match that of
               # the previous example.

    # Truncate values above 100 and rescale into dst.
    t, s = cv2.threshold(s, 100, 100, cv2.THRESH_TRUNC)
    dst = s.astype(b.dtype)

    return dst


def help():
    print('Call: python3 example_10-02.py image.jpg')
    print('    Shows use of alpha blending (addWeighted) and')
    print('    threshold.')


if __name__ == '__main__':
    help()
    
    if len(sys.argv) < 2:
        print('Specify output image.')
        exit(-1)
    
    src = cv2.imread(sys.argv[1])
    
    if src is None:
        print("Can not load", sys.argv[1])
        exit(-1)
    
    dst = sum_rgb(src)
    cv2.imshow(sys.argv[1], dst)
    cv2.waitKey(0)
