import S1_algotools as tobetested
import pytest

list = [8, 15, 14, 12, 6, 18, 10, 2, 20]

def test_myaddition_integers_1():
    assert tobetested.my_addition(10,2) == 12

def test_myaddition_integers_2():
    assert tobetested.my_addition(-1,2) == 1

def test_myaddition_wrong_input():
    with pytest.raises(TypeError):
        tobetested.my_addition('a',2)

def test_average_above_zero_divisionByZero():
    assert tobetested.average_above_zero(list) == 12.125
