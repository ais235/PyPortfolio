Чёт/нечёт:
n = int(input())
print("even" if n % 2 == 0 else "odd")

Максимум из трёх:
a, b, c = map(int, input().split())
m = a
if b > m: m = b
if c > m: m = c
print(m)

Сумма 1..N с циклом:
N = int(input())
s = 0
for i in range(1, N+1):
    s += i
print(s)
