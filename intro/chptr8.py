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
'''