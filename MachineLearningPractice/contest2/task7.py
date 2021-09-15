def is_in_area(args):
    x = float(args[0])
    y = float(args[1])

    if x >= 1 and x <= 4 and y >= 1 and y <= 5 and y <= -4 / 3 * x + 19 / 3:
        print('Yes')
    else:
        print('No')

args = input().split(' ')
is_in_area(args)