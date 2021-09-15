def max_triplet_sum(args):
    max = -301
    for i in range(0, len(args) - 2):
        if args[i] + args[i+1] + args[i+2] > max:
            max = args[i] + args[i+1] + args[i+2]

    return max

N = int(input())
args = [int(x) for x in input().split(' ')]

print(max_triplet_sum(args))