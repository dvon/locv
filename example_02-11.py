import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow('Example 2-11 (original)', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Example 2-11 (log-polar)', cv2.WINDOW_AUTOSIZE)

    capture = cv2.VideoCapture(sys.argv[1])

    fps = int(capture.get(cv2.CAP_PROP_FPS))
    size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    writer = cv2.VideoWriter(sys.argv[2],
            cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
            # Book has CV_FOURCC('M', 'J', 'P', 'G').

    while True:
        r, bgr_frame = capture.read()

        if not r:
             break

        cv2.imshow('Example 2-11 (original)', bgr_frame)

        logpolar_frame = cv2.logPolar(bgr_frame,
                (bgr_frame.shape[0] // 2, bgr_frame.shape[1] // 2),
                40, cv2.WARP_FILL_OUTLIERS)
                # Book has, e.g., bgr_frame.cols / 2...

        cv2.imshow('Example 2-11 (log-polar)', logpolar_frame)
        writer.write(logpolar_frame)

        c = cv2.waitKey(10)

        if c == 27:
            break

    capture.release()
