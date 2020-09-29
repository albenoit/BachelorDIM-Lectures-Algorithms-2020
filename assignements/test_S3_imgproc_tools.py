import numpy as np
import pytest
import S3_imgproc_tools as algo
null_matrix = np.zeros((10, 10), dtype = bool)

def test_invert_colors_numpy_None():
    with pytest.raises(ValueError):
        algo.inv_gray_levels(None)


def test_invert_colors_numpy_Aray():
    with pytest.raises(TypeError):
        algo.inv_gray_levels(1)

def test_invert_colors_numpy_uint8():
    with pytest.raises(TypeError):
        algo.inv_gray_levels(null_matrix)