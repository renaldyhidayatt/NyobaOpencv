import numpy as np
import cv2


canvas = np.zeros((300, 300, 3), dtype="uint8")


def display(winname, image):
    cv2.imshow(winname, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# display("canvas", canvas)


for i in range(0, 25):
    radius = np.random.randint(5, 200)
    color = np.random.randint(0, 256, size=(3,)).tolist()
    pt = np.random.randint(0, 300, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

display("canvas", canvas)

cv2.imwrite("canvas.png", canvas)
