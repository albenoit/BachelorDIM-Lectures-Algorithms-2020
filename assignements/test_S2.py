import S1_algotools as tobetested
import pytest

def test_myaddition_integers():
    assert tobetested.my_addition(10, 2) == 12

def test_myaddition_intergers_2():
    assert tobetested.my_addition(-1, 2) == 1

def test_myaddition_wrong_input():
    with pytest.raises(TypeError):
        tobetested.my_addition('a', 4)


def test_average_above_zero():
    assert tobetested.average_above_zero([1, 3, 2]) == 2

def test_average_above_zero_noPositiveValues():
    with pytest.raises(ValueError):
        tobetested.average_above_zero([-1, -3, -2])


def test_max_value():
    assert tobetested.max_value([25, 67, 42, 69]) == 69

def test_max_value_wrong_input():
    with pytest.raises(TypeError):
        tobetested.max_value('a', 65, 125)

