import cv2
import numpy as np

img_grey = cv2.imread('prophecy.png', 0)
img_bgr = cv2.imread('prophecy.png', 1)

print("Grey levels image shape = " + str(img_grey.shape))
print("BGR image shape = " + str(img_bgr.shape))

cv2.imshow("Gray levels image", img_grey)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey()

def invert_color_manual(input_image):
    '''
    This function takes an image and reverse its color.

    :param
        input_image: an image
    :return:
        nothing, just print the new image out
    '''
    img_out = np.zeros(input_image.shape, dtype=np.uint8)
    for row in range(input_image.shape[0]):
        for col in range(input_image.shape[1]):
            for channel in range(input_image.shape[2]):
                img_out[row, col, channel] = 255 - input_image[row, col, channel]

    cv2.imwrite("reversed_prophecy.png", img_out)
    cv2.imshow("reversed colors", img_out)
    cv2.waitKey()

invert_color_manual(img_bgr)