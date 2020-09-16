import S1_algotools as algo
testTable=[1,3,5,7,9,2,4,6,8]

def test_average_above_zero():
    assert algo.average_above_zero(testTable) == 5.625

def test_max_value():
    assert algo.max_value(testTable) == 9

def test_reverse_table():
    assert algo.reverse_table(testTable) == [8, 6, 4, 2, 9, 7, 5, 3, 1]