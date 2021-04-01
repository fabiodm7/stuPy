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

# Crie um programa que imprime as linhas de um arquivo. Esse programa deve receber
# três parâmetros pela linha de comando: o nome do arquivo, a linha inicial e a última
# linha a imprimir
import sys
entrada = open(sys.argv[1],'r')
inicio = int(sys.argv[2])
fim = int(sys.argv[3])
i = 1
for linha in entrada.readlines():
    if i >= inicio and i <= fim:
        print(linha)
    i += 1
entrada.close()

# Crie um programa que leia um arquivo texto e elemine os espaços repetidos entre as
# palavras e no fim das linhas. O arquivo texto também não deve ter mais de uma linha
# em branco repetida
def rmvRpt(texto,s):
    rpt = s + s
    if rpt in texto:
        return rmvRpt(texto.replace(rpt,s),s)
    else:
        return texto.replace(rpt,s)
entrada = open('entrada.txt','r')
saida = open('saida.txt','w')
repetido = ' ' # input('Digite o caractere que deseja retirar as repetições: ')
lista = ''.join(entrada.readlines())
lista = rmvRpt(lista,repetido)
saida.write(rmvRpt(lista,'\n\n'))
entrada.close()
saida.close()

# Altere o jogo da forca. Utilize um arquivo em que uma palavra seja gravada em cada
# linha. Ao iniciar o programa, utilize ese arquivo esse arquivo para carregar a lista
# de palavras. Experimente também perguntar o nome do jogador e gerar uma arquivo com
# o número de acertos dos 5 melhores
import random
import sys # linha nova
lista_palavras = []
#tamanho = int(input('Quantas palavras: ')) 
#for i in range(tamanho):
entrada = open('palavras.txt','r') # sys.argv[1],'r') # linha nova
saida = open('vencedores.txt','r')
campeoes = []
for s in saida.readlines():
    if s != '\n':
        campeoes.append(s[:-1])
saida.close()
for linha in entrada.readlines(): # linha nova
    lista_palavras.append(linha[:-1].lower().replace(' ','_')) # input('Digite a palavra secreta: ').lower().strip())
# for x in range(100):
#     print()
digitadas = []
acertos = []
erros = 0
palavra = random.sample(lista_palavras,1)[0]
jogador = input('Quem é o jogador: ')
vitorias = 0
while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        campeoes.append(jogador)
        saida = open('vencedores.txt','w')
        for c in campeoes:
            saida.write(str(c)+'\n')
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
        linha2 = ' \\|  '
    elif erros >= 4:
        linha2 = ' \\|/ '
    print('X%s' % linha2)
    linha3 = ''
    if erros == 5:
        linha3 += ' /   '
    elif erros >= 6:
        linha3 += ' / \\ '
    print('X%s' % linha3)
    print('X\n===========')
    if erros == 6:
        print('Enforcado!')
        print('Resposta certa: {0}'.format(palavra))
        break
entrada.close()
saida.close()

# TEORIA: Controle de uma agenda de telefones
def pede_nome(s=''):
    nome = (input('Nome: '))
    if repetido(nome):
        print('O nome digitado já consta na lista, digite outro!')
        return pede_nome()
    else:
        if len(s) > 0 and len(nome) <= 0:
            return s
        else:
            if '#' in nome:
                print('Caracter inválido(#) encontrado. Tente novamente')
                return pede_nome()
            else:
                return nome
def pede_telefone(s=''):
    telefone = (input('Telefone: '))
    if len(s) > 0 and len(telefone) <= 0:
        return s
    else:
        if '#' in telefone:
            print('Caracter inválido(#) encontrado. Tente novamente')
            return pede_telefone()
        else:
            return telefone
def mostra_dados(posicao,nome,telefone,aniversario,email):
    print('[%d] Nome: %s Telefone: %s Aniversario: %s E-mail: %s' % (posicao+1,nome,telefone,aniversario,email))
def pede_nome_arquivo():
    arquivo = open('arquivo.txt','r')
    a = arquivo.readline()
    if len(a) <= 1:
        arquivo.close()
        arquivo = open('arquivo.txt','w')
        a = input('Nome do arquivo: ')
        arquivo.write(a)
        arquivo.close()
        return a
    else:
        return a
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None
def novo():
    global agenda
    global status
    status = False
    nome = pede_nome()
    telefone = pede_telefone()
    aniversario = pede_aniversario()
    email = pede_email()
    agenda.append([nome,telefone])
    stts()
