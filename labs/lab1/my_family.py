my_family = ['папа', 'мама', 'я', 'сестра']

my_family_height = [
    ['папа', 180],
    ['мама', 165],
    ['я', 183],
    ['сестра', 170]
]

def get_father_height():
    return my_family_height[0][1]

def get_total_height():
    total = 0
    for member in my_family_height:
        total += member[1]
    return total
