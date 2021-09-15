a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a ** 2 + b ** 2) ** 0.5 <= d:
    print('Yes')
elif (a ** 2 + c ** 2) ** 0.5 <= d:
    print('Yes')
elif (b ** 2 + c ** 2) ** 0.5 <= d:
    print('Yes')
else:
    print('No')