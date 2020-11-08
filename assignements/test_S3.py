import S3_imgproc_tools as tFile
import pytest
import numpy as np


# 1 - chargement image non définie
# If imgArray is none
# raise value("Img not found")
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


# 2 - chargement image non array
# Vérifier le type de img array == uint8

# 3 - Test Resultat
# Vérifier inversion des valeurs [255, 128, 128, 0] ==>> [0, 127, 127, 255]
