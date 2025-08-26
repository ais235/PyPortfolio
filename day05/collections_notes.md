🔹 Списки (list)

Упорядоченные коллекции, изменяемые.

nums = [1, 2, 3]
nums.append(4)         # [1, 2, 3, 4]
nums[0]                # 1
nums[-1]               # последний элемент
len(nums)              # длина

🔹 Словари (dict)

Хранение по ключу: ключ → значение.

person = {"name": "Alex", "age": 25}
print(person["name"])          # Alex
person["phone"] = "123-45-67"  # добавление

🔹 Множества (set)

Хранение уникальных элементов, без порядка.

fruits = {"apple", "banana", "apple"}
print(fruits)  # {"apple", "banana"}
fruits.add("pear")

Операции с множествами

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # объединение {1,2,3,4,5}
print(a & b)   # пересечение {3}
print(a - b)   # разность {1,2}

# Список квадратов чисел 1..5

squares = [i**2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Словарь переводов

eng_ru = {"cat": "кот", "dog": "собака"}
print(eng_ru["cat"])  # кот

# Подсчёт уникальных чисел

nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)
print(len(unique))  # 5