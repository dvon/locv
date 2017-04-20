import cv2
import sys

if __name__ == '__main__':
    img_rgb = cv2.imread(sys.argv[1])
    img_gry = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_pyr = cv2.pyrDown(img_gry)
    img_pyr2 = cv2.pyrDown(img_pyr)
    img_cny = cv2.Canny(img_pyr2, 10, 100, 3, L2gradient=True)
    
    x = 16
    y = 32
    
    intensity = img_rgb[y, x]
    blue, green, red = intensity
    
    print('At (x, y) = ({}, {}): (blue, green, red) = ({}, {}, {})'.format(
            x, y, blue, green, red))

    print('Gray pixel there is: {}'.format(img_gry[y, x]))
    
    x //= 4
    y //= 4
    
    print('Pyramid2 pixel there is: {}'.format(img_pyr2[y, x]))
    
    img_cny[y, x] = 128
    
    cv2.imshow('Example 2-9', img_cny)
    cv2.waitKey(0)
