x = int(input())
qtd_divisores = 0
divisor = 1

while divisor <= x:
    if x % divisor == 0:
        qtd_divisores += 1
    divisor += 1

if qtd_divisores == 2:
    print(f'{x} eh primo')
else:
    print(f'{x} nao eh primo')