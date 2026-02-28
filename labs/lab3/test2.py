import pytest
from recursion2 import calculate_x1
from recursion2 import calculate_x2


def test_for_5():
    assert calculate_x1(5) == 0.26388888888888884
    assert calculate_x2(5) == 0.26388888888888884

def test_x1_value_4():
    assert calculate_x1(4) == pytest.approx(0.10416666666666667)
    assert calculate_x2(4) == pytest.approx(0.10416666666666667)

def test_x1_returns_float():
    assert isinstance(calculate_x1(3), float)
    assert isinstance(calculate_x2(3), float)