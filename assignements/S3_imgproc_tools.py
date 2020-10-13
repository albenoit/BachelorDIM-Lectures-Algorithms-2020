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
    This function takes an image and reverse its color by looping on each pixels.

    :param
        input_image: an image
    :return:
        nothing, just print the new image out
    '''
    img_out = np.zeros(input_image.shape, dtype=np.uint8)
    for row in range(input_image.shape[0]):
        for col in range(input_image.shape[1]):
            for color in range(input_image.shape[2]):
                img_out[row, col, color] = 255 - input_image[row, col, color]

    cv2.imwrite("reversed_prophecy.png", img_out)
    cv2.imshow("reversed colors (manual)", img_out)
    cv2.waitKey()

def invert_color_numpy(input_image):
    '''
     This function takes an image and reverse its color by using a numpy operation.

    :param
        input_image: an image
    :return:
        nothing, just print the new image out
    '''
    if input_image is None:
        raise ValueError('Expected an uint8 nd array')
    if not(isinstance(input_image, np.ndarray)):
        raise TypeError('Expected an nd array')
    if input_image.dtype != np.dtype(np.unint8):
        raise TypeError('Expected unint8 typed nd array')

    img_out = 255 - input_image
    cv2.imwrite("reversed_prophecy.png", img_out)
    cv2.imshow("reversed colors (numpy)", img_out)
    cv2.waitKey()

def invert_color_opencv(input_image):
    '''
    This function takes an image and reverse its color by using a cv2 function.

    :param
        input_image: an image
    :return:
        nothing, just print the new image out
    '''
    img_out = cv2.bitwise_not(input_image)
    cv2.imwrite("reversed_prophecy.png", img_out)
    cv2.imshow("reversed colors (opencv)", img_out)
    cv2.waitKey()

#invert_color_manual(img_bgr)
#invert_color_numpy(img_bgr)
#invert_color_opencv(img_bgr)


def threshold_image_manual(input_image):
    img_out = np.zeros(input_image.shape, dtype=np.uint8)
    for row in range(input_image.shape[0]):
        for col in range(input_image.shape[1]):
            avgcolor = 0
            for color in range(input_image.shape[2]):           # Assemble all the color values of the pixel (R,G,B)
                avgcolor += input_image[row, col, color]
            avgcolor = avgcolor / 3                             # Get the average of it
            if avgcolor < (255/2):                              # If the color is between white and grey
                for i in range(3):
                    img_out[row, col, i] = 255                  # Change each rgb value to FF so it's white

    cv2.imwrite("threshold_prophecy.png", img_out)
    cv2.imshow("Threshold", img_out)
    cv2.waitKey()

def threshold_image_numpy(input_image):
    threshold_value = 255/2
    if input_image != np.dtype(np.uint8):
        raise TypeError('Expected uint8 typed nd array')

    if input_image > threshold_value:
        input_image = 255

    cv2.imwrite("threshold_prophecy.png", input_image)
    cv2.imshow("Threshold (numpy)", input_image)
    cv2.waitKey()

threshold_image_numpy(img_bgr)
# threshold_image_manual(img_bgr)