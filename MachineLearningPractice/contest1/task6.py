def result(a, b, n):
    kopeek = a * n * 100 + b * n
    return (kopeek // 100, kopeek % 100)

a = int(input())
b = int(input())
n = int(input())

res = result(a, b, n)

print(str(res[0]) + ' ' + str(res[1]))