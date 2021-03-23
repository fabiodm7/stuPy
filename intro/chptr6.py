'''
Exercícios do capítulo 6 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Listas

# Cálculo de média com notas digitadas
notas = []
soma = 0
x = 0
while x <= len(notas):
    notas.append(float(input('Nota %d: ' % x)))
    if notas[x] >= 0:
        soma += notas[x]
        x += 1
    else:
        break
x = 0
while x < len(notas[:len(notas)-1]):
    print('Nota %d: %6.2f' % (x,notas[x]))
    x += 1
print('Média: %5.2f' % (soma/x))

# Faça um programa que leia duas listas e gere uma terceira com os elementos das duas primeiras
lst1, lst2 = [],[]
idx = 0
while 'pare' not in lst1:
    lst1.append(input('Insira um valor para a primeira lista, "pare" para encerrar essa lista: '))
idx = 0
while 'pare' not in lst2:
    lst2.append(input('Insira um valor para a segunda lista, "pare" para encerrar essa lista: '))
lst3 = lst1[:-1]+lst2[:-1]
print(lst3)

# Faça um program que percorra duas listas e gere uma terceira sem elementos repetidos
lst1, lst2 = [],[]
idx = 0
while 'pare' not in lst1:
    lst1.append(input('Insira um valor para a primeira lista, "pare" para encerrar essa lista: '))
idx = 0
while 'pare' not in lst2:
    lst2.append(input('Insira um valor para a segunda lista, "pare" para encerrar essa lista: '))
idx = 0
lst3 = lst1[:]
while idx < len(lst2):
    if lst2[idx] not in lst3:
        lst3.append(lst2[idx])
    idx += 1
print(lst3)
'''
