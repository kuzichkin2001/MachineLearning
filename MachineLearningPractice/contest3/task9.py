A, B = map(int, input().split(' '))

when_b_reached = 1
when_million_reached = 1
current_day = 1
key = 0

cur_leafs_number = A
prev_leafs_number = A

while cur_leafs_number < 1e6:
    prev_leafs_number = cur_leafs_number
    cur_leafs_number = prev_leafs_number * 3

    current_day += 1

    if cur_leafs_number >= B and key == 0:
        when_b_reached = current_day
        key = 1

when_million_reached = current_day
print(str(when_b_reached) + ' ' + str(when_million_reached))