def beg(args):
    v1 = int(args[0])
    v2 = int(args[1])
    v3 = int(args[2])
    s = int(args[3])

    distance = 0
    if s <= 300 * v1:
        return s / v1
    elif s <= 300 * v1 + 600 * v2:
        s -= 300 * v1
        return 300 + s / v2
    else:
        s -= 300 * v1 + 600 * v2
        return 900 + s / v3

args = input().split(' ')
print(f'{beg(args):.6f}')