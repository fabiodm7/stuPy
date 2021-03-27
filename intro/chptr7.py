'''
Exercícios do capítulo 7 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Trabalhando com strings

# Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da
# primeira e imprima a posição de início
# 1a. AABBEFAATT
# 2a. BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT
primeira = input('Digite a primeira palavra: ').upper()
segunda = input('Digite a segunda palavra: ').upper()
if segunda in primeira:
    posicao = primeira.find(segunda)
    print('%s encontrado na posição %d de %s' % (segunda,posicao,primeira))
else:
    print('%s segunda não encontrado em %s' % (segunda,primeira))

# Escreva um programa que leia duas strings e gere uma terceira com os caracteres
# em comum. A ordem não é importante, mas deve conter todas as letras em comum
# 1a. AAACTBF
# 2a. CBT
# Resultado: CBT
primeira = list(input('Digite a primeira palavra: ').upper())
segunda = list(input('Digite a segunda palavra: ').upper())
comum = []
# if len(primeira) > len(segunda):
#     i = 0
#     while i < len(segunda):
#         if segunda[i] in primeira and segunda[i] not in comum:
#             comum.append(segunda[i])
#         i += 1
# else:
#     i = 0
#     while i < len(primeira):
#         if primeira[i] in segunda and primeira[i] not in comum:
#             comum.append(primeira[i])
#         i += 1
for p in primeira:
    if p in segunda and p not in comum:
        comum.append(p)
for s in segunda:
    if s in primeira and s not in comum:
        comum.append(s)
print(''.join(comum))

# Escreva um programa que leia duas strings e gere uma terceira apenas com os
# caracteres que aparecem em uma delas. A ordem não é importante
# 1a. CTA
# 2a. ABC
# Resultado: BT
primeira = list(input('Digite a primeira palavra: ').upper())
segunda = list(input('Digite a segunda palavra: ').upper())
incomum = []
i = 0
for p in primeira:
    if p not in segunda and p not in incomum:
        incomum.append(p)
for s in segunda:
    if s not in primeira and s not in incomum:
        incomum.append(s)
print(''.join(incomum))
'''
# Escreva um programa que leia uma string e imprima quantas vezes cada caractere
# aparece nessa string
string = list(input('Digite a primeira palavra: ').upper())
# for s in string:
#     print('%s: %dx' % (s,string.count(s)))
p = 0
while p > -1:
    p = string.find