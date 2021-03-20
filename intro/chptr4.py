'''
Exercícios do capítulo 4 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Condições
'''
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

# carro novo ou velho, dependendo da idade
idade = int(input('A quanto tempo tem o veículo, em anos? '))
def novoVelho(idade_veiculo):
    if idade_veiculo <= 3:
        return 'carro novo'
    else:
        return 'carro velho'
print(novoVelho(idade))

# escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km.
# calcule o preco da passagem, cobrando R$ 0,5 por km para viagens de até de 200 km,
# e R$ 0,45 para viagens mais longas
d = float(input('Qual a distância da viagem em km?'))
def passagem(distancia):
    if distancia <= 200:
        return distancia * 0.5
    else:
        return distancia * 0.45
print(passagem(d))

# categoria x preco
categoria = int(input('Digite a categoria do produto: '))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print('Categoria invalida, digite um valor de 1 a 5!')
                    preco = 0
print('O preco do produto é: R$ %6.2f' % preco)

# escreva um programa que leia dois numeros e que pergunte qual a operação voce deseja realizar.
# Você deve poder calcular a soma, subtração, multiplicação e divisão.
# Exiba o resultado da operação solicitada
l=[0,0]
l[0] = float(input('Qual o valor do primeiro elemento da operação: '))
l[1] = float(input('Qual o valor do segundo elemento da operação: '))
o = str(input('Qual operação deseja realizar:\na - soma\nb - subtração\nc - multiplicação\nd - divisão\nDigite aqui: '))
if o == 'a':
    print(f'A operação escolhida foi a SOMA e seu resultado é {l[0]+l[1]}')
elif o == 'b':
    print(f'A operação escolhida foi a SUBTRAÇÃO e seu resultado é {l[0]-l[1]}')
elif o == 'c':
    print(f'A operação escolhida foi a MULTIPLICAÇÃO e seu resultado é {l[0]*l[1]}')
elif o == 'd':
    print(f'A operação escolhida foi a DIVISÃO e seu resultado é {l[0]/l[1]}')
else:
    print('Por favor, insira uma operacao valida')

# Escreva um programa para aprovar um emprestimo bancario para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salario e a quantidade de anos a pagar.
# O valor mensal não pode ser superior a 30% do salario
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar
i = float(input('O valor do imóvel em R$: '))
s = float(input('O salario do comprador em R$: '))
t = float(input('Anos de financiamento: '))

def financiamento(valorImovel, salario, tempo):
    prestacao = valorImovel/(12*tempo)
    if prestacao <= salario*0.3:
        return 'APROVADO'
    else:
        return 'REPROVADO'

print(f'O seu financiamento foi {financiamento(i,s,t)}.')

# Escreva um programa que calcule o preço a pagar pelo forneciemnto de energia eletrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residencias, I para industris e C para comercios.
# Calcule o preço a pagar de acordo com a tabela a seguir:
# +---------------------------------+
# |PREÇO POR TIPO E FAIXA DE CONSUMO|
# +---------------------------------+
# |Tipo       |Faixa(kWh)   |Preço  |
# +---------------------------------+
# |Residencial|Até 500      |R$ 0,40|
# |           |Acima de 500 |R$ 0,65|
# +---------------------------------+
# |Comercial  |Até 1000     |R$ 0,55|
# |           |Acima de 1000|R$ 0,60|
# +---------------------------------+
# |Industrial |Até 5000     |R$ 0,55|
# |           |Acima de 5000|R$ 0,60|
# +---------------------------------+
c = float(input('Informe o valor de energia consumida em kWh: '))
t = str(input('Informe o tipo de instalçaõ de consumo (R,C ou I): '))
def energia(consumo,tipoInstalacao):
    if tipoInstalacao == 'R':
        if consumo > 500:
            return consumo * 0.65
        elif consumo <= 500:
            return consumo * 0.4
        else:
            return 'Informe um valor de consumo válido, maior ou igual a zero!'
    elif tipoInstalacao == 'C':
        if consumo > 1000:
            return consumo * 0.6
        elif consumo <= 1000:
            return consumo * 0.55
        else:
            return 'Informe um valor de consumo válido, maior ou igual a zero!'
    elif tipoInstalacao == 'I':
        if consumo > 5000:
            return consumo * 0.6
        elif consumo <= 5000:
            return consumo * 0.55
        else:
            return 'Informe um valor de consumo válido, maior ou igual a zero!'
    else:
        return 'Informe um tipo de instalação válido:\nResidencial -> R\nComercial -> C\nIndustrial -> I!'
print(energia(c,t))