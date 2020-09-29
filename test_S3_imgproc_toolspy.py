import S3_imgproc_toolspy as S3
import pytest
import numpy as np
import cv2

def test_inverse_img_tuNone():
    with pytest.raises(AttributeError):
        S3.invers_img(None)

def test_inverse_img_tuArray():
    with pytest.raises(AttributeError):
        S3.invers_img(1)

def test_inverse_img_tuuint8():
    with pytest.raises(TypeError):
        S3.invers_img(np.zeros((2,2), dtype=np.float32))

    
    