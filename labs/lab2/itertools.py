from itertools import product

def count_codes():
    letters = "ТИМОФЕЙ"
    count = 0
    for x in product(letters, repeat=5):
        s = ''.join(x)
        if (s.count('Й') <= 1 and s[0] != 'Й' and s[-1] != 'Й' and 'ИЙ' not in s and 'ЙИ' not in s):
            count += 1
    
    return count


print(count_codes())
