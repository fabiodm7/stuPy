'''
Exercícios do capítulo 7 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Trabalhando com strings
'''
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
for p in primeira:
    if p not in segunda and p not in incomum:
        incomum.append(p)
for s in segunda:
    if s not in primeira and s not in incomum:
        incomum.append(s)
print(''.join(incomum))

# Escreva um programa que leia uma string e imprima quantas vezes cada caractere
# aparece nessa string
string = list(input('Digite a primeira palavra: ').upper())
# for s in string:
#     print('%s: %dx' % (s,string.count(s)))
p = 0
lista = []
while p < len(string):
    if string[p] not in lista:
        lista.append(string[p])
        print(f'{string[p]}: {string.count(string[p])}x')
    p += 1

# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres
# da segunda foram retirados da primeira
# 1a. AATTGGAA
# 2a. TG
# Resultado: AAAA
primeira = list(input('Digite a primeira palavra: ').upper())
segunda = list(input('Digite a segunda palavra: ').upper())
incomum = []
for p in primeira:
    if p not in segunda:
        incomum.append(p)
print(''.join(incomum))

# Escreva um programa que leia três strings. Imprima o resultado da substituição
# da primeira, dos caracteres da segunda, pelos da terceira
# 1a. AATTGGAA
# 2a. TG
# 3a. AC
# Resultado: AAAACCAA
primeira = list(input('Digite a primeira palavra: ').upper())
segunda = list(input('Digite a segunda palavra: ').upper())
terceira = list(input('Digite a segunda palavra: ').upper())
quarta = []
for p in primeira:
    for s in segunda:
        if p == s:
            for t in terceira:
                if segunda.index(s) == terceira.index(t):
                    p = t
    quarta.append(p)
print(''.join(quarta))

# Jogo da forca.
# 1. Modifique o programa de forma a escrever a palavra secreta caso o jogador perca
# 2. Modifique o jogo de forma a utilizar uma lista de palavras. No início, pergunte um número
# e calcule o índice da palavra a utilizar pela fórmula: 
# indice = (numero * 776) % len(lista_palavras) 
# 3. Modifique o programa para utilizar listas de strings para desenhar o boneco da forca. Você
# pode utilizar uma lista para cada linha e orzanizá-la em uma lista de listas. Em vez de
# controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento desenhar
# Exemplo:
# >>> linha = list('X------')
# >>> linha
# ['x','-','-','-','-','-','-']
# >>> linha[6] = '|'
# >>> linha
# ['x','-','-','-','-','-','|']
# >>> ''.join(linha)
# 'x-----|' 
lista_palavras = [] # linha nova
# palavra = input('Digite a palavra secreta: ').lower().strip()
tamanho = int(input('Quantas palavras: ')) # linha nova 
for i in range(tamanho): # linha nova
    lista_palavras.append(input('Digite a palavra secreta: ').lower().strip()) # linha nova
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
numero = int(input('Digite um númedo de 0 a {0}: '.format(tamanho-1))) # linha nova
indice = (numero * 776) % len(lista_palavras) # linha nova
palavra = lista_palavras[indice] # linha nova
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
        print('Resposta certa: {0}'.format(palavra)) # linha nova
        break

# Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar
# e alternar entre os jogadores. A cada jogada, verifique se a posição está livre.
# Verifique também quando um jogador venceu a partida. Um jogo da velha pode ser visto como
# uma lista de 3 elementos, onde cada elemento é outra lista, também com três elementos
# Cada posição pode ser vista como um número. Por exemplo:
#  x | o |    ->  7 | 8 | 9 
# ---+---+---    ---+---+---
#    | x | x  ->  4 | 5 | 6 
# ---+---+---    ---+---+---
#    |   | o  ->  1 | 2 | 3 
dic = {
    "1":'',"2":'',"3":'',
    "4":'',"5":'',"6":'',
    "7":'',"8":'',"9":''
}
print('POSIÇÕES:     TABULEIRO:')
print(' 7 | 8 | 9 -> {0:^3}|{1:^3}|{2:^3}\n---+---+---   ---+---+---'.format(dic["7"],dic["8"],dic["9"]))
print(' 4 | 5 | 6 -> {0:^3}|{1:^3}|{2:^3}\n---+---+---   ---+---+---'.format(dic["4"],dic["5"],dic["6"]))
print(' 1 | 2 | 3 -> {0:^3}|{1:^3}|{2:^3}'.format(dic["1"],dic["2"],dic["3"]))
while True:
    while True:
        player1 = input('Jogador 1, qual posição deseja jogar? ')
        if dic[player1] is not '':
            print('Posição ocupada, tente outra!')
            continue
        dic[player1] = 'x'
        break
    print('POSIÇÕES:     TABULEIRO:')
    print(' 7 | 8 | 9 -> {0:^3}|{1:^3}|{2:^3}\n---+---+---   ---+---+---'.format(dic["7"],dic["8"],dic["9"]))
    print(' 4 | 5 | 6 -> {0:^3}|{1:^3}|{2:^3}\n---+---+---   ---+---+---'.format(dic["4"],dic["5"],dic["6"]))
    print(' 1 | 2 | 3 -> {0:^3}|{1:^3}|{2:^3}'.format(dic["1"],dic["2"],dic["3"]))
    velha = [
        [dic["1"] , dic["2"] , dic["3"]],
        [dic["4"] , dic["5"] , dic["6"]],
        [dic["7"] , dic["8"] , dic["9"]]
    ]
    if velha[0] == ['x','x','x'] or velha[1] == ['x','x','x'] or velha[2] == ['x','x','x']:
        print('Jogador 1 venceu!')
        break
    elif (velha[0][0] == 'x' and velha[1][0] == 'x' and velha[2][0] == 'x') or (velha[0][1] == 'x' and velha[1][1] == 'x' and velha[2][1] == 'x') or (velha[0][2] == 'x' and velha[1][2] == 'x' and velha[2][2] == 'x'):
        print('Jogador 1 venceu!')
        break
    elif (velha[0][0] == 'x' and velha[1][1] == 'x' and velha[2][2] == 'x') or (velha[0][2] == 'x' and velha[1][1] == 'x' and velha[2][0] == 'x'):
        print('Jogador 1 venceu!')
        break
    elif '' not in velha and '' not in velha[1] and '' not in velha[2]:
        print('Velha!')
        break
    while True:
        player2 = input('Jogador 2, qual posição deseja jogar? ')
        if dic[player2] is not '':
            print('Posição ocupada, tente outra!')
            continue
        dic[player2] = 'o'
        break
    print('POSIÇÕES:     TABULEIRO:')
    print(' 7 | 8 | 9 -> {0:^3}|{1:^3}|{2:^3}\n---+---+---   ---+---+---'.format(dic["7"],dic["8"],dic["9"]))
    print(' 4 | 5 | 6 -> {0:^3}|{1:^3}|{2:^3}\n---+---+---   ---+---+---'.format(dic["4"],dic["5"],dic["6"]))
    print(' 1 | 2 | 3 -> {0:^3}|{1:^3}|{2:^3}'.format(dic["1"],dic["2"],dic["3"]))
    velha = [
        [dic["1"] , dic["2"] , dic["3"]],
        [dic["4"] , dic["5"] , dic["6"]],
        [dic["7"] , dic["8"] , dic["9"]]
    ]
    if velha[0] == ['o','o','o'] or velha[1] == ['o','o','o'] or velha[2] == ['o','o','o']:
        print('Jogador 2 venceu!')
        break
    elif (velha[0][0] == 'x' and velha[1][0] == 'x' and velha[2][0]== 'x') or (velha[0][1] == 'x' and velha[1][1] == 'x' and velha[2][1] == 'x') or (velha[0][2] == 'x' and velha[1][2] == 'x' and velha[2][2] == 'x'):
        print('Jogador 2 venceu!')
        break
    elif (velha[0][0] == 'x' and velha[1][1] == 'x' and velha[2][2] == 'x') or (velha[0][2] == 'x' and velha[1][1] == 'x' and velha[2][0] == 'x'):
        print('Jogador 2 venceu!')
        break
    elif '' not in velha[0] and '' not in velha[1] and '' not in velha[2]:
        print('Velha!')
        break