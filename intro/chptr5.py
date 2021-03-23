'''
Exercícios do capítulo 5 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Repetições
'''
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

# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total de ganho com juros no período
x = float(input('Depósito inicial de: '))
tx = float(input('Taxa de juros: '))/100
t = int(input('Anos de investimento: '))*12
t0 = 1
while t0 <= t:
    x *= (1+tx)
    t0 += 1
print('Você acumulou %.2f.' % x)

# Altere o programa de forma a perguntar o valor a ser depositado mensalmente. Esse valor
# será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros
# do mês seguinte
x = float(input('Depósito inicial de: '))
tx = float(input('Taxa mensal de juro: '))/100
t = int(input('Anos de investimento: '))*12
y = float(input('O aporte mensal será de: '))
t0 = 1
while t0 <= t:
    x *= (1+tx)
    x += y
    t0 += 1
print('Você acumulou %.2f.' % x)

# Escreva um programa que pergunte o valor inicial de uma dívida e juro mensal. Pergunte
# também o valor mensal que será pago. Imprima o número de meses para que a dívida seja
# paga, o total pago e o total de juros.
divida = float(input('Dívida adquirida: '))
tx = float(input('Taxa mensal de juro: '))/100
aporte = float(input('O aporte mensal será de: '))
correcao = divida
tempo = 0
pago = 0
while correcao > 0:
    correcao *= (1+tx)
    correcao -= aporte
    pago += aporte
    tempo += 1
juros = pago-divida
print(f'Você levará {tempo} meses para pagar um total de R$ {pago}.')
print(f'Sendo R$ {juros} de juros.')

# Escreva um programa que leia numeros inteiros do teclado. O programa deve ler os números
# até que o usuário digite 0. No final do programa imprima a quantidade de números, a soma
# e a média aritmética
contagem = 0
soma = 0
media = 0
while True:
    entrada = int(input('Digite um número de 1 a 9.\nDigite 0 (zero) para encerrar: '))
    if entrada == 0:
        break
    contagem += 1
    soma += entrada
media = soma / contagem
print(f'Você executou {contagem} cliques, sem contar o ZERO.\nResultou em uma soma de {soma} e uma média de {media}')

# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar
# ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela para
# obter o preço. Seu programa deve exibir o total de compras depois que o usuário digitar
# 0 (zero). Qualquer outro código deve gerar a mensagem de codigo inválido:
# +--------------+
# |Codigo |Preço |
# |-------|------|
# |   1   | 0,50 |
# |-------|------|
# |   2   | 1,00 |
# |-------|------|
# |   3   | 4,00 |
# |-------|------|
# |   5   | 7,00 |
# |-------|------|
# |   9   | 8,00 |
# +-------+------+
itens,total = 0,0
while True:
    produto = int(input('Digite o código do produto comprado: '))
    if produto == 0:
        break
    elif produto not in [1,2,3,5,9]:
        print('Digite um produto válido')
    itens += 1
    if produto == 1:
        total += 0.5
    elif produto == 2:
        total += 1
    elif produto == 3:
        total += 4
    elif produto == 5:
        total += 7
    elif produto == 9:
        total += 8
print(f'Total de itens: {itens}\nTotal a pagar: R$ {total}')

# Contagem de cédulas. Execute o programa para os seguintes valores: 501, 745, 384, 2, 7 e 1
valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 50
pagar = valor
while True:
    if atual <= pagar:
        pagar -= atual
        cedulas += 1
    else:
        print('%d cédula(s) de R$ %d' % (cedulas,atual))
        if pagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

# o que acontece se digitar 0 no valor a pagar?
# executa a primeira contagem de cédulas de R$ 50
# e imprime a primeira linha "0 cédula(s) de R$ 50"

# Modifique o programa para que aceite notas de R$ 100
valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
pagar = valor
while True:
    if atual <= pagar:
        pagar -= atual
        cedulas += 1
    else:
        print('%d cédula(s) de R$ %d' % (cedulas,atual))
        if pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

