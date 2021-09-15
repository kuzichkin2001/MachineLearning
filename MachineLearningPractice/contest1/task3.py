def digitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def digitMul(num):
    mul = 1
    while num > 0:
        mul *= num % 10
        num = num // 10
    return mul


N = int(input())

print(digitSum(N))
print(digitMul(N))