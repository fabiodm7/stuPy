'''
Exercícios do capítulo 8 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Funções
'''
# Escreva uma função que retorne o maior de dois números
def max(a,b):
    if a > b:
        return a
    else:
        return b
print(max(9,8))

# Escreva uma função que retorne True se o primeiro número for múltiplo do segundo
def mult(a,b):
    if a % b == 0:
        return True
    else:
        return False
print(mult(9,2))

# Escreva uma função que receba um lado de um quadrado e retorne a área do quadrado
def areaQd(lado):
    return lado * lado
print(areaQd(9))

# Escreva uma função que receba a base e a altura de um triangulo e retorne a sua
# área: (base x altura) / 2
def areaTr(base,altura):
    return (base * altura) / 2
print(areaTr(5,8))

# Pesquisa em lista
# Reescreva de forma a utilizar métodos de pesquisa em lista 
# def pesquise(lista, valor):
    # for x,e in enumerate(lista):
    #     if e == valor:
    #         return x
    #     else:
    #         return None
def pesquise(texto, valor): # linha nova
    return texto.find(valor) # linha nova

# Como escrever uma função
# Reescreva utilizando for invés de while
def soma(lista):
    total = 0
    # x = 0
    # while x < len(lista):
    #     total += lista[x]
    #     x += 1
    for x in lista: # linha nova
        total += x # linha nova
    return total
l = [1,7,2,9,15]
print(soma(l))
print(soma([7,9,12,3,100,20,4]))

# Defina uma função recursiva que calcula o maior divisor comum entre dois números,
# onde a > b:
# mdc(a,b) = {a                  b = 0
#            {mdc(b,a-b|a/b|)    a > b
# Onde a-b|a/b| pode ser escrito em python como a % b 
def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b,(a%b))
print(mdc(15,10))

# Usando a função mdc, defina uma função para calcular o menor multiplo comum
# entre dois números:
# mmc(a,b) = {|a x b| / mdc(a,b)
# Onde |a x b| pode ser escrito em python como abs(a*b)
def mmc(a,b):
    return abs(a * b)/mdc(a,b)
print(mmc(15,10))

# Calculo fatorial
def fatorial(n):
    print('Calculando o fatorial de %d' % n)
    if n == 0 or n == 1:
        print('Fatorial de %d = 1' % n)
        return 1
    else:
        fat = n * fatorial(n-1)
        print('Fatorial de %d = %d' % (n, fat))
        return fat
print(fatorial(4))

# Sequencia de fibonacci com recursão
# fibonacci(n) = {n                              n <= 1
#                {fibonacci(n-1)+fibonacci(n-2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print('Recursivo: ',fibonacci(21))
# Sequencia de fibonacci sem recursão
def fibonacci2(n):
    anterior = 0
    proximo = 0
    i = 0
    while(i < n):
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1
        i += 1
    return proximo
print('Sem recursão: ',fibonacci2(21))

# Escreva uma funçao para validar uma variável string. Essa função recebe
# como parâmetro a string, o número mínimo e máxima de caracteres.
# Retorne verdadeiro se o tamanho da string estiver dentro do intervalo e falso se não
def string(s,minimo,maximo):
    if len(s) < minimo or len(s) > maximo:
        return False
    else:
        return True
print(string('Sua string aqui', 5, 10))

# Escreva uma função que receba uma string e um lista. A função deve comparar a string
# com os elementos da lista. Se a string for encontrada retorne verdadeiro, se não, falso
def emLista(s,l):
    return s in l
print(emLista('fabio',['fabio','duarte','medina']))
print(emLista('teste',['fabio','duarte','medina']))

# Adinhavando um número
import random
n = random.randint(1,10)
tentativas = 0
while tentativas < 3:
    x = int(input('Escolha um número entre 1 e 10: '))
    if x == n:
        print('Acertou!')
        break
    else:
        print('Errou')
        tentativas += 1
        if tentativas < 3:
            print('Tente outra vez...')
        else:
            print('Perdeu!')

# Altere o jogo da forca. Escolha a palavra a advinhar utilizando números aleatórios
import random # linha nova
lista_palavras = []
tamanho = int(input('Quantas palavras: ')) 
for i in range(tamanho):
    lista_palavras.append(input('Digite a palavra secreta: ').lower().strip())
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
# numero = int(input('Digite um númedo de 0 a {0}: '.format(tamanho-1)))
# indice = (numero * 776) % len(lista_palavras)
# palavra = lista_palavras[indice]
palavra = random.sample(lista_palavras,1)[0] # linha nova
while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        break
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já tentou essa letra.')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    print('X==:==\nX  :  ')
    print('X  0  ' if erros >= 1 else 'X')
    linha2 = ''
    if erros == 2:
        linha2 = '  |  '
    elif erros == 3:
        linha2 = ' \|  '
    elif erros >= 4:
        linha2 = ' \|/ '
    print('X%s' % linha2)
    linha3 = ''
    if erros == 5:
        linha3 += ' /   '
    elif erros >= 6:
        linha3 += ' / \ '
    print('X%s' % linha3)
    print('X\n===========')
    if erros == 6:
        print('Enforcado!')
        print('Resposta certa: {0}'.format(palavra))
        break

# Utilizando a função type, escreva uma função recursiva que imprima os elementos
# de uma lista. Cada elemento deve ser impresso separadamente, um por linha. Considere
# o caso de listas dentro de listas, como L = [1,[2,3,4,[5,6,7]]]. A cada nível
# imprima a lista mais à direita, como fazemos ao identar blocos em python.
# Dica: envie o nível atual como parêmetro e utilize-o para calcular a quantidade de
# espaços em branco à esquerda de cada elemento
def listaElementos(lista,nivel=0):
    for i in lista:
        if type(i) != list:
            espaco = ' '*nivel
            print(espaco,i)
        else:
            nivel = nivel+4
            listaElementos(i,nivel)
L = [1,[2,3,4,[5,6,7]]]
print(listaElementos(L))