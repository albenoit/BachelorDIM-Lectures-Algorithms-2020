import cv2
import numpy as np
img=cv2.imread("BachelorDIM-Lectures-Algorithms-2020/assignements/iuCkR.jpg")
img_gray=cv2.imread("BachelorDIM-Lectures-Algorithms-2020/assignements/iuCkR.jpg", 0)
img_bgr=cv2.imread("BachelorDIM-Lectures-Algorithms-2020/assignements/iuCkR.jpg", 1)

def invert_gray_lvl_image(img : np.ndarray):
    '''
    Function to invert image colors with highest CPU demanding processing
    Parameters :
        img: image nd array
    Returns :
        imgRet image inverted
    '''
    img_out=np.zeros(img.shape, dtype=np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for channel in range(img.shape[2]):
                img_out[row, col, channel]=255-img[row, col, channel]
    return img_out

def invert_gray_lvl_image_light(img : np.ndarray):
    '''
    Function to invert image colors with lower CPU demanding processing
    Parameters :
        img: image nd array
    Returns :
        imgRet image inverted
    '''
    # imgRet=np.zeros(img.shape, dtype=np.uint8)
    # if img is None:
    #     raise ValueError('expected an uint8 nd array')
    # if not(isinstance(img, np.ndarray)):
    #     raise TypeError('expected an nd array')
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')

    imgRet = 255-img
    return imgRet

def invert_color_opencv(img : np.ndarray):
    '''
    Function to invert image colors with opencv method
    Parameters :
        img: image nd array
    Returns :
        imgRet image inverted
    '''
    return ~img


def threshold(img : np.ndarray):
    threshold_value=128
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')
    return img > threshold_value

print(threshold(img))
# stream=cv2.VideoCapture(0)


# while True:
#     ok, imgStream=stream.read()
#     cv2.imshow("Inverted image", invert_gray_lvl_image_light(imgStream))
#     cv2.waitKey(1)

# cv2.imshow("test", invert_color_opencv(img))
# cv2.waitKey()

#display matrix
# print("Gray levels image shape = "+str(img_gray.shape))
# print("BGR levels image shape = "+str(img_bgr.shape))

#display images
# cv2.imshow("Gray lvl image", img_gray)
# cv2.imshow("Bgr lvl image", img_bgr)
# cv2.waitKey()



