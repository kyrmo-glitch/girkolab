def count1(lst):
    total = 0
    for item in lst:
        total +=1
        if isinstance(item, list):
            total += count1(item)
    return total

print(count1([]))
print(count1([1, 2, 3]))
print(count1(["x", "y", ["z"]]))
print(count1([1, 2, [3, 4, [5]]]))



print('-------------------------------')


def count2(lst):
    process = [lst]  
    count = 0
    
    while process:
        current = process[0]
        process = process[1:] 
        
        for item in current:
            if isinstance(item, list):
                process.append(item)  
                count += 1
            else:
                count += 1
    
    return count

# Проверка
print(count2([]))                    
print(count2([1, 2, 3]))             
print(count2(["x", "y", ["z"]]))    
print(count2([1, 2, [3, 4, [5]]]))

