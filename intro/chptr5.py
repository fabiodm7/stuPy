'''
Exercícios do capítulo 5 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Repetições

# exiba números de 1 a 100
x = 1
while x <= 100:
    print(x)
    x += 1

# exiba números de 50 a 100
x = 1
while x <= 100:
    if x >= 50:
        print(x)
    x += 1

# Faça um programa para escrever a contagem regressiva do lançamento de um foguete
# O programa deve imprimir "10,9,...1,0 e Fogo!" na tela.
x = 10
while x != 0:
    print(x)
    x -= 1
print('Fogo!')

# imprima numeros de 1 até o número digitado pelo usuário, mas apenas números ímpares
fim = int(input('Digite o ultimo numero da serie: '))
x = 1
while x <= fim:
    #print(x)
    #x += 2
    if x % 2 != 0:
        print(x)
    x += 1

# Reescreva o programa anterior para escrever os 10 primeiros multiplos de 3
x = 1
cont = 0
while x <= fim:
    if x % 3 == 0 and cont < 10:
        print(x)
    x += 1
    cont += 1

# ecreva um programa que imprima as linhsa de uma tabuada
n = int(input('Tabuada do: '))
x = 0
while x <= 10:
    print(f'{n} x {x} =', n*x)
    x += 1

# modifique o programa de modo que o usuário digite o início e o fim da tabuada
n = int(input('Tabuada do: '))
x = int(input('A partir de: '))
y = int(input('Até: '))
while x <= y:
    print(f'{n} x {x} =', n*x)
    x += 1

# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do
# primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular
# o resultado. Lembre-se que podemos entender a multiplicação de dois números como somas
# sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 ou 4 + 4 + 4 + 4 + 4
n = int(input('Deseja multiplicar: '))
x = int(input('Por: '))
y = 1
aux = 0
while y <= x:
    aux += n
    y += 1
print(f'{n} x {x} = {aux}.')

# Escreve um programa que leia dois números. Imprima a divisão inteira do primeiro pelo
# segundo, assim como o resto da divisão. Utilize apenas operadores de soma e subtração
# para chegar ao resultado. Lembre-se de que podemos entender o quociente da divisão de
# de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20/4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
a = int(input('Deseja dividir: '))
b = int(input('Por: '))
def divisao(n,x):
    y = 1
    z = 1
    aux = n
    if b == 0:
        print('Não pode dividir por 0.')
    else:
        while aux > x:
            aux -= x
            if aux >= x:
                y += 1
        if aux < x and aux > 0:
            aux = aux + aux + aux + aux + aux + aux + aux + aux + aux + aux
            while aux > 0:
                aux -= x
                if aux >= x:
                    z += 1
        else:
            z = 0
        print(f'{a} / {b} = {y}.{z}')
divisao(a,b)

# contagem de questões corretas. o programa deve aceitar respostas com
# letras maiúsculas e minúsculas
pontos = 0
questao = 1
while questao <= 3:
    resposta = input('Resposta da questao %d: ' % questao).lower()
    if questao == 1 and resposta == 'b':
        pontos += 1
    if questao == 2 and resposta == 'a':
        pontos += 1
    if questao == 3 and resposta == 'd':
        pontos += 1
    questao += 1
print('O aluno fez %d ponto(s).' % pontos)
'''
# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total de ganho com juros no período
x = float(input('Depósito inicial de: '))
tx = float(input('Taxa de juros: '))/100
t = int(input('Anos de investimento: '))
t0 = 1
while t0 <= t:
    x *= (1+tx)
    t0 += 1
print('Você acumulou %.2f.' % x)