import pytest
from generator import my_random_generator
def test_generator_returns_ints():
    gen = my_random_generator(1, 100)
    for _ in range(10):
        num = next(gen)
        assert isinstance(num, int)

def test_generator_range():
    min_val, max_val = 1, 100
    gen = my_random_generator(min_val, max_val)
    
    for _ in range(100):
        num = next(gen)
        assert min_val <= num <= max_val

def test_generator_range_custom():
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

def test_generator_different_sequences():
    min_val, max_val = 1, 100
    
    gen1 = my_random_generator(min_val, max_val)
    gen2 = my_random_generator(min_val, max_val)
    
    sequence1 = [next(gen1) for _ in range(50)]
    sequence2 = [next(gen2) for _ in range(50)]
    
    assert sequence1 != sequence2
