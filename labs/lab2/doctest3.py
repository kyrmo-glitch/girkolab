def searchediv(n):
    """
    Ищет делители числа n (кроме 1 и самого числа).

    >>> searchediv(17)  
    set()
    
    >>> sorted(searchediv(6)) 
    [2, 3]
    
    >>> (searchediv(16))  
    {8, 2, 4}
    
    >>> sorted(searchediv(25)) 
    [5]
    

    >>> result = []
    >>> for i in range(174457, 174506):
    ...     d = sorted(searchediv(i))
    ...     if len(d) == 2:
    ...         result.append((i, d[0], d[1]))
    >>> result[0]  
    (174459, 3, 58153)
    """
    div = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
        if len(div) > 2:
            break
    return div

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    for i in range(174457, 174506):
        d= sorted(searchediv(i))
        if len(d) == 2:
            print(i,d[0], d[1])
