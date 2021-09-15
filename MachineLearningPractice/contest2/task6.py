def is_in_area(args):
    x = float(args[0])
    y = float(args[1])

    if x < 2:
        if y <= 1.5 and y >= 0.5:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')

args = input().split(' ')
is_in_area(args)