def apaga():
    global agenda
    global status
    status = False
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        check = input(''''''
            Deseja realmente realizar a operação:
            - Excluir o contato: %s
            Sim/Não [s/n]:''''''
            % (nome)
        )
        if check.lower() == 's':
            del agenda[p]
    else:
        print('Nome não encontrado.')
    stts()
def altera():
    p = pesquisa(pede_nome())
    if p != None:
        nomeOld = agenda[p][0]
        telefoneOld = agenda[p][1]
        aniversarioOld = agenda[p][2]
        emailOld = agenda[p][3]
        print('Encontrado:')
        mostra_dados(p,nomeOld,telefoneOld,aniversarioOld,emailOld)
        nome = pede_nome()
        telefone = pede_telefone()
        aniversario = pede_aniversario()
        email = pede_email()
        check = input(''''''
            Deseja realmente realizar a operação:
            - %s -> %s
            - %s -> %s
            - %s -> %s
            - %s -> %s
            Sim/Não [s/n]: ''''''
            % (nomeOld,nome,telefoneOld,telefone,aniversarioOld,aniversario,emailOld,email)
        )
        if check.lower() == 's':
            agenda[p] = [nome,telefone]
    else:
        print('Nome não encontrado.')
    global status
    status = False
    stts()
def lista():
    print('\nAgenda\n\n------')
    for x, e in enumerate(agenda):
        mostra_dados(x,e[0],e[1],e[2],e[3])
    print('------\n')
def le(a):
    global agenda
    nome_arquivo = a # pede_nome_arquivo()
    arquivo = open(nome_arquivo,'r',encoding = 'utf-8')
    agenda = []
    for l in arquivo.readlines():
        nome, telefone, aniversario, email = l.strip().split('#')
        agenda.append([nome,telefone,aniversario,email])
    arquivo.close()
    stts()
def grava(a):
    global status
    status = True
    nome_arquivo = a # pede_nome_arquivo()
    arquivo = open(nome_arquivo,'w',encoding = 'utf-8')
    for e in agenda:
        arquivo.write('%s#%s#%s#%s\n' % (e[0],e[1],e[2],e[3]))
    arquivo.close()
    stts()
