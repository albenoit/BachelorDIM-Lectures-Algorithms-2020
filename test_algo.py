import S1_algotools as algo 

tab=[1,2,3,4,5]

def test_max_value():
    assert algo.max_value(tab)==5

def test_average():
    assert algo.average(tab)==3