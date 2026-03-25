import math

def deliteli(number):
    count = 0
    for d in range(1, number + 1):
        if number % d == 0:
            count = count + 1
    return count

a = int(input())
def good_number(number):
    global a
    return deliteli(number) <= a

numbers = []

seed = 100

for _ in range(10):
    seed = (seed * 1231231 + 45613) % 10000
    num = seed % 50
    numbers.append(num)
    print(num)

good_numbers = list(filter(good_number, numbers))

print(f"Числа, у которых делителей <= {a}:")

for num in good_numbers:
    print(num)