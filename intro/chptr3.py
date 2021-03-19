'''
Exercícios do capítulo 3 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Variáveis e entradas de dados
'''
# escreva o tipo de cada número da lista abaixo
print(5, type(5))
print(5.0, type(5.0))
print(4.3, type(4.3))
print(-2, type(-2))
print(100, type(100))
print(1.333, type(1.333))
print(1333, type(1333))

# true ou false se:
a = 4
b = 10
c = 5.0
d = 1
f = 5
print(f'a({a}) == c({c})', a == c)
print(f'a({a}) < b({b})', a < b)
print(f'd({d}) > b({b})', d > b)
print(f'c({c}) != f({f})', c != f)
print(f'a({a}) == b({b})', a == b)
print(f'c({c}) < d({d})', c < d)
print(f'b({b}) > a({a})', b > a)
print(f'c({c}) >= f({f})', c >= f)
print(f'f({f}) >= c({c})', f >= c)
print(f'c({c}) <= c({c})', c <= c)
print(f'c({c}) <= f({f})', c <= f)

# escreva a combinação de cada
a = True
b = False
c = True
print(a and a)
print(b and b)
print(not c)
print(not b)
print(not a)
print(a and b)
print(b and c)
print(a or c)
print(b or c)
print(a or b)
print(b or c)
print(c or a)
print(c or b)
print(c or c)
print(b or b)

# escreva um sistema que determina se alguem deve pagar imposto ou não
# considere que salários maiores de R$ 1.200,00 pagam imposto
salario1 = 900
salario2 = 1200
salario3 = 1500

def imposto(x):
    return x >= 1200

print(imposto(salario3))

# calcule o resultado da expressao A > B and C or D
caso1 = [1,2,True,False]
caso2 = [10,3,False,False]
caso3 = [5,1,True,True]

def teste(lista):
    x = lista[0] > lista[1]
    y = lista[2] or lista[3]
    return x and y
def teste2(lista):
    return lista[0] > lista[1] and lista[2] or lista[3]

print(teste(caso3))
print(teste2(caso3))

# faça um programa para avaliar a aprovação do aluno
# todas as médias devem ser maiores que 7
def aprovacao(notas):
    apr = []
    for n in notas:
        apr.append(n > 7)
    return not False in apr

n = [8,9,7.5,10]
print(aprovacao(n))

# faça um programa que peça dois números inteiros e imprima a soma dos dois números
def entradaNumero():
    return input('Digite um número: ')

def soma():
    print('Digite apenas numeros inteiros:')
    a = int(entradaNumero())
    b = int(entradaNumero())
    return a + b

print(soma())

# leia um valor em metros e converta para milimetros
def milimetros():
    print('Digite a metragem que deseja converter:')
    m = float(entradaNumero())
    return m * 100 * 10

print(milimetros())

# escreva um programa que leia a quantidade de dias, horas, minutos e segundos
# retorne o total em segundos
def segundos():
    print('Digite numeros inteiros:\nQuantos dias?')
    d = int(entradaNumero())
    print('Quantos horas?')
    h = int(entradaNumero())
    print('Quantos minutos?')
    m = int(entradaNumero())
    print('Quantos segundos?')
    s = int(entradaNumero())
    return d*86400+h*3600+m*60+s

print(segundos())

# faça um programa que calculo o salario atualizado, ele deve receber o salario atual e a % de aumento
def atlSalario():
    print('Insira o salario atual:')
    sal = float(entradaNumero())
    print('Insira a taxa de aumento:')
    tx = 1 + float(entradaNumero())/100
    return sal*tx

print(atlSalario())

# faça um programa que solicite o preco de uma mercadoria e o percentual de desconto
# imprima o valor do desconto e o preco a pagar
def precoDesc():
    print('Qual o valor do produto?')
    bruto = float(entradaNumero())
    print('Qual o % de desconto?')
    desc = float(entradaNumero())/100
    descVl = bruto * desc 
    return [descVl , bruto - descVl]
item = precoDesc()

print(f'o desconto foi de R$ {item[0]}')
print(f'o valor a pagar é R$ {item[1]}')

# calcule o tempo de uma viagem de carro, pergunte a distancia e a velocidade esperada
def viagem():
    print('qual a distancia em KM')
    dist = float(entradaNumero())
    print('qual a velocidade média esperada em KM/H')
    vlc = float(entradaNumero())
    return dist/vlc

print(f'o tempo estimado de viagem é de {viagem()} horas')

# converta ºC em ºF, a fórmula é:
# F = 9 x C + 32
#    -------
#       5
def fahrenheit(c):
    f = (9*c/5)+32
    return f

print('Insira uma temperatura em ºC')
celsius = float(entradaNumero())
print(f'A temperatura de {celsius}ºC é igual a {fahrenheit(celsius)}ºF')

# Escreva um programa que pergunte a quantidade de km percorridos 
# por um carro alugado pelo usuário, assim como a quantidade de dias
# pelos quais o casso foi alugado calcule o preco a pagar, sabendo
# que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
def aluguel(dist,dias):
    return dist * 0.15 + dias * 60
print('Insira a distancia percorrida em KM')
percorrido = float(entradaNumero())
print('Insira os dias alugados')
d = int(entradaNumero())
print(f'o valor a pagar é R$ {aluguel(percorrido,d)}')

# escreva um programa para calcula a reducao do tempo de vida de um fumante
# pergunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou
# considere que um fumante perde 10 min de vida a cada cigarro
# calcule quantos dias de vida um fumante perdera. Exiba o total em dias
def vidaFumante(cigarros,anos):
    return cigarros * 10/(24*60) * 365 * anos

print('Quantos cigarros fuma por dia?')
c = int(entradaNumero())
print('A quanto tempo?')
t = int(entradaNumero())
print(f'Você já perdeu {vidaFumante(c,t)} dias da sua vida!')