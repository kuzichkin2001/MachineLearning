x1, x2, x3 = map(int, input().split())

if x1 > x2 > x3 or x3 > x2 > x1:
    print(x2)
elif x2 > x1 > x3 or x3 > x1 > x2:
    print(x1)
elif x2 > x3 > x1 or x1 > x3 > x2:
    print(x3)