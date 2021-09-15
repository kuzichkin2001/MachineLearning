def abs(num):
    if num >= 0:
        return num
    else:
        return -num

def shortest_way(args):
    x1 = int(args[0])
    x2 = int(args[1])
    x3 = int(args[2])

    summary_way = 0

    if abs(x1 - x2) <= abs(x1 - x3):
        summary_way += abs(x1 - x2) + abs(x2 - x3)
    elif abs(x1 - x3) <= abs(x1 - x2):
        summary_way += abs(x1 - x3) + abs(x3 - x2)

    return summary_way

args = input().split(' ')
print(shortest_way(args))
