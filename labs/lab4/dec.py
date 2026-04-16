a = int(input())
def repeat(decorated_func):
    def wrapper(*args):
        global a
        results = []
        for i in range(a):  
            result = decorated_func(*args)
            results.append(result)
        return results
    return wrapper

@repeat
def say_hello(name):
    return f"Привет, {name}!"

decorated = repeat(say_hello)
result = decorated("anna")
print(result)

result = say_hello("Анна")
print(result)
