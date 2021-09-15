def abs(num):
    if num >= 0:
        return num
    else:
        return -num

N = int(input())

max = -1e5 - 1
index_to_print = 1
for i in range(0, N):
    cur_token = abs(int(input()))
    if cur_token >= max:
        max = cur_token
        index_to_print = i + 1

print(index_to_print)