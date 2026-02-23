def count_ones_in_binary():
    x = 4**2020 + 2**2017 - 15
    count = 0
    while x > 0:
        if x % 2 == 1:  
           count += 1
        x //= 2          
    return count
s = bin(4**2020 + 2**2017 - 15)
print(s.count('1'))
result = count_ones_in_binary()
print(f"Количество единиц {result}")