# Modifique o programa para que aceite valores decimais, ou seja, conte moedas de 0.01
# 0.05, 0.10, 0.25 e 0.50
valor = float(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
pagar = valor
while True:
    if atual <= pagar:
        pagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print('%d cédula(s) de R$ %d' % (cedulas,atual))
        else:
            print('%d moeda(s) de R$ %.2f' % (cedulas,atual))
        if pagar <= 0.001:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0

# O que acontece se digitarmos 0.001 no programa anterior? Caso ele não funcione, altere-o
# de forma a corrigir o problema
# Já corrigido no programa anterior

# Reescreva o programa anterior de forma a continuar executando até que o usuario digite 0.
# Utilize repetições aninhadas
valor = 1
while valor > 0:
    valor = float(input('Digite o valor a pagar: '))
    cedulas = 0
    atual = 100
    pagar = valor
    while True:
        if atual <= pagar:
            pagar -= atual
            cedulas += 1
        else:
            if atual >= 1:
                print('%d cédula(s) de R$ %d' % (cedulas,atual))
            else:
                print('%d moeda(s) de R$ %.2f' % (cedulas,atual))
            if pagar <= 0.001:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.5
            elif atual == 0.5:
                atual = 0.25
            elif atual == 0.25:
                atual = 0.1
            elif atual == 0.1:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.01
            cedulas = 0

# Escreva um programa que exiba uma lista de opçẽs (menu): adição, subtração, divisão,
# multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção
# saída seja escolhida:
opcao = ''
while opcao != 's':
    opcao = str(input('O que você deseja fazer agora:\n"+" para soma\n"-" para subtração\n"x" para multiplicação\n"%" para divisão\n"s" para sair\nDigite uma opção: ')).lower()
    tabuada = 1
    if opcao == 's':
        break
    elif opcao == '+':
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print('%d + %d = %d' % (tabuada,numero,tabuada + numero))
                numero += 1
            tabuada += 1
    elif opcao == '-':
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print('%d - %d = %d' % (tabuada,numero,tabuada - numero))
                numero += 1
            tabuada += 1
    elif opcao == 'x':
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print('%d x %d = %d' % (tabuada,numero,tabuada * numero))
                numero += 1
            tabuada += 1
    elif opcao == '%':
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print('%d / %d = %.2f' % (tabuada,numero,tabuada / numero))
                numero += 1
            tabuada += 1
    else:
        print('Insira uma opção válida')
        opcao = ''

# Escreva um programa que leia um numero e verifique se é ou não um número primo
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois
# por todos os números ímpares até o número lido. Se o resto de alguma dessas divisões
# for igual a zero, o número não é primo. Observe que 0 e 1 não são primo e que 2 é
# o único número primo que é par
numero = 2
while numero not in [0,1]:
    numero = int(input('Digite um numero inteiro: '))
    resto = False
    if numero % 2 != 0:
        impar = 3
        while impar < numero:
            if numero % impar == 0:
                resto = True
                impar += 2
            else:
                impar += 2
    else:
        resto = True
    if resto == False or numero == 2:
        print('Número é primo')
    else:
        print('Número não é primo')

# Modifique o programa anterior de forma a ler um número N e imprimir os primeiros números primos
def numeroPrimo(numero):
    resto = False
    if numero % 2 != 0:
        impar = 3
        while impar < numero:
            if numero % impar == 0:
                resto = True
                impar += 2
            else:
                impar += 2
    else:
        resto = True
    if resto == False or numero == 2:
        #return True
        print(numero)
    #else:
        #return False
        

entrada = int(input('Digite um numero inteiro: '))

while entrada not in [0,1]:
    n0 = 2
    while n0 <= entrada:
        numeroPrimo(n0)
        n0 += 1
    entrada = int(input('Digite um numero inteiro: '))

# Escreva um prorama que calcule a raiz quadrada de um numero. Utilize o método de Newton para
# obter o resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2.
# Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça
# b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o 
# quadrado de p for menor que 0.0001
def raizQuadrada(n):
    b = 2
    p2 = 0
    p = 0
    while abs(n - p2) >= 0.0001:
        p = (b + (n / b)) / 2
        p2 = p ** 2
        b = p
    return p
entrada = float(input('Digite um número: '))
print('A raiz quadrada de %.2f é %.3f' % (entrada,raizQuadrada(entrada)))

# Escreva um programa que calcule o resto da divisão inteira entre dois números.
# Utilize apenas as operações de soma e subtração para calcular o resultado.
divisor = float(input('Insira o divisor: '))
dividendo = float(input('Insira o dividendo: '))
resto = dividendo
if divisor > dividendo:
    count = 1
    while count < 10:
        resto += dividendo
        count += 1
while resto >= divisor:
    resto -= divisor
print(resto)

# Escreva uma função que verifica se um número é palindromo. Um número é palindromo
# se continua o mesmo quando seus digitos são invertidos. Exemplo: 454, 10501
def palindromo(txt):
    if txt == txt[::-1]:
        return True
    else:
        return False
entrada = input('Digite um número: ')
if palindromo(entrada):
    print('É palindromo')
else:
    print('Não é palindromo')