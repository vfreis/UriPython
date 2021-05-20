dia_compra = input()
dia_espera = int(input())
dia_entrega = dia_compra

for i in range(0, dia_espera):
    if dia_entrega == 'domingo':
        dia_entrega = 'segunda'
    elif dia_entrega == 'segunda':
        dia_entrega = 'terca'
    elif dia_entrega == 'terca':
        dia_entrega = 'quarta'
    elif dia_entrega == 'quarta':
        dia_entrega = 'quinta'
    elif dia_entrega == 'quinta':
        dia_entrega = 'sexta'
    elif dia_entrega == 'sexta':
        dia_entrega = 'sabado'
    else:
        dia_entrega = 'domingo'

if dia_compra != dia_entrega:
    print(f'sera entregue {dia_entrega}')
else:
    print('chega hoje!')