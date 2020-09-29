import cv2
import numpy as np
img_gray=cv2.imread('img.jpg',0)
img_bgr=cv2.imread('6490.jpg',1)

scale_percent = 20
width = int(img_bgr.shape[1] * scale_percent / 100)
height = int(img_bgr.shape[0] * scale_percent / 100)
dsize = (width, height)
img_bgr = cv2.resize(img_bgr, dsize)

def invert_colors_manual(img:np.ndarray):
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 nd array')
        
    newImg = np.zeros(img.shape, dtype=np.uint8)
    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            for channel in range (img.shape[2]):
                newImg[row, col, channel] = 255 - img[row, col, channel]
    return newImg

def invert_colors_numpy(img):  
    return 255-img

def invert_colors_opencv(img):  
    return ~img

img_bgr = invert_colors_manual(img_bgr)

#cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey()