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


print('-------------------------------')


def count_elements(lst):
    process = [lst]  # список списков для обработки
    count = 0
    
    while process:
        # Берем первый элемент (не последний, как в стеке)
        current = process[0]
        process = process[1:]  # удаляем первый элемент
        
        for item in current:
            if isinstance(item, list):
                process.append(item)  # добавляем в конец
                count += 1
            else:
                count += 1
    
    return count

# Проверка
print(count_elements([]))                    # 0
print(count_elements([1, 2, 3]))             # 3
print(count_elements(["x", "y", ["z"]]))     # 4
print(count_elements([1, 2, [3, 4, [5]]]))   # 7