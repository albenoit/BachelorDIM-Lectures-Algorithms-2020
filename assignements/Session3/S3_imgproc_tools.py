import cv2
import numpy as np
img_gray=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg',0) 
img_bgr=cv2.imread('P:/DIM/algo/BachelorDIM-Lectures-Algorithms-2020/assignements/Session3/images/raoult.jpg',1) 
#display the matrix shapes
print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images
#cv2.imshow("Gray levels image", img_gray)
#cv2.imshow("BGR image", img_bgr)
#cv2.waitKey()

def invert_colors_manual():
    return True