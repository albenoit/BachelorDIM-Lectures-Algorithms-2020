import cv2
import numpy as np
import pytest
import S3_imgproc_tools as algo


'''Start TU innv_gray_levels'''
def test_innv_gray_levels_tuNone():
    with pytest.raises(ValueError):
        algo.innv_gray_levels(None)

def test_innv_gray_levels_tuArray():
    with pytest.raises(ValueError):
        algo.innv_gray_levels(1)

def test_innv_gray_levels_tuuint8():
    with pytest.raises(ValueError):
        algo.innv_gray_levels(np.zeros((2,2), dtype=np.float32))

def test_innv_gray_levels_tuprocessOK():
    with pytest.raises(ValueError):
        algo.innv_gray_levels(None)

'''End TU innv_gray_levels'''