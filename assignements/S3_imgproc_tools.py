import cv2
import numpy as np
img = cv2.imread('/home/fabien/Pictures/algo_img.jpg')

print("input image shape", img.shape)

cv2.imshow('input', img)
cv2.waitKey()

img_out = np.zeros(img.shape, dtype=np.uint8)

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        for channel in range (img.shape[2]):
            img_out[row, col, channel] = 255-img[row, col, channel]

cv2.imshow("output", img_out)
cv2.waitKey()


def invert_colors_numpy(input_img):
    '''

    This function reverse the color of an image
    Parameters:
        input_img: an image
    Returns: a reversed image. It's the optimal solution.

    '''
    return 255 - input_img


img_gray = cv2.imread("/home/fabien/Pictures/algo_img.jpg", 0)
img_bgr = cv2.imread("/home/fabien/Pictures/algo_img.jpg", 1)
img_bgr_reversed = invert_colors_numpy(cv2.imread("/home/fabien/Pictures/algo_img.jpg", 1))

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.imshow("BGR image inverted", img_bgr_reversed)
cv2.waitKey()


