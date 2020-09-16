import S1_algotools as algo
testTable=[1,3,5,7,9,2,4,6,8]

def test_average_above_zero():
    assert algo.average_above_zero(testTable) == 5.625