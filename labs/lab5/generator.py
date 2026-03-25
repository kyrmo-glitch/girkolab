def my_random_generator(min, max):
    seed = 12345
    while True:
        seed = (seed * 1103515245 + 12345) % 8345345
        random_num = min + (seed % (max - min + 1))
        yield random_num

def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

random_gen = my_random_generator(1, 100)

n=int(input())
def check_divisors(num):
    global n
    return count_divisors(num) <= n

filtered_numbers = filter(check_divisors, random_gen)

print('-' * 30)

for i in range(5):
    num = next(filtered_numbers)
    deliteli = count_divisors(num)
    print(f"{num} {deliteli}")
