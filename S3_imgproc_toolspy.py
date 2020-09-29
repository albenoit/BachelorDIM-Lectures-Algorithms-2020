import cv2 
import numpy as np
def invers_img(image):
    if(img is None):
        raise ValueError("L'image est vide")
    if (isinstance(image, np.ndarray)):
        raise TypeError("expected an nd array")
    if image.dtype != np.dtype(np.uint8):
        raise TypeError("expected uint8 typed nd array")
    image_out = np.zeros(image.shape, dtype=np.uint8)
    for row in range (image.shape[0]):
        for col in range (image.shape[1]):
            for channel in range (image.shape[2]):
                image_out[row,col,channel] = 255 - image[row,col,channel]
    return image_out
    
img=cv2.imread('image_test.jpg')
cv2.imshow('img', img)
img_invers = ~img
#img_invers=invers_img(img)
cv2.imshow('invers_img', img_invers)
cv2.waitKey()

