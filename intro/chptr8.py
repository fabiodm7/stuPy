'''
Exercícios do capítulo 8 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Funções

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
'''
