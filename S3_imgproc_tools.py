import cv2
import numpy as np
stream = cv2.VideoCapture(0)

img_gray = cv2.imread('image.jpg', 0)
img_bgr = cv2.imread('image.jpg', 1)

print("Gray levels image", str(img_gray.shape))
print("BGR image", str(img_bgr.shape))

# cv2.imshow("Gray levels image", img_gray)
# cv2.imshow("BGR image", img_bgr)
# cv2.waitKey()

# jusqu'a 128 = invert

def invert_color_manual(input_img):
    '''
    Invert colors of a given image

    Parameters:
        input_img: the image you want to invert colors

    Returns: the inverted colors image
    '''
    if input_img is None:
        raise ValueError('expected an uint8 nd array')
    # if isinstance(input_img, np.ndarray()):
    #     raise TypeError('expected np array')
    if input_img.dtype != np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')

    inverted_img = np.zeros(input_img.shape, dtype=np.uint8)

    inverted_img = 255 - input_img

    # for row in range(input_img.shape[0]):
    #     for col in range(input_img.shape[1]):
    #         for channel in range(input_img.shape[2]):
    #             inverted_img[row, col, channel] = 255 - input_img[row, col, channel]

    return 255 - input_img

def threshold_image_manual(input_img):
    '''
    Threshold the colors of a given image

    Parameters:
        input_img: the image you want to threshold colors

    Returns: the threshold colors image
    '''
    threshold_img = np.zeros(input_img.shape, dtype=np.uint8)
    threshold_value = 128

    threshold_img = input_img > threshold_value

    return threshold_img 


while True:
    ok, okimg = stream.read()
    inverted_img = invert_color_manual(okimg)
    threshold_img = threshold_image_manual(okimg)
    threshold_img_cast = threshold_img.astype(np.uint8)*255
    threshold_img_inverted = threshold_image_manual(inverted_img)
    threshold_img_inverted_cast = threshold_img_inverted.astype(np.uint8)*255

    cv2.imshow("test", inverted_img)
    cv2.waitKey(1)

    # cv2.imshow("test", threshold_img_cast)
    # cv2.waitKey(1)

    # cv2.imshow("test", threshold_img_inverted_cast)
    # cv2.waitKey(1)