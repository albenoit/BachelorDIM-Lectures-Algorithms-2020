import cv2 
import numpy as np

def invers_img(image:np.ndarray):
    '''
    if(img is None):
        raise ValueError("L'image est vide")
    if not(isinstance(image, np.ndarray)):
        raise TypeError("expected an nd array")
    '''
    if image.dtype != np.dtype(np.uint8):
        raise TypeError("expected uint8 typed nd array")
    '''
    image_out = np.zeros(image.shape, dtype=np.uint8)
    for row in range (image.shape[0]):
        for col in range (image.shape[1]):
            for channel in range (image.shape[2]):
                image_out[row,col,channel] = 255 - image[row,col,channel]
    '''
    image_out = ~image
    return image_out
    
def threshold(img:np.ndarray):
    threshold_value=128
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError("expected uint8 typed nd array")
    return img>threshold_value

img=cv2.imread('image_test.jpg')
cv2.imshow('img', img)
cv2.imshow('invers_img', invers_img(img))
cv2.waitKey()

img=cv2.imred('''TODO''')
img_thresholded = threshold(img)
img_thresholded_disp = img_thresholded.astype(np.uint8)*255
cv2.imshow('seuilled image', img_thresholded_disp)