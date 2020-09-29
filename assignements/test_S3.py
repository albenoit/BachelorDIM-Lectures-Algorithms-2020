import S3_imgproc_tools as tobetested
import pytest

def test_innv_gray_levels_tuNone():
    with pytest.raises(AttributeError):
        innv_gray_levels(None)

def test_innv_gray_levels_tuArray():
    with pytest.raises(AttributeError):
        innv_gray_levels(1)

def test_innv_gray_levels_tuuint8():
    with pytest.raises(TypeError):
        innv_gray_levels(np.zeros((2,2), dtype=np.float32))

def test_innv_gray_levels_process():
    '''TODO'''

def test_innv_gray_levels_tuprocessOK():
