'''
Exercícios do capítulo 4 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Condições

# o que acontece se o primeiro e segundo valor forem iguais?
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('O primeiro é maior que o segundo')
if b > a:
    print('O segundo é maior que o primeiro')
# nada acontece se os valores forem iguais, pois tem condição que prevê esse caso

# escreva um programa que pergunte a velocidade do carro do usuário.
# caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# nesse caso exiba o valor da multa, sendo R$ 5,00 a cada km/h acima de 80
def multa(velocidade):
    if velocidade > 80:
        print('Usuário multado em R$ ', (velocidade - 80)*5)
v = float(input('Velocidade atual em km/h: '))
multa(v)

# escreva um programa que leia tres numeros e imprima o maior e o menor
def maiorMenor(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n1 and n3 > n2:
        maior = n3
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    elif n3 < n1 and n3 < n2:
        menor = n3
    print(f'Maior: {maior}; Menor: {menor}')

a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))
maiorMenor(a,b,c)

# escreva um programa que pergunte o salario que retorne o aumento
# aumento de 15% para salario menores ou iguais a R$ 1250,00, se não 10%
def aumentoSal(salario):
    if salario > 1250:
        return salario * 1.1
    else:
        return salario * 1.15

s = float(input('Salario atual: '))
print(f'A salario ajustado é R$ {aumentoSal(s)}')
'''
# carro novo ou velho, dependendo da idade
# idade = int(input('A quanto tempo tem o veículo, em anos? '))
# def novoVelho(idade_veiculo):
#    return 'carro velho'
# print(novoVelho(idade))