def valida_faixa_inteiro(pergunta,inicio,fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print('Valor inválido, favor digitar entre %d e %d' % (inicio,fim))
def conta_contatos(a):
    arquivo = open(a,'r',encoding = 'utf-8')
    i = len(arquivo.readlines())
    return('%d contato(s) gravados' % i)
def ordenar():
    global agenda
    global status
    status = False
    agenda = sorted(agenda, key = lambda x : x[0])
    lista()
def stts():
    global status
    if status == False:
        print('Agenda não foi salva ainda, escolha a opção gravar.')
    else:
        print('Agenda gravada ou não alterada.')
def repetido(nome):
    global agenda
    rpt = False
    for x, e in enumerate(agenda):
        if nome in e:
            rpt = True
            break
        else:
            rpt = False
    return rpt
def pede_aniversario():
    aniversario = (input('Data de aniversario DD/MM/YYYY: '))
    if '#' in aniversario:
        print('Caracter inválido(#) encontrado. Tente novamente')
        return pede_aniversario()
    else:
        if aniversario[2] == '/' and aniversario[5] == '/' and len(aniversario) == 10:
            return aniversario
        else:
            print('Formato inválido. Tente novamente')
            return pede_aniversario()
def pede_email():
    email = (input('Data de aniversario DD/MM/YYYY: '))
    if '#' in email:
        print('Caracter inválido(#) encontrado. Tente novamente')
        return pede_email()
    else:
        if '@' not in email:
            return email
        else:
            print('Formato inválido. Tente novamente')
            return pede_email()
def atualizar(arq,a = False):
    if a:
        global agenda
        arquivo = open(arq,'r',encoding = 'utf-8')
        for linha in arquivo.readlines():
            agenda.append(linha.strip().split('#'))
        for e in agenda:
            while len(e) < 4:
                e.append('')
        arquivo.close()
        grava(arq)
def menu(a):
    print(''''''
        1 - Novo contato
        2 - Altera contato
        3 - Apaga contato
        4 - Lista de contatos
        5 - Grava contato
        6 - Lê contatos
        7 - Ordenar contatos por nome
        0 - Sair''''''
    )
    print(conta_contatos(a)) # Linha nova
    return valida_faixa_inteiro('Escolha uma opção: ',0,7)
agenda = []
# atualizacao = True
status = True
arquivo = pede_nome_arquivo()
# atualizar(arquivo,atualizacao)
while True:
    opcao = menu(arquivo)
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava(arquivo)
    elif opcao == 6:
        le(arquivo)
    elif opcao == 7:
        ordenar()
        
# Explique como os campos nome e telefone são gravados no arquivo de saída
# RESPOSTA: Apaga o conteudo e registra um novo contato, caso o usuário não efetue a 
# leitura antes de dar o comando gravar, todo o conteúdo é substituído.

# Altera o programa para exibir o tamanho da agenda no menu principal

# O que acontece se o nome ou telefone contiverem o caractere separador em seus conteúdos?
# Explique o problema e proponha uma solução
# RESPOSTA: o erro "too manu values to unpack" ocorre ao ler os contatos e interrompe
# a execução, deve-se verificar se o separador não foi utilizado nas entradas, antes de
# gravar o conteúdo

# Altere a função lista para que exiba também a posição de cada elemento

# Adicione a opção de ordenar a lista por nome no menu principal

# Nas funções de altera de apaga, peça ao usuário que confirme a operação antes de
# realizá-la

# Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi gravada. Você
# pode usar uma variável para controlar quando a lista foi alterada (novo, altera,
# apaga) e reinicializar esse valor quando ela for lida ou gravada

# Altere o programa para ler a última agenda lida ou gravada ao inicializar. Dica:
# utilize outro arquivo para armazenar o nome

# O que acontece com a agenda se ocorrer um erro de leitura ou gravação?
# RESPOSTA: Um erro interrompe a execução do programa e tudo realizado é perdido

# Altere as funções pede_nome e pede_telefone de forma a receberem um parâmetro opcional.
# Caso esse parâmetro seja passado, utilize-o como retorno caso a entrada de dados seja
# vazia

# Altere o programa de forma a verificar a repetição de nomes. Gere uma mensagem de erro,
# caso duas entradas na agenda tenham o mesmo o nome

# Modifique o programa para também controlar a data de aniversário e o e-mail do contato

# Modifique o programa de forma a resistrar vários telefones para a mesma pessoa.
# Permita também cadastrar o tipo do telefone: celular, fixo, residência, trabalho ou fax
# NAO FOI DESENVOLVIDO

# TEORIA: Criação de um página inicial em python
pagina = open('pagina.html','w',encoding='utf-8')
pagina.write('<DOCTYPE html>\n')
pagina.write('<html lang=\"pt-BR\">\n')
pagina.write('<head>\n')
pagina.write('<meta charset=\"utf-8\">\n')
pagina.write('<title>Título da página</title>\n')
pagina.write('</head>\n')
pagina.write('<body>\n')
pagina.write('Olá!\n')
for l in range(100):
    pagina.write('<p>%d</p>\n' % l)
pagina.write('</body>\n')
pagina.write('</html>\n')
pagina.close()

# TEORIA: Criação de um página inicial em python usando aspas triplas
pagina = open('pagina.html','w',encoding='utf-8')
pagina.write(''''''<DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Título da página</title>
</head>
<body>
Olá!
'''''')
for l in range(25):
    pagina.write('<p>%d</p>\n' % l)
pagina.write(''''''</body>
</html>'''''')
pagina.close()

# TEORIA: Pagina web a partir de um dicionário
filmes = {
    "drama":["Cidadão Kane","O Poderoso Chefão"],
    "comédia":["Tempos Modernos","American Pie","Dr. Dolittle"],
    "policial":["Chuva Negra","Desejo de Matar","Difícil de Matar"],
    "guerra":["Rambo","Platoon","Tora!Tora!Tora!"]
}
pagina = open('filmes.html','w',encoding='utf-8')
pagina.write(''''''<DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
Olá!
'''''')
for c,v in filmes.items():
    pagina.write('<h1>%s</h1>' % c)
    pagina.write('<ul>')
    for e in v:
        # pagina.write('<h2>%s</h2>' % e)
        # pagina.write('<p>%s</p>' % e)
        pagina.write('<li>%s</li>' % e)
    pagina.write('</ul>')
pagina.write(''''''</body>
</html>'''''')
pagina.close()

# Modifique o programa para utilizar <p> invés de <h2>

# Modifique o programa para gerara uma lista hmtl, utilizando os elementos ul e li.
# Todos os elementos da lista devem estar dentro do elemento ul, e cada item dentro 
# de um li. Exemplo:
# <ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>

# TEORIA: Diretório atual
import os
dAtual = os.getcwd()
print(dAtual)

# TEORIA: Troca de diretório
import os
os.chdir('intro')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('stuPy/intro')
print(os.getcwd())
os.chdir('../../stuPy')
print(os.getcwd())

# TEORIA: Criar diretórios
import os
os.mkdir('d')
os.mkdir('e')
os.mkdir('f')
print(os.getcwd())
os.chdir('d')
print(os.getcwd())
os.chdir('../e')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('f')
print(os.getcwd())

# TEORIA: Criar diretórios intermediarios
import os
os.makedirs('avo/pai/filho')
os.makedirs('avo/mae/filha')

# TEORIA: Alteração do nome de arquivos e diretórios
import os
os.mkdir('velho')
os.rename('velho','novo')

# TEORIA: Alteração do nome de arquivos e diretórios
import os
os.rename('avo/pai/filho','avo/mae/filho')

# TEORIA: Exclusão de arquivos e diretórios
import os
open('morimbundo.txt','w').close() # Cria um arquivo e o fecha imediatamente
os.mkdir('vago')
os.rmdir('vago')
os.remove('morimbundo.txt')
os.rmdir('avo/pai')
os.rmdir('avo/mae/filho')
os.rmdir('avo/mae/filha')
os.rmdir('d')
os.rmdir('e')
os.rmdir('f')
os.rmdir('avo/mae')
os.rmdir('avo')
os.rmdir('novo')

# TEORIA: Listagem do nome de arquivos e diretórios
import os
print(os.listdir('.'))
print(os.listdir('./intro'))

# TEORIA: Verificação se é diretório ou arquivo
import os
import os.path
for a in os.listdir('.'):
    if os.path.isdir(a):
        print('%s/' % a)
    elif os.path.isfile(a):
        print('%s' % a)

# Verificação se um diretório ou arquivo já existe
import os.path
diretorio = 'intro'
if os.path.exists(diretorio):
    print('O diretorio %s/ existe' % diretorio)
else:
    print('O diretorio %s/ não existe' % diretorio)

# Crie um programa que corrija o programa anterior de forma a verificar se o diretorio
# existe e é um diretório
import os.path
diretorio = 'agenda.txt'
if os.path.exists(diretorio):
    if os.path.isdir(diretorio):
        print('O diretorio %s/ existe' % diretorio)
    else:
        print('%s existe, mas é um arquivo' % diretorio)
else:
    print('O diretorio ou arquivo %s não existe' % diretorio)

# Modifique o programa de forma a receber o nome do arquivo ou diretório a verificar 
# pela linha de comando. Imprima se existir e se for um arquivo ou um diretório
import sys
import os.path
diretorio = sys.argv[1]
if os.path.exists(diretorio):
    if os.path.isdir(diretorio):
        print('O diretorio %s/ existe' % diretorio)
    else:
        print('%s existe, mas é um arquivo' % diretorio)
else:
    print('O diretorio ou arquivo %s não existe' % diretorio)

# Crie um programa que gere uma página html com links para todos os arquivos jpg e png
# encontrados a partir de um diretório informado na linha de comando
import sys
import os
import os.path
diretorio = '../stuPy' # sys.argv[1]
arquivos = os.listdir(diretorio)
pagina = open('arquivos.html','w',encoding='utf-8')
pagina.write(''''''<DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos do diretório</title>
</head>
<body>
'''''')
pagina.write('<h1>%s</h1>' % diretorio)
pagina.write('<ul>')
for a in arquivos:
    if a[-3:] == 'txt':
        pagina.write('<li><a href="%s/%s" target="_blank">%s</a></li>' % (diretorio,a,a))
pagina.write('</ul>')
pagina.write(''''''</body>
</html>'''''')
pagina.close()

# TEORIA: Obtenção de mais informações sobre o arquivo
import os
import os.path
import time
import sys
nome = 'entrada.txt' # sys.artv[1]
print('Nome: %s' % nome)
print('Tamanho: %d bytes' % os.path.getsize(nome))
print('Criado: %s' % time.ctime(os.path.getctime(nome)))
print('Modificado: %s' % time.ctime(os.path.getmtime(nome)))
print('Acessado: %s' % time.ctime(os.path.getatime(nome)))

# TEORIA: Obtenção das horas em python
import time
agora = time.time()
print(agora)
agora = time.ctime(agora)
print(agora)
agora2 = time.localtime()
print(agora2)
agora3 = time.gmtime(time.time())
print(agora3)

# TEORIA: Obtenção de data e hora por nome
import time
agora = time.localtime()
print('Ano: %d' % agora.tm_year)
print('Mês: %d' % agora.tm_mon)
print('Dia: %d' % agora.tm_mday)
print('Hora: %d' % agora.tm_hour)
print('Minuto: %d' % agora.tm_min)
print('Segundo: %d' % agora.tm_sec)
print('Dia da semana: %d' % agora.tm_wday)
print('Dia do ano: %d' % agora.tm_yday)
print('Horário de verão: %d' % agora.tm_isdst)

# Altere o jogo da forca. Utilize funções de tempo para cronometrar a duração de
# cada partida
import random
import sys
import time # linha nova
lista_palavras = []
entrada = open('palavras.txt','r')
saida = open('vencedores.txt','r')
campeoes = []
for s in saida.readlines():
    if s != '\n':
        campeoes.append(s[:-1])
saida.close()
for linha in entrada.readlines():
    lista_palavras.append(linha[:-1].lower().replace(' ','_'))
digitadas = []
acertos = []
erros = 0
palavra = random.sample(lista_palavras,1)[0]
jogador = input('Quem é o jogador: ')
inicio = time.time() # linha nova
vitorias = 0
def tempo(inicio,final): # linha nova
    return('%s segundos' % (final - inicio)) # linha nova
while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        fim = time.time() # linha nova
        print('Duração da partida: %s' % tempo(inicio,fim)) # linha nova
        campeoes.append(jogador)
        saida = open('vencedores.txt','w')
        for c in campeoes:
            saida.write(str(c)+'\n')
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
        linha2 = ' \\|  '
    elif erros >= 4:
        linha2 = ' \\|/ '
    print('X%s' % linha2)
    linha3 = ''
    if erros == 5:
        linha3 += ' /   '
    elif erros >= 6:
        linha3 += ' / \\ '
    print('X%s' % linha3)
    print('X\n===========')
    if erros == 6:
        print('Enforcado!')
        print('Resposta certa: {0}'.format(palavra))
        fim = time.time() # linha nova
        print('Duração da partida: %s' % tempo(inicio,fim)) # linha nova
        break
entrada.close()
saida.close()

# TEORIA: Uso de caminhos
import os.path
caminho = 'i/j/k'
print(os.path.abspath(caminho))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print(os.path.split(caminho))
print(os.path.splitext('agenda.txt'))
print(os.path.splitdrive('C:/Windows'))

# TEORIA: Combinação dos componentes de um caminho
import os.path
print(os.path.join('c:','dados','programas'))
print(os.path.abspath(os.path.join('c:','dados','programas')))

# TEORIA: Visita a todos os subdiretorios recursivamente
import os
import sys
for raiz,diretorios,arquivos in os.walk(sys.argv[1]):
    print('\nCaminho: ', raiz)
    for d in diretorios:
        print(' %s/' % d)
    for f in arquivos:
        print(' %s' % f)
    print('%d diretorio(s), %d arquivo(s)' % (len(diretorios),len(arquivos)))

# Utilizando a função os.walk, crie uma página html com o nome e o tamanho de cada
# arquivo de um diretório passado e de seus subdiretórios
import sys
import os
import os.path
diretorio = '../stuPy' # sys.argv[1]
arquivos = os.listdir(diretorio)
pagina = open('diretorios.html','w',encoding='utf-8')
pagina.write(''''''<DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos do diretório</title>
</head>
<body>
'''''')
pagina.write('<h1>%s</h1>' % diretorio)
for raiz,diretorios,arquivos in os.walk(diretorio): # sys.argv[1]):
    pagina.write('<h2>Caminho: %s</h2>' % raiz)
    for d in diretorios:
        pagina.write('<p> %s/</p>' % d)
    for f in arquivos:
        pagina.write('<p> %s - %s</p>' % (f,os.path.getsize(f)))
pagina.write(''''''</body>
</html>'''''')
pagina.close()
'''
# Utilizando a função os.walk, crie um programa que calcule o espaço ocupado por cada
# diretório e subdiretório, gerando uma página HTML com os resultados
