def countone():
    x = 4**2020 + 2**2017 - 15
    count = 0
    while x > 0:
        if x % 2 == 1:  
            count += 1
        x //= 2          
    return count

print(countone())
