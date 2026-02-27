def calculate_x_recursive(i):
    if i == 1:
        return 1
    if i == 2:
        return -1/8
    
    return ((i-1) * calculate_x_recursive(i-1)) / 3 + ((i-2) * calculate_x_recursive(i-2)) / 4
print(f"x1 = {calculate_x_recursive(1)}")
print(f"x2 = {calculate_x_recursive(2)}")
print(f"x3 = {calculate_x_recursive(3)}")
print(f"x4 = {calculate_x_recursive(4)}")
print(f"x5 = {calculate_x_recursive(5)}")



def calculate_x(i):
    if i == 1:
        return 1
    if i == 2:
        return -1/8
    
    x_prev1 = 1        # x1
    x_prev2 = -1/8     # x2
    
    for n in range(3, i + 1):
        x_current = ((n-1) * x_prev2) / 3 + ((n-2) * x_prev1) / 4
        x_prev1, x_prev2 = x_prev2, x_current
    
    return x_prev1


print(f"x1 = {calculate_x(1)}")
print(f"x2 = {calculate_x(2)}")
print(f"x3 = {calculate_x(3)}")
print(f"x4 = {calculate_x(4)}")
print(f"x5 = {calculate_x(5)}")
