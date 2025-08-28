# with open("notes.txt", "w", encoding="utf-8") as f:
#     f.write("Привет, файл!\n")
# # файл автоматически закрыт

# with open("out.txt", "w", encoding="utf-8") as f:
#     f.write("строка 1\n")
#     print("строка 2", file=f)  # тоже запись

# file: day06/files_basics.py
from pathlib import Path

p = Path("day06_data.txt")
with open(p, "w", encoding="utf-8") as f:
    f.write("Первая строка\nВторая строка\nТретья строка\n")

with open(p, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.rstrip()}")

