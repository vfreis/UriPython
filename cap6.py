def exibe_intervalo(x):
    if 0 <= x <= 25:
        print('Intervalo [0, 25]')
    elif 25 < x <= 50:
        print('Intervalo [25, 50]')
    elif 75 < x <= 100:
        print('Intervalo [75, 50]')
    else:
        print('Fora de Intervalo')

x = float(input('Digite Valor '))
exibe_intervalo(x)