num = int(input())

res = ''
for i in range(0, num + 1):
    for j in range(0, i):
        res += str(i) + ' '

print(res)