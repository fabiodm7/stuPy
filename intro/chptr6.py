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

# O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop()?
# O python retornará um erro "pop from empty list"
lista =[]
lista.pop()

# Simulação de uma fila de banco. O programa deve poder trabalhar com vários comandos digitados
# de uma só vez. Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a
# considerar a operação como uma string.
# Exemplo: FFFAAAS significaria três chagadas de novos clientes, três atendimentos e, finalmente,
# a saída do programa
ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print('\nExistem %d clientes na fila' % len(fila))
    print('Fila atual: ',fila)
    print('Digite "F" para adicionar um cliente ao fim da fila,')
    print('ou "A" para realizar o atendimento. "S" para sair.')
    # operacao = input('Operacao (F, A ou S): ').upper()
    operacao = input('Operacoes a realizar (F, A ou S): ').upper() # linha nova
    cliente = 0      
    while cliente < len(operacao) and operacao[cliente] != 'S': # linha nova
        # if operacao == 'A':
        if operacao[cliente] == 'A': # linha nova
            if len(fila) > 0 and cliente < len(operacao):
                atendido = fila.pop(0)
                print('Cliente %d atendido' % atendido)
                cliente += 1 # linha nova
            else:
                print('Fila vazia!')
                cliente += 1
        # elif operacao == 'F':
        elif operacao[cliente] == 'F': # linha nova
            ultimo += 1
            fila.append(ultimo)
            cliente += 1 # linha nova
        # elif operacao == 'S':    
            # break
        else:
            # print('Operacao inválida! Digite apenas F, A ou S.')
            print('Operacao inválida! Digite apenas F, A ou S, ou uma combinação delas.') # linha nova
            cliente += 1 # linha nova
    if operacao[cliente] == 'S': # linha nova
        break # linha nova

# Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho,
# considere o camando A para atendimento da fila 1 e B para atendimento da fila 2.
# O mesmo para a chegada de clientes: F para a fila 1 e G para a fila 2
ultimo1 = 0 # 10
ultimo2 = 0
fila1,fila2 = [],[] # list(range(1,ultimo+1))
while True:
    print('\nExistem %d clientes na fila 1 e %d na fila 2' % (len(fila1),len(fila2)))
    print('Fila 1 atual: ',fila1)
    print('Fila 2 atual: ',fila2)
    print('Digite "F" para adicionar um cliente ao fim da fila 1,')
    print('Digite "G" para adicionar um cliente ao fim da fila 2,')
    print('Digite "A" para realizar o atendimento na fila 1.')
    print('Digite "B" para realizar o atendimento na fila 2. Ou "S" para sair de ambas.')
    operacao = input('Operacoes a realizar (F, G, A, B ou S): ').upper()
    cliente = 0      
    while cliente < len(operacao) and operacao[cliente] != 'S':
        if operacao[cliente] == 'A':
            if len(fila1) > 0 and cliente < len(operacao):
                atendido = fila1.pop(0)
                print('Cliente %d atendido na fila 1' % atendido)
                cliente += 1
            else:
                print('Fila vazia!')
                cliente += 1
        elif operacao[cliente] == 'F':
            ultimo1 += 1
            fila1.append(ultimo1)
            cliente += 1
        elif operacao[cliente] == 'B':
            if len(fila2) > 0 and cliente < len(operacao):
                atendido = fila2.pop(0)
                print('Cliente %d atendido na fila 2' % atendido)
                cliente += 1
            else:
                print('Fila vazia!')
                cliente += 1
        elif operacao[cliente] == 'G':
            ultimo2 += 1
            fila2.append(ultimo2)
            cliente += 1
        else:
            print('Operacao inválida! Digite apenas F, G, A, B ou S, ou uma combinação delas.') # linha nova
            cliente += 1
    if cliente < len(operacao) and operacao[cliente] == 'S':
        break

# Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se
# os parênteses foram abertos e fechados na ordem correta.
# Exemplo:
# (()) OK
# ()()(()()) OK
# ()) ERRO
entrada = input('Digite uma sequência de (): ').upper()
lista = []
p = 0
while p < len(entrada):
    lista.append(entrada[p])
    p += 1
abrt,fech = [],[]
while len(lista) > 0:
    if lista[-1] == '(':
        abrt.append(lista.pop(-1))
    else:
        fech.append(lista.pop(-1))
if len(abrt) == len(fech):
    print('OK')
else:
    print('ERRO')

# Pesquisa senquencial. Modifique de modo a realizar a mesma tarefa, sem utilizar
# a variável achou. Observe a condição de saída do while:
l = [15,7,27,39]
p = int(input('Digite o valor a procurar: '))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        # achou = True
        print('%d achado na posição %d' % (p,x))
        break
    x += 1
# if achou:
    # print('%d achado na posição %d' % (p,x))
else:
    print('%d não encontrado' % p)

# Modifique o programa anterior para pesquisar dois valores. Em vez de apenas p,
# leia outro valor v que também será procurado. Na impressão, indique qual valor
# foi achado primeiro
l = [15,7,27,39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        # achou = True
        print('%d achado na posição %d antes de %d' % (p,x,v))
        break
    if l[x] == v:
        # achou = True
        print('%d achado na posição %d antes de %d' % (v,x,p))
        break
    x += 1
# if achou:
    # print('%d achado na posição %d' % (p,x))
else:
    print('Nenhum valor encontrado')

# Modifique o programa de forma a pesquisar p e v em toda a lista e informando a
# posição de p e v
l = [15,7,27,39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        print('%d achado na posição %d' % (p,x))
    x += 1
x = 0
while x < len(l):
    if l[x] == v:
        print('%d achado na posição %d' % (v,x))
    x += 1
'''
