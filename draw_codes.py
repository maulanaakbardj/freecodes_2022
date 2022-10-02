import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
draw = False
ix = -1
iy = -1


def draw_rect(event, x, y, flags, param):
    global ix, iy, draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(img, (x, y), 10, (255, 0, 0), -10)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img, (x, y), 10, (255, 0, 0), -10)


cv2.namedWindow(winname='My_Drawing')
cv2.setMouseCallback('My_Drawing', draw_rect)
while True:
    cv2.imshow('My_Drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
