'''
Exercícios do capítulo 11 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Banco de dados
'''
'''
# TEORIA: Exemplo de uso do SQLite em Python
import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute(''''''
    create table agenda (
        nome text,
        telefone text
    )
'''''')
cursor.execute(''''''
    insert into agenda (nome, telefone)
        values(?,?)
'''''',('Nilo','97788-1432'))
conexao.commit()
cursor.close()
conexao.close()

# TEORIA: Consulta
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
resultado = cursor.fetchone()
print('Nome: %s\nTelefone: %s' % (resultado))
cursor.close()
conexao.close()

#TEORIA: Inserindo múltiplos registros
import sqlite3
dados = [   ('João','98901-0109'),
            ('André','98902-8900'),
            ('Maria','97891-3321')]
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.executemany(
    'insert into agenda (nome, telefone) values(?,?)',dados
)
conexao.commit()
cursor.close()
conexao.close()

#TEORIA: Consulta com múltiplos resultados
import sqlite3
from sqlite3.dbapi2 import Cursor
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
resultado = cursor.fetchall()
for registro in resultado:
    print ('Nome: %s\nTelefone: %s' % (registro))
cursor.close()
cursor.close()

#TEORIA: Consulta registro por registro
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print('Nome: %s\nTelefone: %s' % (resultado))
cursor.close()
conexao.close()

#TEORIA: Uso do with para fechar a conexão
import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from agenda')
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print('Nome: %s\nTelefone: %s' % (resultado))

# Faça um programa que crie um banco de dados precos.db com a tablea de precos para armazenar
# uma lista de precos de venda de produtos. A tabela deve conter o nome do produto e seu
# respectivo preço. O programa também deve inserir alguns dados para teste.
import sqlite3

dados = [   ('pera',2.00),
            ('uva',3.00),
            ('maçã',4.00),
            ('salada mista',5.00)]

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute(''''''
    create table precos (
        produto text,
        preco text
    )
'''''')
cursor.executemany(
    'insert into precos (produto, preco) values(?,?)',dados
)
conexao.commit()
cursor.close()
conexao.close()

# Faça um programa para listar todos os preços do banco preços.db
import sqlite3
from contextlib import closing

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from precos')
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print('Produto %s: R$ %s' % (resultado))

# TEORIA: Consulta com filtro de seleção
import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = 'Nilo'")
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print('Nome: %s\nTelefone: %s' % (resultado))

# TEORIA: Consulta com filtro de seleção vindo de variável
import sqlite3
nome = input('Nome a selecionar: ')
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = "%s"' % nome)
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print('Nome: %s\nTelefone: %s' % (resultado))
cursor.close()
conexao.close()

# TEORIA: Consulta utilizando parâmetros
import sqlite3
nome = input('Nome a selecionar: ')
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = ?', (nome,))
x = 0
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        if x == 0:
            print('Nada encontrado.')
        break
    print('Nome: %s\nTelefone: %s' % (resultado))
    x += 1
cursor.close()
conexao.close()

# Escreva um programa que realiza consultas do banco de dados preços.db.
# O programa deve perguntar o nome do produto e listar seu preço
import sqlite3
nome = input('Selecione o produto: ')
conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute('select * from precos where produto = ?', (nome,))
x = 0
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        if x == 0:
            print('Nada encontrado.')
        break
    print('Produto %s: R$ %s' % (resultado))
    x += 1
cursor.close()
conexao.close()

# Modifique o programa anterior de forma a perguntar dois valores
# e listar todos os produtos com preços entre esses dois valores
import sqlite3
minimo = float(input('Valor mínimo: '))
maximo = float(input('Valor máximo: '))
conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute(''''''
    select
        *
    from
        precos
    where
        preco >= ?
        and preco <= ?
    '''''', (minimo,maximo))
x = 0
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        if x == 0:
            print('Nada encontrado.')
        break
    print('Produto %s: R$ %s' % (resultado))
    x += 1
cursor.close()
conexao.close()
'''
# TEORIA: Atualizando o telefone
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('update agenda set telefone = "12345-6789" where nome = "Nilo"')
conexao.commit()
conexao.close()