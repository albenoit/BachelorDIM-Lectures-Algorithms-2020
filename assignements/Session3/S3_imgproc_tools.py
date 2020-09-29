import cv2
import numpy as np
img_gray=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg',0) 
img_bgr=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg',1) 
img=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/covid19.jpg') 
#display the matrix shapes
#print("Gray levels image shape = "+str(img_gray.shape))
#print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images
#cv2.imshow("Gray levels image", img_gray)
#cv2.imshow("BGR image", img_bgr)
#cv2.waitKey()

#def invert_colors_manual(img):
#    for i in range(img.shape[0]):
#        for j in range(img.shape[1]):
#            for k in range(img.shape[2]):
#            print(img[i,j,k])
#    return print(img.shape)
#
#invert_colors_manual(img)

print('input image shape',img.shape)

cv2.imshow('input',img)


def invert_colors_manual(img):
    '''
        This function invert color
        Parameters:
            img: image
        Returns:
            image with color inversion
        Raises:
            
    '''
    img_out=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/covid19.jpg') 
    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            for channel in range (img.shape[2]):
                img_out[row,col,channel]=255-img[row,col,channel]

    return img_out


def invert_colors_numpy(img):
    '''
        This function invert color with numpy
        Parameters:
            img: image
        Returns:
            image with color inversion
        Raises:
            
    '''
    img_out=np.zeros(img.shape,dtype=np.uint8)
    img_out=255-img
    return img_out

def  invert_colors_opencv(img):
    '''
        This function invert color with opencv
        Parameters:
            img: image
        Returns:
            image with color inversion
        Raises:
            
    '''
    img_out=cv2.bitwise_not(img)
    return img_out

cv2.imshow('img out ', invert_colors_manual(img))
cv2.waitKey()



def innv_gray_levels(img:np.ndarray):
    '''test data type, expecting uint8'''
    '''not usefull

    if img is None:
        raise ValueError('Expected an uint8')
    if img.dtype != np.dtype(np.uint8):
        raise ValueError('Expected uint8 typed nd array')
    if isinstance(img, np.ndarray):
        raise ValueError('Expected an nd array')
    '''

    if img.dtype != np.dtype(np.uint8):
        raise TypeError('Expected uint8 typed nd array')
    

    return 255-img

