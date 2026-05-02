def area(a, b, h):
    return (a + b) * h / 2

def r_in(a, b, h):
    c = (h**2 + ((a - b)/2)**2)**0.5
    if a + b == 2 * c:  # прямое сравнение (может не сработать из-за float)
        return h / 2
    return None

def r_out(a, b, h):
    c = (h**2 + ((a - b)/2)**2)**0.5
    R = (c / (2 * h)) * ((a * b + c**2)**0.5)
    return R
