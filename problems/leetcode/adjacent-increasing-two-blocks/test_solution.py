from solution import max_adjacent_increasing

def test_sample():
    nums = [2,5,7,8,9,2,3,4,3,1]
    assert max_adjacent_increasing(nums) == 3

def test_user_case():
    nums = [4,3,2,1,1,2,3,4]
    assert max_adjacent_increasing(nums) == 2

def test_edges():
    assert max_adjacent_increasing([]) == 0
    assert max_adjacent_increasing([1]) == 0
    assert max_adjacent_increasing([2,2]) == 0

def test_more():
    assert max_adjacent_increasing([1,2,3,4,2,3,4,5]) == 4
    assert max_adjacent_increasing([1,3,2,4,5,1,2]) == 2
    assert max_adjacent_increasing([5,4,3,2,1,0]) == 0
