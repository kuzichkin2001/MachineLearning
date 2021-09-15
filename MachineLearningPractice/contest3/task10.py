def isPrime(num):
    if num % 2 == 0:
        return num == 2
    current_del = 3
    while current_del * current_del <= num and num % current_del != 0:
        current_del += 2
    return current_del * current_del > num

num = int(input())

if isPrime(num):
    print('Yes')
else:
    print('No')