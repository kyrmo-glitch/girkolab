import pytest
from recursion import count1  
from recursion import count2

def test_empty_list():
    assert count1([]) == 0

def test_flat_list():
    assert count1([1, 2, 3]) == 3

def test_list_with_one_nested_list():
    assert count1(["x", "y", ["z"]]) == 4  

def test_deeply_nested_list():
    assert count1([1, 2, [3, 4, [5]]]) == 7  

def test_multiple_nested_lists():
    assert count1([1, [2, 3], [4, [5, 6]]]) == 9 

def test_empty_nested_list():
    assert count2([1, [], 2]) == 3  

def test_complex_nested_structure():
    assert count2([1, [2, [3, [4, [5]]]]]) == 9 

def test_mixed_types():
    assert count2([1, "st", [True, None], 3.14]) == 6  

def test_very_deep_nesting():
    deep_list = [1, [2, [3, [4, [5, [6]]]]]]
    assert count2(deep_list) == 11

def test_multiple_empty_lists():
    assert count2([[], [], []]) == 3  