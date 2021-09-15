k = int(input())
x = int(input())

mediana = x // k
if k % 2 == 0:
    m1 = mediana - k // 2 + 1
    m2 = mediana + k // 2
else:
    m1 = mediana - k // 2
    m2 = mediana + k // 2

print(str(m1) + ' ' + str(m2))