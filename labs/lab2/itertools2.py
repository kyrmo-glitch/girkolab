def count_ones_in_binary():
    value = 4**2020 + 2**2017 - 15
    count = 0
    n = value
    while n > 0:
        if n % 2 == 1:  
            count += 1
        n //= 2          
    return count

result = count_ones_in_binary()
print(f"Количество единиц {result}")