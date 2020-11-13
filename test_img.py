# TU1 imgarray is None
# TU2 image non nbarray
#     si bien uint8
# TU3 test resultat

import cv2
import pytest
import S3_imgproc_tools as S3
import numpy as np

img_gray = cv2.imread('image.jpg', 0)
img_bgr = cv2.imread('image.jpg', 1)

def test_innv_gray_levels_tuNone():
    with pytest.raises(ValueError):
        S3.innv_gray_levels(None)

def test_innv_gray_levels_tuArray():
    with pytest.raises(TypeError):
        S3.innv_gray_levels(1)

def test_innv_gray_levels_tuuint8():
    with pytest.raises(TypeError):
        S3.innv_gray_levels(np.zeros((2,2), dtype=np.float32))

# def test_innv_gray_levels_tuOk():
#     with pytest.raises