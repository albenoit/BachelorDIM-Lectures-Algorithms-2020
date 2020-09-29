import cv2
import numpy as np
img_gray=cv2.imread('img.jpg',0)
img_bgr=cv2.imread('6490.jpg',1)

width = int(img_bgr.shape[1] * 0.6)
height = int(img_bgr.shape[0] * 0.2)
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

def invert_colors_numpy(img:np.ndarray):  
    return 255-img

def invert_colors_opencv(img:np.ndarray):  
    return ~img

def threshold_image_manual(img:np.ndarray):
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 nd array')
        
    newImg = np.zeros(img.shape, dtype=np.uint8)
    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            for channel in range (img.shape[2]):
                if img[row, col, channel] < 128:
                    newImg[row, col, channel] = 0
                else:
                    newImg[row, col, channel] = 255
    return newImg

def threshold_image_numpy(img:np.ndarray):
    thresold_value = 128
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 nd array')
    return img > thresold_value


img_bgr = threshold_image_manual(img_bgr)

img_thresolded = threshold_image_numpy(img_bgr)
img_thresolded_disp = img_thresolded.astype(np.uint8)*255
#cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.imshow("BGR trhesold image", img_thresolded_disp)
cv2.waitKey()