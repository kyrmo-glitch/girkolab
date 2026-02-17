value = 4**2020 + 2**2017 - 15

count = 0
n = value
while n > 0:
    if n % 2 == 1:   # если остаток от деления на 2 равен 1
        count += 1
    n //= 2          # целочисленно делим на 2

print(count)