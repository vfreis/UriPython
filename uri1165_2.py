total = 0
real = 0
while True:
    vic = float(input())
    if vic < 0:
        break
    total += vic
    real += vic*2.50
print(f'VC$ {total:.2f}')
print(f'R$ {real:.2f}')