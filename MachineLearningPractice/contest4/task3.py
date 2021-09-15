N = int(input())

min = max = None
key = 0
sum = 0
for i in range(0, N):
    current_token = int(input())
    sum += current_token

    if key == 0:
        min = max = current_token
        key = 1
    if current_token < min:
        min = current_token
    if current_token > max:
        max = current_token

print((sum - min - max) / (N - 2))