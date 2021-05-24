inicio = int(input())
fim = int(input())
cont = 1
primo = 0
while inicio <= fim:
    qtd = 0
    for c in range(cont,inicio+1):
        if inicio % c == 0:
            qtd+=1
    if qtd == 2:
        print(inicio)
        primo+=1
    inicio+= 1
print(f'primos: {primo}')