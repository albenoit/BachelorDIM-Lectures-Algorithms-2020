# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import cv2
import numpy as np
test=cv2.imread('test.jpg',0)
test1=cv2.imread('test.jpg',1)
cv2.imshow("test",test)
cv2.imshow("test1",test1)
cv2.waitKey()

