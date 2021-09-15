def max_plot(m1, v1, m2, v2):
    if (m1 / v1) > (m2 / v2):
        return 1
    elif (m1 / v1) < (m2 / v2):
        return 2
    else:
        return '='

v1 = int(input())
m1 = int(input())
v2 = int(input())
m2 = int(input())

print(max_plot(m1, v1, m2, v2))