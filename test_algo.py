import S1_algotools as algo 

tab_positive=[1,2,3,4,5]
tab_negative=[-1,-2,-3,-4,-5]
boolean_matrix=np.zeros((12,10),dtype=bool)
for c in range (7,9):
    for l in range (4,9):
        boolean_matrix[l,c]=1


def test_average_1():
    assert algo.average(tab_positive)==3

def test_average_2():
    assert algo.average(tab_negative)=='no positive value found'

def test_max_value():
    assert algo.max_value(tab_positive)==5

def test_reverse_table():
    assert algo.reverse_table(tab_positive) == [5,4,3,2,1]


