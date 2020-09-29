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
    input_image = (255-input_image)
    cv2.imwrite("reversed_prophecy.png", input_image)
    cv2.imshow("reversed colors", input_image)
    cv2.waitKey()

invert_color_manual(img_bgr)