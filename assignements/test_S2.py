import Session1.S1_algotools as tFile
import pytest
import numpy as np

# Average above zero function
def test_average_above_zero_with_only_positive_numbers():
    assert tFile.average_above_zero([2, 3, 4]) == 3


def test_average_above_zero_with_positive_and_negative_numbers():
    assert tFile.average_above_zero([2, -3, 4, -8, 3]) == 3


def test_average_above_zero_with_only_negative_numbers():
    with pytest.raises(ValueError):
        tFile.average_above_zero([-2, -3, -4, -8, -3])


def test_average_above_zero_with_char_in_tab_error():
    with pytest.raises(Exception):
        tFile.average_above_zero(["azerty", -3, -4, -8, -3])


def test_average_above_zero_with_no_tab_error():
    with pytest.raises(Exception):
        tFile.average_above_zero("azerty")


def test_average_above_zero_with_empty_error():
    with pytest.raises(Exception):
        tFile.average_above_zero("")


# Max Values function
def test_max_value_with_only_positive_numbers():
    assert tFile.max_value([1, 10, 2, 8, 11]) == (4, 11)  # Only positive numbers


def test_max_value_with_only_negative_numbers():
    assert tFile.max_value([-1, -10, -2, -8, -11]) == (0, -1)  # Only negative numbers


def test_max_value_with_positive_and_negative_numbers():
    assert tFile.max_value([1, 10, 2, 8, -11]) == (
        1,
        10,
    )  # With positive and negative numbers


def test_max_value_with_char_in_tab_error():
    with pytest.raises(Exception):
        tFile.max_value(["azerty", -3, -4, -8, -3])


# Reverse table V1 function
def test_reserse_table_V1():
    assert tFile.reverse_table([1, 10, 2, 8, 11]) == [11, 8, 2, 10, 1]


def test_reserse_table_V2():
    assert tFile.reverse_table_V2([1, 10, 2, 8, 11]) == [11, 8, 2, 10, 1]


def test_reserse_table_V3():
    assert tFile.reverse_table_V3([1, 10, 2, 8, 11]) == [11, 8, 2, 10, 1]


# Bounding box
H = 12
W = 10
matrix = np.zeros((H, W))
for c in range(1, 3):
    for l in range(3, 5):
        matrix[l, c] = 1
for c in range(5, 8):
    for l in range(6, 9):
        matrix[l, c] = 1
bbox_real = np.array([3, 1, 8, 7])
bbox = tFile.roi_bbox(matrix)


def test_bounding_box_V1():
    assert np.prod(bbox_real == bbox)


bboxV2 = tFile.roi_bbox_V2(matrix)


def test_bounding_box_V2():
    assert np.prod(bbox_real == bboxV2)