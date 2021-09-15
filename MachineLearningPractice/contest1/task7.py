import math

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

R = a * b * c / (4 * S)
print(f'{R:.4f}')