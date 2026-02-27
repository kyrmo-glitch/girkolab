from itertools import product

def countwords():
    """
    Подсчитывает количество 5-буквенных комбинаций из букв слова "ТИМОФЕЙ",
    удовлетворяющих условиям:
    >>> countwords() > 0
    True
    >>> countwords()
    10476
    
    Тесты для проверки логики подсчета:
    >>> letters = "ТИМОФЕЙ"
    >>> count = 0
    >>> for x in product(letters, repeat=5):
    ...     s = ''.join(x)
    ...     if (s.count('Й') <= 1 and s[0] != 'Й' and s[-1] != 'Й' 
    ...         and 'ИЙ' not in s and 'ЙИ' not in s):
    ...         count += 1
    >>> count == 10400
    False
    """
    letters = "ТИМОФЕЙ"
    count = 0
    for x in product(letters, repeat=5):
        s = ''.join(x)
        if (s.count('Й') <= 1 and s[0] != 'Й' and s[-1] != 'Й' and 'ИЙ' not in s and 'ЙИ' not in s):
            count += 1
    
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print(f"Результат: {countwords()}")