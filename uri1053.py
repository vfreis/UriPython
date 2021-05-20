def media(n1, n2, n3, n4):
    return ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

m = media(n1, n2, n3, n4)

if m >= 7.0:
    print(f'Media: {m:.1f}')
    print('Aluno aprovado.')
elif m < 5.0:
    print(f'Media: {m:.1f}')
    print('Aluno reprovado.')
else:
    print(f'Media: {m:.1f}')
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    nota = (m + n5) / 2
    if nota >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {nota:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {nota:.1f}')