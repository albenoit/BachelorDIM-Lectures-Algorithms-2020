import cv2
import numpy as np
img_gray=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg',0) 
img_bgr=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg',1) 
img=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg') 
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

img_out=np.zeros(img.shape,dtype=np.uint8)
for row in range (img.shape[0]):
    for col in range (img.shape[1]):
        for channel in range (img.shape[2]):
            img_out[row,col,channel]=255-img[row,col,channel]

cv2.imshow('img out ', img_out)
cv2.waitKey()