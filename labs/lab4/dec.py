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

@repeat(times=3)
def say_hello(name):
    return f"Привет, {name}!"

result = say_hello("Анна")
print(result)
