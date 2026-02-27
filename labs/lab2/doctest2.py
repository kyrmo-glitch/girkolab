def countone():
    """
    Вычисляет количество единиц в двоичной записи числа 4**2020 + 2**2017 - 15.

    >>> countone() > 0  
    True
    
    >>> countone() == 2019
    False
    
    >>> x = 4**2020 + 2**2017 - 15
    >>> bin(x).count('1') == countone()
    True
    
    >>> # Проверка, что результат не меняется
    >>> countone() == countone()
    True
    """
    x = 4**2020 + 2**2017 - 15
    count = 0
    while x > 0:
        if x % 2 == 1:
           count += 1
        x //= 2
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print(f"Результат: {countone()}")