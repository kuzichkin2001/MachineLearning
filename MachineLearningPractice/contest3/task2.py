mul_res = 1

current_mul = 1
while current_mul >= 0:
    mul_res *= current_mul
    current_mul = float(input())

print(f'{mul_res:.6f}')