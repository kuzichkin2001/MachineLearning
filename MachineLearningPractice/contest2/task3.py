def is_triangle_possible(args):
    a = int(args[0])
    b = int(args[1])
    c = int(args[2])
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
    else:
        return -1

args = input().split(' ')
print(f'{is_triangle_possible(args):.6f}')
