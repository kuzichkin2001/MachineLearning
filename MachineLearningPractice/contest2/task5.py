def is_working(N):
    if N % 3 == 0 and N % 10 != 3 or N % 3 != 0 and N % 10 == 3:
        return 1
    elif N % 3 == 0 and N % 10 == 3:
        return 0
    else:
        return 0

N = int(input())
print(is_working(N))