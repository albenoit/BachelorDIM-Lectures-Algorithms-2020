import pytest
import S3_imgproc_tools as algo

def test_invert_colors_numpy_None():
    with pytest.raises(ValueError):
        algo.invert_color_numpy(None)


def test_invert_colors_numpy_Aray():
    with pytest.raises(TypeError):
        algo.invert_color_numpy(1)

def test_invert_colors_numpy_uint8():
    with pytest.raises(TypeError):
        algo.invert_color_numpy(null_matrix)