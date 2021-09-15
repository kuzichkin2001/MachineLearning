def find_second_max(args):
    first_max = -101
    second_max = -102
    for arg in args:
        if arg > first_max:
            second_max = first_max
            first_max = arg
        elif arg > second_max and arg < first_max:
            second_max = arg

    return second_max

N = int(input())
args = [int(x) for x in input.split(' ')]

print(find_second_max(args))