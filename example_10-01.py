import cv2
import sys

def sum_rgb(src):
    # Split image onto the color planes.
    planes = cv2.split(src)
    b, g, r = planes
    
    # Add equally weighted rgb values.
    s = cv2.addWeighted(r, 1 / 3, g, 1 / 3, 0)
    s = cv2.addWeighted(s, 1, b, 1 / 3, 0)
    
    # Truncate values above 100.
    t, dst = cv2.threshold(s, 100, 100, cv2.THRESH_TRUNC)

    return dst


def help():
    print('Call: python3 example_10-01.py image.jpg')
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
