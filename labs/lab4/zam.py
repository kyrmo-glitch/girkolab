def make_calc(operation, initial=0):
    result = initial
    def calculator(num):
        nonlocal result
        if operation == '+':
            result = result + num
        elif operation == '-':
            result = result - num
        elif operation == '*':
            result = result * num
        elif operation == '/':
            result = result / num
        return result
    
    return calculator



calc = make_calc("*", initial=1)
print(calc(5))  # 5
print(calc(2))  # 10


calc_bad = make_calc("%", initial=10)
print(calc_bad(5))  
print(calc_bad(3))  