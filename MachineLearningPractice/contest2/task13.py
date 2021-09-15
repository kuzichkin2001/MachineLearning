k = int(input())

if 10 < k % 100 < 20:
    print(f'Мне {k} лет')
elif k % 10 == 1:
    print(f'Мне {k} год')
elif k % 10 >= 5 or k % 10 == 0:
    print(f'Мне {k} лет')
elif k % 10 < 5:
    print(f'Мне {k} года')