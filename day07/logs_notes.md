Вывести все строки файла:

with open("sample.log", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


Фильтрация ошибок:

with open("sample.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print("Ошибка:", line.strip())


Подсчёт количества ошибок:

count = 0
with open("sample.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            count += 1
print("Количество ошибок:", count)