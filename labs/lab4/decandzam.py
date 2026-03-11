def repeat(times):
    def decorator(func):
        def wrapper(*args,):
            results = []
            for i in range(times):
                result = func(*args)
                results.append(result)
            return results
        return wrapper
    return decorator

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
                return 'Ошибка'
            result = result / num
        return result
    return calculator

@repeat(times=3)
def calculate_with_repeat(operation, initial, value):
    calc = make_calc(operation, initial)
    return calc(value)

calc = make_calc("*", initial=1)
print(calc(5))  
print(calc(2))  

results = calculate_with_repeat("*", 1, 5)
print(results) 