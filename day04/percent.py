def hello(name):
    return f"Привет, {name}!"

print(hello("Alex"))

def is_even(n):
    return n % 2 == 0

print(is_even(9))

def percent(a, b):
    if b == 0:
        return None
    return (a / b) * 100

n = int(input("Основное число: "))
m = int(input("Процент от числа: "))

print(percent(n, m))