import numpy
import cv2

def draw_box(img, box):
    tl = (box[0], box[1])
    br = (box[0] + box[2], box[1] + box[3])
    cv2.rectangle(img, tl, br, (0, 0, 255))
            # cv.rectangle(img, box.tl(), box.br(),
            #         cv::Scalar(0x00, 0x00, 0xff))


def help():
    print('Call: python3 example_09-02.py')
    print('    Shows how to use a mouse to draw regions in an image.')


# After main in original example.
def my_mouse_callback(event, x, y, flags, param):
    global box, drawing_box

    image = param

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing_box:
            box[2] = x - box[0]    # box.width = x - box.x
            box[3] = y - box[1]    # box.height = y - box.y

    elif event == cv2.EVENT_LBUTTONDOWN:
        drawing_box = True
        box = [x, y, 0, 0]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing_box = False

        if box[2] < 0:
            box[0] += box[2]
            box[2] *= -1

        if box[3] < 0:
            box[1] += box[3]
            box[3] *= -1

        draw_box(image, box)


if __name__ == '__main__':
    global box, drawing_box

    drawing_box = False

    help()
    box = [-1, -1, 0, 0]
            # ...cv::Rect(-1, -1, 0, 0)
    image = numpy.zeros((200, 200, 3), dtype=numpy.uint8)
            # cv::Mat image(200, 200, CV_8UC3)

    # Three extra lines here in original example?

    cv2.namedWindow('Box Example')
    cv2.setMouseCallback('Box Example', my_mouse_callback, image)

    while True:
        temp = image.copy()

        if drawing_box:
            draw_box(temp, box)

        cv2.imshow('Box Example', temp)

        if cv2.waitKey(15) == 27:
            break
