n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n > m:
    print(min(x, y, m - x, n - y))
elif n < m:
    print(min(x, y, n - x, m - y))