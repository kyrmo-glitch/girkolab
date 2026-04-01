import pytest
from generator import my_random_generator
def test_generator_returns_ints():
    """Проверка, что генератор возвращает целые числа"""
    gen = my_random_generator(1, 100)
    for _ in range(10):
        num = next(gen)
        assert isinstance(num, int)

def test_generator_range():
    """Проверка, что числа попадают в заданный диапазон"""
    min_val, max_val = 1, 100
    gen = my_random_generator(min_val, max_val)
    
    for _ in range(100):
        num = next(gen)
        assert min_val <= num <= max_val

def test_generator_range_custom():
    """Проверка с произвольным диапазоном"""
    test_cases = [
        (5, 10),
        (1, 50),
        (20, 30),
        (0, 100),
        (-10, 10),
        (1, 1)
    ]
    
    for min_val, max_val in test_cases:
        gen = my_random_generator(min_val, max_val)
        for _ in range(50):
            num = next(gen)
            assert min_val <= num <= max_val 
        
