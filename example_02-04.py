import cv2
import sys

g_slider_position = 0
g_run = 1
g_dontset = 0
g_cap = cv2.VideoCapture()

def onTrackbarSlide(pos):
    global g_run, g_dontset

    g_cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    if not g_dontset:
        g_run = 1

    g_dontset = 0

if __name__ == '__main__':
    cv2.namedWindow('Example 2-4', cv2.WINDOW_AUTOSIZE)
    g_cap.open(sys.argv[1])

    frames = int(g_cap.get(cv2.CAP_PROP_FRAME_COUNT))
            # Depending on the video file this might return 0,
            # causing the program to fail later on when you click
            # the trackbar.

    tmpw   = int(g_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    tmph   = int(g_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print('Video has {} frames of dimensions({}, {}).'.format(
            frames, tmpw, tmph))

    cv2.createTrackbar(
            'Position', 'Example 2-4', g_slider_position, frames,
            onTrackbarSlide)

    while True:
        if g_run != 0:
            r, frame = g_cap.read()

            # When we get to the end of the file, r will be
            # False.  Without this program ends with and error
            # message when at the end of the file.
            if not r:
                break

            current_pos = int(g_cap.get(cv2.CAP_PROP_POS_FRAMES))
            g_dontset = 1

            cv2.setTrackbarPos(
                    'Position', 'Example 2-4', current_pos)
            cv2.imshow('Example 2-4', frame)

            g_run -= 1

        c = cv2.waitKey(10)

        if chr(c) == 's':
            g_run = 1
            print('Single step, run =', g_run)

        elif chr(c) == 'r':
            g_run = -1
            print('Run mode, run =', g_run)

        elif c == 27:  # escape key
            break
