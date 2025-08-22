a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Выберите операцию (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Неизвестная операция")
