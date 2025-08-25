# # file: day03/table.py
n = 10
#
# # шапка
# print("    ", end="")
# for j in range(1, n+1):
#     print(f"{j:4}", end="")
# print()
# print("    " + "-" * (4 * n))
#
# # тело
# for i in range(1, n+1):
#     print(f"{i:3}|", end="")
#     for j in range(1, n+1):
#         print(f"{i*j:4}", end="")
#     print()

# Школьная таблица умножения
for i in range(1, n+1):
     for j in range(1, n + 1):
         print(f"{j:3} * " + f"{i:2} =" + f"{i*j:3}|", end="")
     print()