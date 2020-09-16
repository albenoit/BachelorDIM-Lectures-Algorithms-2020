import S1_algotools as S1
import pytest

nbr_list = [1, -5, 3]

def test_average_above_zero():
    assert S1.average_above_zero(nbr_list) == 2.0

def test_max_value():
    assert S1.max_value(nbr_list) == 2

def test_reverse_table():
    assert S1.reverse_table(nbr_list) == [3, -5, 1]

def test_erreur():
    with pytest.raises(TypeError):
        S1.average_above_zero('a', 2)