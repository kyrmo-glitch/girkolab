import math

def area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def r_in(a, b, c):
    s = area(a, b, c)
    p = (a + b + c) / 2
    return s / p

def r_out(a, b, c):
    s = area(a, b, c)
    return (a * b * c) / (4 * s)