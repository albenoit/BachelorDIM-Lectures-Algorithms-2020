import S1_algotools as algo

tab = [1,9,3,4,5,6,7,8,2]

def test_average():
    assert algo.average_above_zero(tab) == 5

def test_max_value():
    assert algo.max_value(tab) == 9

def test_get_index_max_value():
    assert algo.get_index_max_value(tab) == 2