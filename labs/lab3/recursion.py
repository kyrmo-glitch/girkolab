def count(lst):
    total = 0
    for item in lst:
        total +=1
        if isinstance(item, list):
            total += count(item)
    return total

print(count([]))
print(count([1, 2, 3]))
print(count(["x", "y", ["z"]]))
print(count([1, 2, [3, 4, [5]]]))  