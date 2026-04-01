import math

def area(a, b):
    return a * b

def r_in(a, b):
    if a == b:
        return a / 2
    return 0

def r_out(a, b):
    return math.sqrt(a**2 + b**2) / 2