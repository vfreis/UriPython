x = int(input())
numero = 1
while numero <= x:
    if numero % 2 != 0:
        print(numero)
    numero += 1

# Versão 2 

def exibe_impares(limite):
    impar = 1
    while impar <= limite:
        print(impar)
        impar += 2

x = int(input())
exibe_impares(x)