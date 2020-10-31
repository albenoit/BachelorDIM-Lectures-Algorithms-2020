import myCodeSamples as tobetested
import pytest


#print('10+2=12 ?',tobetested.my_addition(10,2))
def test_myaddition_integers_1():
    assert tobetested.my_addition(10,2) == 12


def test_myaddition_integers_2():
    assert tobetested.my_addition(-1,2) == 1
    
def test_myaddition_wrong_input():
    with pytest.raises(TypeError):
        tobetested.my_addition('a',2)