def count(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += count(item)
        else:
            total += 1
    return total
print(count([1, 2, [3, 4, [5]]]))  