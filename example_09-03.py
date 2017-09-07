import cv2
import sys


def switch_off_function():
    print('Pause')


def switch_on_function():
    print('Run')


def switch_callback(position):
    global g_switch_value
    g_switch_value = position    # Need this since you can't pass
                                 # pointer to g_switch_value
                                 # when createTrackbar is called
                                 # below in main.
    if position == 0:
        switch_off_function()
    else:
        switch_on_function()


def help():
    print('Call: python3 example_09-03.py video.avi')
    print('    Shows putting a pause button in a video.')


if __name__ == '__main__':
    global g_switch_value
    g_switch_value = 1

    help()
    g_capture = cv2.VideoCapture()

    if len(sys.argv) < 2 or not g_capture.open(sys.argv[1]):
        print('Failed to open video file.\n')
                # Original has argv[1] in error message, but that
                # fails is len < 2.
        exit(-1)

    cv2.namedWindow('Example 9-3', cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar('Switch', 'Example 9-3', g_switch_value,
            1, switch_callback)

    while True:
        if g_switch_value:
            r, frame = g_capture.read()    # g_capture >> frame

            if not r:    # if (frame.empty)
                break

            cv2.imshow('Example 9-3', frame)

        if cv2.waitKey(10) == 27:    # 10 ms may be too fast
            break                    # depending on video file.

    exit(0)
