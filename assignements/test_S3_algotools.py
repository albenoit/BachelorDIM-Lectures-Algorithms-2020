# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:13:01 2020

@author: cuvellin
"""

import pytest
import S3_imgproc_tools as imgproc
import numpy as np


def test_invert_colors_manual():
    img = np.zeros((1, 1, 3), np.uint8)
    assert (imgproc.invert_colors_manual(img) == np.full((1, 1), 255)).all()


def test_invert_colors_manual_not_uint8():
    with pytest.raises(TypeError):
        imgproc.invert_colors_manual(1)


def test_invert_colors_numpy():
    img = np.zeros((1, 1, 3), np.uint8)
    assert (imgproc.invert_colors_numpy(img) == np.full((1, 1), 255)).all()


def test_invert_colors_opencv():
    img = np.zeros((1, 1, 3), np.uint8)
    assert (imgproc.invert_colors_opencv(img) == np.full((1, 1), 255)).all()


def test_invert_colors_numpy_none():
    with pytest.raises(TypeError):
        imgproc.invert_colors_numpy(None)


def test_invert_colors_numpy_not_an_array():
    with pytest.raises(TypeError):
        imgproc.invert_colors_numpy(1)


def test_invert_colors_numpy_not_an_uint8():
    with pytest.raises(TypeError):
        imgproc.invert_colors_numpy(np.zeros((2, 2), dtype=np.float32))


def test_threshold():
    img = np.array([[[129, 0, 254]]], dtype=np.uint8)
    assert (imgproc.threshold(img) == np.array([[[True, False,  True]]])).all()


def test_threshold_not_an_uint8():
    with pytest.raises(TypeError):
        imgproc.threshold(np.zeros((2, 2), dtype=np.float32))
