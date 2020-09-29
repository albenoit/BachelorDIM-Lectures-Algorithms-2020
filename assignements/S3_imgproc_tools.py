import cv2
import numpy as np
# img_gray=cv2.imread('P:/DIM/ALGO/BachelorDIM-Lectures-Algorithms-2020/assignements/myimage.jpg',0)
# img_bgr=cv2.imread('P:/DIM/ALGO/BachelorDIM-Lectures-Algorithms-2020/assignements/myimage.jpg',1)
img=cv2.imread('P:/DIM/ALGO/BachelorDIM-Lectures-Algorithms-2020/assignements/myimage.jpg')
#display the matrix shapes
# print("Gray levels image shape = "+str(img_gray.shape))
# print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images
# cv2.imshow("Gray levels image", img_gray)
# cv2.imshow("BGR image", img_bgr)
# cv2.waitKey()




def invert_colors_manual(img):
    img_out = np.zeros(img.shape, dtype=np.uint8)
    img_out = 255-img
    cv2.imshow('img_out', img_out)
    cv2.waitKey()
    return print(img_out.shape)

invert_colors_manual(img)