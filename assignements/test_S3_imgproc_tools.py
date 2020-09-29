import pytest
import numpy as np
import S3_imgproc_tools as imgproc

def test_invert_colors_tuNone():
    with pytest.raises(AttributeError):
        imgproc.invert_colors_manual(None)
    
def test_invert_colors_tuArray():
    with pytest.raises(AttributeError):
        imgproc.invert_colors_manual(1)
    
def test_invert_colors_tuUint8():
    with pytest.raises(TypeError):
        imgproc.invert_colors_manual(np.zeros((2,2), dtype=np.float32))

def test_invert_colors_tuProcessOK():
    imgproc.invert_colors_manual(np.zeros((2,2,2), dtype=np.uint8))
