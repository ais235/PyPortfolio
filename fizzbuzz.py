# fizz_buzz = 0
# fizz = 0
# buzz = 0
# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#         fizz_buzz += 1
#     elif i % 3 == 0:
#         print("Fizz")
#         fizz += 1
#     elif i % 5 == 0:
#         print("Buzz")
#         buzz += 1
#     else:
#         print(i)
#
# print("количество fizz_buzz: ", fizz_buzz)
# print("количество fizz: ", fizz)
# print("количество buzz: ", buzz)

for i in range(1, 101):
    out = ""
    if i % 3 == 0: out += "Fizz"
    if i % 5 == 0: out += "Buzz"
    print(out or i)
