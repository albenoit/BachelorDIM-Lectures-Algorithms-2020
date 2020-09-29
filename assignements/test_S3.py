import S3_imgproc_tools as tobetested
import pytest
import numpy as np

def test_invert_color_numpy_tuNone():
    with pytest.raises(ValueError):
        tobetested.invert_color_numpy(None)

def test_invert_color_numpy_tuArray():
    with pytest.raises(TypeError):
        tobetested.invert_color_numpy(1)

def test_invert_color_numpy_tuuint8():
    with pytest.raises(TypeError):
        tobetested.invert_color_numpy(np.zeros((2,2), dtype=np.float32))