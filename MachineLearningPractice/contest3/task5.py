n = int(input())

min = 1e4 + 1
min_count = 1

for i in range(0, n):
    current_token = int(input())
    if current_token < min:
        min = current_token
        min_count = 1
    elif current_token == min:
        min_count += 1

print(min_count)