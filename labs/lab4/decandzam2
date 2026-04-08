def repeat(times):
    def decorator(func):
        def wrapper(*args):
            results = []
            for i in range(times):
                result = func(*args)
                results.append(result)
            return results
        return wrapper
    return decorator

def make_calc(operation, initial=0):
    result = initial
    
    @repeat(times=3)  
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
                print('Ошибка: деление на ноль')
                return result
            result = result / num
        return result
    
    return calculator

calc = make_calc("*", initial=1)

print(calc(5)) 
print(calc(2))  