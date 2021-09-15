def visokos(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    else:
        return 28

year = int(input())
print(visokos(year))