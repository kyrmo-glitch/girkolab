def repeat_decorator(times):
    """
    Декоратор, который запускает функцию указанное число раз
    
    Args:
        times: количество запусков функции
    
    Returns:
        Декорированная функция, возвращающая список результатов
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


# Исходное замыкание-калькулятор
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


# Применяем декоратор к замыканию
@repeat_decorator(times=3)
def run_calculator(calc_func, value):
    """Функция для запуска калькулятора с одним значением"""
    return calc_func(value)


# Создаем калькулятор
calc = make_calc("*", initial=1)

# Запускаем декорированную функцию
results = run_calculator(calc, 2)
print(f"Результаты 3 запусков с value=2: {results}")  # [2, 4, 8]

# Другой пример с разными значениями
@repeat_decorator(times=5)
def run_calc_with_values(calc_func, *values):
    """Запускает калькулятор с разными значениями последовательно"""
    results = []
    for value in values:
        results.append(calc_func(value))
    return results


calc_add = make_calc("+", initial=10)
results = run_calc_with_values(calc_add, 1, 2, 3, 4, 5)
print(f"Результаты последовательных вычислений: {results}")  # [11, 13, 16, 20, 25]


# Более гибкий вариант с сохранением состояния калькулятора между запусками
print("\n--- Тест с сохранением состояния ---")
calc_mul = make_calc("*", initial=1)

@repeat_decorator(times=4)
def multiply_step(value):
    """Функция, использующая замыкание calc_mul"""
    return calc_mul(value)

# Каждый запуск использует предыдущий результат
results = multiply_step(2)
print(f"Последовательное умножение на 2: {results}")  # [2, 4, 8, 16]

# Еще один пример
results = multiply_step(3)
print(f"Продолжаем умножать на 3: {results}")  # [48, 144, 432, 1296]