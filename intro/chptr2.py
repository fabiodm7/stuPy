'''
Exercícios do capítulo 2 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Preparando o ambiente
'''
# converta as seguintes expressoes para que possam ser calculadas
print(10+20*30)
print(4**2+30)
print((9**4+2)*6-1)

# execute a expressão e tente calcula na mão
print(10%3*10**2+1-10*4/2)

# escreva seu nome
print("Fabio")

# escreva um programa que calcule 2a x 3b, onde a vale 3 e b vale
def equacao(a,b):
    return 2*a*3*b

print(equacao(3,5))

# crie um programa que some 3 variaveis
a = 2
b = 3
c = 4
print(a+b+c)

# aumento de salario
salario = 1500
aumento = 15
print(salario + salario * aumento / 100) # menos legível
print(salario + (salario * aumento / 100)) # mais legível