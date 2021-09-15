N = int(input())

capacity = 0
for i in range(0, N):
    capacity += int(input())

M = int(input())

if capacity <= M:
    print(True)
else:
    print(False)
