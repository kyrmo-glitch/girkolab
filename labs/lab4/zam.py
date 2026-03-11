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
            if num == 0:
                print('Ошибка')
                return result
            result = result / num
        return result
    return calculator

calc = make_calc("*", initial=1)
print(calc(5))  
print(calc(2))  

calc_bad = make_calc("/", initial=10)
print(calc_bad(5))  
print(calc_bad(0))  