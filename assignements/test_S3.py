import S3_imgproc_tools as tFile
import pytest
import numpy as np

# Invert color manual function
def test_invert_color_manual_tuNone():
    with pytest.raises(AttributeError):
        tFile.invert_color_manual(None)


def test_invert_color_manual_tuArray():
    with pytest.raises(AttributeError):
        tFile.invert_color_manual(1)


def test_invert_color_manual_tuuint8():
    with pytest.raises(TypeError):
        tFile.invert_color_manual(np.zeros((2, 2), dtype=np.float32))


# invert_gray_lvl_image_light function
def test_invert_gray_lvl_image_light_tuNone():
    with pytest.raises(ValueError):
        tFile.invert_gray_lvl_image_light(None)


def test_invert_gray_lvl_image_light_tuArray():
    with pytest.raises(TypeError):
        tFile.invert_gray_lvl_image_light(1)


def test_invert_gray_lvl_image_light_tuuint8():
    with pytest.raises(TypeError):
        tFile.invert_gray_lvl_image_light(np.zeros((2, 2), dtype=np.float32))


def test_invert_gray_lvl_image_light_process():
    """TODO"""


# invert_color_opencv function
def test_invert_color_opencv_tuNone():
    with pytest.raises(ValueError):
        tFile.invert_color_opencv(None)


def test_invert_color_opencv_tuArray():
    with pytest.raises(TypeError):
        tFile.invert_color_opencv(1)


def test_invert_color_opencv_tuuint8():
    with pytest.raises(TypeError):
        tFile.invert_color_opencv(np.zeros((2, 2), dtype=np.float32))


# threshold function
def test_threshold_tuNone():
    with pytest.raises(ValueError):
        tFile.threshold(None)


def test_threshold_tuuint8():
    with pytest.raises(TypeError):
        tFile.threshold(np.zeros((2, 2), dtype=np.float32))


# 2 - chargement image non array
# Vérifier le type de img array == uint8

# 3 - Test Resultat
# Vérifier inversion des valeurs [255, 128, 128, 0] ==>> [0, 127, 127, 255]
