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
'''
fim = int(input('Digite o ultimo numero da serie: '))
'''
x = 1
while x <= fim:
    #print(x)
    #x += 2
    if x % 2 != 0:
        print(x)
    x += 1
'''
# Reescreva o programa anterior para escrever os 10 primeiros multiplos de 3
x = 1
cont = 0
while x <= fim:
    if x % 3 == 0 and cont < 10:
        print(x)
    x += 1
    cont += 1