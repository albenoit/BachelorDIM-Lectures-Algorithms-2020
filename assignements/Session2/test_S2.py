import Function as algo
import pytest

def test_answer():
    assert algo.onemore(3) == 4

def test_myaddition_intergers_1():
    assert algo.my_addition(10,2) == 12

def test_myaddition_intergers_2():
    assert algo.my_addition(-1,2) == 1

def test_myaddition_wrong_input():
    with pytest.raises(TypeError):
        algo.my_addition('a',2)

def test_average_above_zero():
    assert algo.average_above_zero([1 ,3 ,5 ,7 ,9 ,2 ,4 ,6 ,8 ]) == 5.625
# def test_average_above_zero2():
#     with pytest.raises(TypeError):
#         algo.average_above_zero(testTable2)

def test_max_value():
    assert algo.max_value([1 ,3 ,5 ,7 ,9 ,2 ,4 ,6 ,8 ]) == (9,4)

def test_reverse_table():
    assert algo.reverse_table([1 ,3 ,5 ,7 ,9 ,2 ,4 ,6 ,8 ]) == [8, 6, 4, 2, 9, 7, 5, 3, 1]

# def roi_bbox():
#     assert algo.roi_bbox(Xin) == [2 4 13 14]