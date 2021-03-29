'''
Exercícios do capítulo 9 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Arquivos

# TEORIA: Abrindo, escrevendo e fechando um arquivo
arquivo = open('numeros.txt','w')
for linha in range(1,51):
    arquivo.write('%d\n' % linha)
arquivo.close()

# TEORIA: Abrindo, lendo e fechando um arquivo
arquivo = open('numeros.txt','r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# TEORIA: Impressão dos parâmetros passados na linha de comando
# Experimente chamar o script na linha de comando usando os seguintes parâmetros:
# nomeArquivo.py primeiro segundo terceiro 
# nomeArquivo.py 1 2 3
# nomeArquivo.py readme.txt 5
# nomeArquivo.py 'nome grande' 'segundo nome grande'
import sys
print('Número de parâmetros %d' % len(sys.argv))
for n,p in enumerate(sys.argv):
    print('Parametro %d: %s' % (n,p))

# Escreva um programa que receba o nome de um arquivo pela linha de comando e que
# imprima todas as linhas desse arquivo
import sys
arquivo = open(sys.argv[1],'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# Modifique o programa para que receba mais dois parâmetros: a linha de início e de 
# fim da impressão. O programa deve imprimir apenas as linhas entre esses dois valores
# (incluindo as linhas de início e fim)
import sys
arquivo = open(sys.argv[1],'r')
inicio = int(sys.argv[2])
fim = int(sys.argv[3])
l = 0
for linha in arquivo.readlines():
    if l >= inicio-1 and l < fim:
        print(linha)
    l += 1
print('Inicio: %d\nFim: %d' %(inicio,fim))
arquivo.close()

# TEORIA: Gravação de números pares e ímpares em arquivos diferentes
impares = open('impares.txt','w')
pares = open('pares.txt','w')
for n in range(1,1001):
    if n % 2 == 0:
        pares.write('%d\n' % n)
    else:
        impares.write('%d\n' % n)
impares.close()
pares.close()

# Filtragem exclusiva dos multiplos de 4
multi4 = open('multiplos4.txt','w')
pares = open('pares.txt','r')
for l in pares.readlines():
    if int(l) % 4 == 0:
        multi4.write(l)
pares.close()
multi4.close()

# Crie um programa que leia os arquivos pares.txt e impares.txt e que crie um só 
# arquivo paresimpares.txt com todas as linhas dos dois arquivos, preservando a
# ordem numerica
pares = open('pares.txt','r')
impares = open('impares.txt','r')
paresimpares = open('paresImpares.txt','w')
imp = []
par = []
for i in impares.readlines():
    imp.append(int(i))
for p in pares.readlines():
    par.append(int(p))
parimp = imp + par
parimp.sort()
for x in parimp:
    paresimpares.write(str(x)+'\n')
pares.close()
impares.close()
paresimpares.close()

# Crie um programa que receba o nome de dois arquivos a partir da linha de comando
# e gere um terceiro arquivo com as linhas dos dois arquivos
import sys
arquivo1 = open(sys.argv[1],'r')
arquivo2 = open(sys.argv[2],'r')
arquivo3 = open(sys.argv[3],'w')
for a1 in arquivo1.readlines():
    arquivo3.write(a1)
for a2 in arquivo2.readlines():
    arquivo3.write(a2)
arquivo1.close()
arquivo2.close()
arquivo3.close()

# Crie um programa que inverta a ordem do arquivo pares. A primeira linha deve
# conter o maior número e a última o menor
pares = open('pares.txt','r')
# paresReverso = open('paresReversos.txt','w')
par = []
for p in pares.readlines():
    par.append(int(p))
par.sort(reverse=True)
pares.close()
pares = open('pares.txt','w')
for p in par:
    # paresReverso.write(str(p)+'\n')
    pares.write(str(p)+'\n')
pares.close()
# paresReverso.close()

# TEORIA: Processamento de um arquivo
largura = 100
entrada = open('entrada.txt','r')
for linha in entrada.readlines():
    if linha.startswith(';'):
        continue
    elif linha.startswith('>'):
        print(linha[1:].rjust(largura))
    elif linha.startswith('*'):
        print(linha[1:].center(largura))
    else:
        print(linha)
entrada.close()

# Modifique o programa para imprimir 40x o símbolo "*" se este for o primeiro
# caractere da linha. Adicione também a opção para parar de imprimir até que se
# pressione a tecla Enter cada vez que a linha inicia com "."
largura = 100
entrada = open('entrada.txt','r')
for linha in entrada.readlines():
    if linha.startswith(';'):
        continue
    elif linha.startswith('>'):
        print(linha[1:].rjust(largura))
    elif linha.startswith('*'):
        print(linha[1:].center(largura))
        print('*'*40)
    elif linha.startswith('.'):
        input('Pressione Enter para continuar:')
    else:
        print(linha)
entrada.close()

# Crie um programa que leia um arquivo texto e gere um arquivo de saída paginado.
# Cada linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60
# linhas. Adicione na última linha de cada página o número da página atual e o
# nome do arquivo
# Modifique o programa anterior para também receber o número de caracteres por linha
# e o número de páginas por folha pela linha de comando
import sys
arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]
largura = int(sys.argv[3]) # 76
comprimento = int(sys.argv[4]) # 60
pagina = 1
posicao = 0
entrada = open(arquivo1,'r')
saida = open(arquivo2,'w')
nome = saida.name
saidaComp = 0
for linha in entrada.readlines():
    if len(linha) <= largura:
        saida.write(linha)
        posicao += 1
        saidaComp += 1
    else:
        qbr = 0
        inicio = 0
        while qbr < len(linha)/largura:
            saida.write(linha[inicio:largura+inicio-1])
            qbr += 1
            inicio += largura-1
            saidaComp += 1
            if qbr <= len(linha)/largura:
                saida.write('\n')
        posicao += qbr
    resto = posicao % (comprimento-1)
    if posicao % (comprimento-1) == 0:
        saida.write('---------- Arquivo {0}, Página {1} ----------\n'.format(nome,pagina))
        pagina += 1
        posicao = 0
        saidaComp += 1
entrada.close()
saida.close()

# Crie um programa que receba uma lista de nomes de arquivos e imprima um por um
entrada = input('Insira os arquivos que deseja imprimir, separados por vírgula: ')
arquivos = entrada.split(',')
for a in arquivos:
    arq = open(a,'r')
    print('Imprimindo o arquivo: %s' % a)
    for linha in arq:
        print(linha)
    arq.close()

# Crie um programa que receba uma lista de nomes de arquivos e gere um unico arquivo
# com o conteúdo de todos eles
entrada = input('Insira os arquivos que deseja imprimir, separados por vírgula: ')
arquivos = entrada.split(',')
saida = open('saida.txt','w')
for a in arquivos:
    arq = open(a,'r')
    print('Imprimindo o arquivo: %s' % a)
    for linha in arq.readlines():
        saida.write(linha)
    entrada.close()
saida.close()

# Crie um programa que leia um arquivo e crie um dicionário onde cada chave é uma
# palavra e cada valor é o número de ocorrências no arquivo
entrada = open('entrada.txt','r')
dic = {}
lista = []
for linha in entrada.readlines():
    for l in linha.split(' '):
        lista.append(l)
for i in lista:
    dic[i] = lista.count(i)
print(dic)
entrada.close()
'''
# Modifique o programa anterior para também registrar a linha e a coluna de cada
# ocorrência da palavra no arquivo. Para isso, utilize listas nos valores de cada
# palavra, guardando a linha e a coluna de cada ocorrência
entrada = open('entrada.txt','r')
dic = {}
palavras = []
posicoes = []
lin = 0
for linha in entrada.readlines():
    for l in linha.split(' '):
        palavras.append(l)
        posicoes.append([l,lin,linha.find(l)])
    lin += 1
for i in palavras:
    dic[i] = {'ocorrencias':palavras.count(i)}
    pos = []
    for j in posicoes:
        if j[0] == i:
            pos.append([j[1],j[2]])
            dic[i]['posicoes'] = pos
entrada.close()
saida = open('saida.json','w')
saida.write(str(dic).replace('\'','\"'))
saida.close()