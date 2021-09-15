def sum_of_power_two_indices(args):
    current_del = 1
    sum = 0
    for i in range(0, len(args)):
        if (i + 1) % current_del == 0:
            sum += args[i]
            current_del *= 2

    return sum

N = int(input())

args = []
for i in range(0, N):
    args.append(int(input()))

print(sum_of_power_two_indices(args))