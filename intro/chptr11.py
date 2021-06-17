'''
Exercícios do capítulo 11 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Banco de dados
'''
# TEORIA: Exemplo de uso do SQLite em Python
import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("""
    create table agenda (
        nome text,
        telefone text
    )
""")
cursor.execute("""
    insert into agenda (nome, telefone)
        values(?,?)
""",('Nilo','97788-1432'))
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
cursor.execute("""
    create table precos (
        produto text,
        preco text
    )
""")
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

# Escreva um programa que realiza consultas do banco de dados preços.db. O programa deve perguntar
# o nome do produto e listar seu preço
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
cursor.execute("""
    select
        *
    from
        precos
    where
        preco >= ?
        and preco <= ?
    """, (minimo,maximo))
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

# TEORIA: Atualizando o telefone
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('update agenda set telefone = "12345-6789" where nome = "Nilo"')
conexao.commit()
conexao.close()

# TEORIA: Exemplo de update sem where e com rowcount
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("""update agenda set telefone = '12345-6789'""")
print('Registros alterados: ', cursor.rowcount)
conexao.commit()
conexao.close()

# TEORIA: Update com rollback
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("""update agenda set telefone = '12345-6789'""")
print('Registros alterados: ', cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print('Alterações gravadas')
else:
    conexao.rollback()
    print('Alterações abortadas')
conexao.close()

# Escreva um programa que aumente o preço de todos os produtos do banco precos.db em 10%
import sqlite3
conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute("""update precos set preco = preco + 10""")
print('Registros alterados: ', cursor.rowcount)
conexao.commit()
# cursor.execute("""select * from precos""")
# while True:
#     resultado = cursor.fetchone()
#     if resultado == None:
#         break
#     print('Produto: %s | Preco: %s' % (resultado))
conexao.close()

# Escreve um programa que pergunte o nome do produto e um novo preço. Usando o banco precos.db,
# atualize o preço deste produto no banco de dados.
import sqlite3
p = input('Qual produto deseja alterar: ')
v = float(input('Qual o novo valor: '))
conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute("""update precos set preco = ? where produto = ?""", (v,p))
print('Registros alterados: ', cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print('Alterações gravadas')
else:
    conexao.rollback()
    print('Alterações abortadas')
# cursor.execute("""select * from precos""")
# while True:
#     resultado = cursor.fetchone()
#     if resultado == None:
#         break
#     print('Produto: %s | Preco: %s' % (resultado))
conexao.close()

# TEORIA: Apagando registros
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("""delete from agenda where nome = 'Maria'""")
print('Registros apagados: ', cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print('Alterações gravadas')
else:
    conexao.rollback()
    print('Alterações abortadas')
conexao.close()

# TEORIA: Consulta a vários registros, acesso simplificado
import sqlite3
with sqlite3.connect('agenda.db') as conexao:
    for registro in conexao.execute('select * from agenda'):
        print('Nome: %s | Telefone: %s' % (registro))

# TEORIA: Acessando os campos pelo nome
import sqlite3
conexao = sqlite3.connect('agenda.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
for registro in cursor.execute('select * from agenda'):
    print('Nome: %s | Telefone: %s' % (registro['nome'],registro['telefone']))
cursor.close()
conexao.close()

# TEORIA: Criação de banco de dados com a população dos estados brasileiros
import sqlite3
dados = [["Rondônia",1796460],["Acre",894470],["Amazonas",4207714],["Roraima",631181],["Pará",8690745],
["Amapá",861773],["Tocantins",1590248],["Maranhão",7114598],["Piauí",3281480],["Ceará",9187103],
["Rio Grande do Norte",3534165],["Paraíba",4039277],["Pernambuco",9616621],["Alagoas",3351543],
["Sergipe",2318822],["Bahia",14930634],["Minas Gerais",21292666],["Espírito Santo",4064052],
["Rio de Janeiro",17366189],["São Paulo",46289333],["Paraná",11516840],["Santa Catarina",7252502],
["Rio Grande do Sul",11422973],["Mato Grosso do Sul",2809394],["Mato Grosso",3526220],["Goiás",7113540],
["Distrito Federal",3055149]]
conexao = sqlite3.connect('brasil.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
cursor.execute("""create table estados(id integer primary key autoincrement, nome text, populacao integer)""")
cursor.executemany("insert into estados(nome,populacao) values(?,?)",dados)
conexao.commit()
cursor.close()
conexao.close()

# TEORIA: Consulta dos estados brasileiros, ordenados por nome
import sqlite3
conexao = sqlite3.connect('brasil.db')
conexao.row_factory = sqlite3.Row
print('%3s %-20s %12s' % ('id','estado','populacao'))
print('='*37)
for estado in conexao.execute('select * from estados order by populacao desc'):
    print('%3s %-20s %12s' % (estado['id'],estado['nome'],estado['populacao']))
conexao.close()

# TEORIA: Alterando a tabela
import sqlite3
with sqlite3.connect('brasil.db') as conexao:
    conexao.execute("""alter table estados add sigla text""")
    conexao.execute("""alter table estados add regiao text""")

# TEORIA: Preechendo a sigla e a região de cada estado
import sqlite3
dados = [["RO","N","Rondônia"],["AC","N","Acre"],["AM","N","Amazonas"],["RR","N","Roraima"],
["PA","N","Pará"],["AP","N","Amapá"],["TO","N","Tocantins"],["MA","NE","Maranhão"],
["PI","NE","Piauí"],["CE","NE","Ceará"],["RN","NE","Rio Grande do Norte"],["PB","NE","Paraíba"],
["PE","NE","Pernambuco"],["AL","NE","Alagoas"],["SE","NE","Sergipe"],["BA","NE","Bahia"],
["MG","SE","Minas Gerais"],["ES","SE","Espírito Santo"],["RJ","SE","Rio de Janeiro"],["SP","SE","São Paulo"],
["PR","S","Paraná"],["SC","S","Santa Catarina"],["RS","S","Rio Grande do Sul"],["MS","CO","Mato Grosso do Sul"],
["MT","CO","Mato Grosso"],["GO","CO","Goiás"],["DF","CO","Distrito Federal"]]
with sqlite3.connect('brasil.db') as conexao:
    conexao.executemany("""update estados set sigla = ?, regiao = ? where nome = ?""", dados)

# TEORIA: Agrupando e contando estados por região
import sqlite3
print('Região Números de estados')
print('====== ==================')
with sqlite3.connect('brasil.db') as conexao:
    for regiao in conexao.execute("""select regiao, count(*) from estados group by regiao"""):
        print('{0:6} {1:17}'.format(*regiao))

# TEORIA: Usando as funções de agregação
import sqlite3
print('Regiao Estados População   Mínima     Máxima     Média      Total')
print('====== =======         ========== ========== ==========    ==========')
with sqlite3.connect('brasil.db') as conexao:
    for regiao in conexao.execute("""select regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) from estados group by regiao"""):
        print('{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}'.format(*regiao))
    print('\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}'.format(*conexao.execute("""select count(*), min(populacao),max(populacao),avg(populacao),sum(populacao) from estados""").fetchone()))

# TEORIA: Funções de agregação com order by
import sqlite3
print('Regiao Estados População   Mínima     Máxima     Média      Total')
print('====== =======         ========== ========== ==========    ==========')
with sqlite3.connect('brasil.db') as conexao:
    for regiao in conexao.execute("""select regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) from estados group by regiao order by sum(populacao) desc"""):
        print('{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}'.format(*regiao))
    print('\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}'.format(*conexao.execute("""select count(*), min(populacao),max(populacao),avg(populacao),sum(populacao) from estados""").fetchone()))

# TEORIA: Utilizando having para ordenar apenas regiões com mais de 5 estados
import sqlite3
print('Regiao Estados População   Mínima     Máxima     Média      Total')
print('====== =======         ========== ========== ==========    ==========')
with sqlite3.connect('brasil.db') as conexao:
    for regiao in conexao.execute("""select regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) as tpop from estados group by regiao having count(*) > 5 order by tpop desc"""):
        print('{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}'.format(*regiao))

# TEORIA: Criando uma tabela de feriados nacionais
import sqlite3
feriados = [['2021-01-01','Confraternização universal'],['2021-04-21','Tiradentes'],
            ['2021-05-01','Dia do trabalhador'],['2021-09-07','Idenpendência'],
            ['2021-10-12','Padroeira do Brasil'],['2021-11-02','Finados'],
            ['2021-11-15','Proclamação da república'],['2021-12-25','Natal']]
with sqlite3.connect('brasil.db') as conexao:
    conexao.execute('drop table feriados')
    conexao.execute('create table feriados(id integer primary key autoincrement, data date, descricao text)')
    conexao.executemany('insert into feriados(data,descricao) values (?,?)',feriados)

# TEORIA: Acessando um campo do tipo data
import sqlite3
with sqlite3.connect('brasil.db') as conexao:
    for feriado in conexao.execute('select * from feriados'):
        print(feriado)

# TEORIA: Solicitando o tratamento do tipo dos campos
import sqlite3
with sqlite3.connect('brasil.db',detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    for feriado in conexao.execute('select * from feriados'):
        print(feriado)

# TEORIA: Trabalhando com datas
import sqlite3
with sqlite3.connect('brasil.db',detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    conexao.row_factory = sqlite3.Row
    for feriado in conexao.execute('select * from feriados'):
        print('{0} {1}'.format(feriado['data'].strftime('%d/%m'),feriado['descricao']))

# TEORIA: Feriados nos próximos 60 dias
import sqlite3
import datetime
hoje = datetime.date.today()
hoje60dias = hoje + datetime.timedelta(days=60)
with sqlite3.connect('brasil.db',detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    conexao.row_factory = sqlite3.Row
    for feriado in conexao.execute('select * from feriados where data >= ? and data <= ?',(hoje, hoje60dias)):
        print('{0} {1}'.format(feriado['data'].strftime('%d/%m'),feriado['descricao']))

# TEORIA: Agenda com banco de dados completa
import sys
import sqlite3
import os.path
from functools import total_ordering

BANCO = """
    create table tipos(id integer primary key autoincrement, descricao text);
    create table nomes(id integer primary key autoincrement, nome text);
    create table telefones(id integer primary key autoincrement, id_nome integer, numero text, id_tipo integer);
    insert into tipos(descricao) values ('celular');
    insert into tipos(descricao) values ('fixo');
    insert into tipos(descricao) values ('fax');
    insert into tipos(descricao) values ('casa');
    insert into tipos(descricao) values ('trabalho');
"""

def nulo_ou_vazio(texto):
    return texto == None or not texto.strip()
def valida_faixa_inteiro(pergunta, inicio, fim, padrao = None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao != None:
                entrada = padrao
                valor = int(entrada)
                if inicio <= valor <= fim:
                    return(valor)
        except ValueError:
            print('Valor inválido, favor digitar entre %d e %d' % (inicio,fim))
def valida_faixa_inteiro_ou_branco(pergunta,inicio,fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print('Valor inválido, favor digitar entre %d e %d' % (inicio,fim))

class ListaUnica:
    def __init__(self,elem_class):
        self.lista = []
        self.elem_class = elem_class
    def __len__(self):
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem__(self,p):
        return self.lista[p]
    def indiceValido(self,i):
        return i >= 0 and i <= len(self.lista)
    def adiciona(self,elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)
    def remove(self,elem):
        self.lista.remove(elem)
    def pesquisa(self,elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1
    def verifica_tipo(self,elem):
        if type(elem) != self.elem_class:
            raise TypeError('Tipo inválido')
    def ordena(self,chave = None):
        self.lista.sort(key=chave)

class DBListaUnica(ListaUnica):
    def __init__(self,elem_class):
        super().__init__(elem_class)
        self.apagados = []
    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)
    def limpa(self):
        self.apagados = []

@total_ordering
class Nome:
    def __init__(self,nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    def __repr__(self):
        return '<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>'.format(
            id(self), self.__nome,self.__chave,type(self).__name__
        )
    def __eq__(self,outro):
        return self.nome == outro.nome
    def __lt__(self,outro):
        return self.nome < outro.nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,valor):
        if nulo_ou_vazio(valor):
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()

class DBNome(Nome):
    def __init__(self,nome,id_= None):
        super().__init__(nome)
        self.id = id_

@total_ordering
class TipoTelefone:
    def __init__(self,tipo):
        self.tipo = tipo
    def __str__(self):
        return '({0})'.format(self.tipo)
    def __eq__(self,outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo
    def __lt__(self,outro):
        return self.tipo < outro.tipo

class DBTipoTelefone(TipoTelefone):
    def __init__(self,id_,tipo):
        super().__init__(tipo)
        self.id = id_

class Telefone:
    def __init__(self,numero,tipo = None):
        self.numero = numero
        self.tipo = tipo
    def __str__(self):
        if self.tipo != None:
            tipo = self.tipo
        else:
            tipo = ''
        return '{0} {1}'.format(self.numero,tipo)
    def __eq__(self,outro):
        return self.numero == outro.numero and (
            (self.tipo == outro.tipo) or (
                self.tipo == None or outro.tipo == None
            )
        )
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,valor):
        if nulo_ou_vazio(valor):
            raise ValueError('Numero não pode ser None ou em branco')
        self.__numero = valor

class DBTelefone(Telefone):
    def __init__(self,numero,tipo = None,id_=None,id_nome=None):
        super().__init__(numero,tipo)
        self.id = id_
        self.id_nome = id_nome

class DBTelefones(DBListaUnica):
    def __init__(self):
        super().__init__(DBTelefone)

class DBTiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(DBTipoTelefone)

class DBDadoAgenda:
    def __init__(self,nome):
        self.nome = nome
        self.telefones = DBTelefones()
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,valor):
        if type(valor) != DBNome:
            raise TypeError('Nome deve ser uma instância da classe DBNome')
        self.__nome = valor
    def pesquisaTelefone(self,telefone):
        posicao = self.telefones.pesquisa(DBTelefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]

class DBAgenda:
    def __init__(self,banco):
        self.tiposTelefone = DBTiposTelefone()
        self.banco = banco
        novo = not os.path.isfile(banco)
        self.conexao = sqlite3.connect(banco)
        self.conexao.row_factory = sqlite3.Row
        if novo:
            self.cria_banco()
        self.carregaTipos()
    def carregaTipos(self):
        for tipo in self.conexao.execute('select * from tipos'):
            id_ = tipo['id']
            descricao = tipo['descricao']
            self.tiposTelefone.adiciona(DBTipoTelefone(id_,descricao))
    def cria_banco(self):
        self.conexao.executescript(BANCO)
    def pesquisaNome(self,nome):
        if not isinstance(nome,DBNome):
            raise TypeError('Nome deve ser do tipo DBNome')
        achado = self.conexao.execute("""select count(*)
            from nomes where nome = ?""", (nome.nome,)).fetchone
        if (achado[0] > 0):
            return self.carrega_por_nome(nome)
        else:
            return None
    def carrega_por_id(self,id):
        consulta = self.conexao.execute(
            "select * from nomes where id = ?",(id,)
        )
        return carrega(consulta.fetchone())
    def carrega_por_nome(self,nome):
        consulta = self.conexao.execute(
            "select * from nomes where nome = ?",(nome.nome,)
        )
        return carrega(consulta.fetchone())
    def carrega(self,consulta):
        if consulta is None:
            return None
        novo = DBDadoAgenda(DBNome(consulta['nome'],consulta['id']))
        for telefone in self.conexao.execute(
            "select * from telefones where id_nome = ?",
            (novo.nome.id,)
        ):
            ntel = DBTelefone(telefone['numero'],None,
                telefone['id'],telefone['id_nome'])
            for tipo in self.tiposTelefone:
                if tipo.id == telefone['id_tipo']:
                    ntel.tipo = tipo
                    break
            novo.telefones.adiciona(ntel)
        return novo
    def lista(self):
        consulta = self.conexao.execute(
            "select * from nomes order by nome"
        )
        for registro in consulta:
            yield self.carrega(registro)
    def novo(self,registro):
        try:
            cur = self.conexao.cursor()
            cur.execute("insert into nomes(nome values (?)",
                (str(registro.nome),))
            registro.nome.id = cur.lastrowid
            for telefone in registro.telefones:
                cur.execute("""insert into telefones(numero,
                    id_tipo,id_nome) values (?,?,?)""",
                    (telefone.numero,telefone.tipo.id,
                    registro.nome.id))
                telefone.id = cur.lastrowid
            self.conexao.commit()
        except:
            self.conexao.rollback()
            raise
        finally:
            cur.close()
    def atualiza(self,registro):
        try:
            cur = self.conexao.cursor()
            cur.execute("update nomes set nome = ? where id = ?",
                (str(registro.nome),registro.nome.id))
            for telefone in registro.telefones:
                if telefone.id is None:
                    cur.execute("""insert into telefones(numero,
                        id_tipo,id_nome)
                        values (?,?,?)""",
                        (telefone.numero,telefone.tipo.id,registro.nome.id))
                    telefone.id = cur.lastrowid
                else:
                    cur.execute("""update telefones set numero = ?,
                        id_tipo = ?, id_nome = ?
                        where id = ?""",
                        (telefone.numero, telefone.tipo.id,registro.nome.id,telefone.id))
            for apagado in registro.telefones.apagados:
                cur.execute('delete from telefones where id = ?',(apagado,))
            self.conexao.commit()
            registro.telefones.limpa()
        except:
            self.conexao.rollback()
            raise
        finally:
            cur.close()
    def apaga(self,registro):
        try:
            cur = self.conexao.cursor()
            cur.execute("delete from telefones where id_nome = ?",(registro.nome.id,))
            cur.execute("delete from nomes where id = ?",(registro.nome.id,))
            self.conexao.commit()
        except:
            self.conexao.rollback()
            raise
        finally:
            cur.close()

class Menu:
    def __init__(self):
        self.opcoes = [['Sair',None]]
    def adicionaopcao(self,nome,funcao):
        self.opcoes.append([nome,funcao])
    def exibe(self):
        print('====')
        print('Menu')
        print('====\n')
        for i, opcao in enumerate(self.opcoes):
            print('[{0}] = {1}'.format(i,opcao[0]))
        print()
    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro('Escola uma opção: ',0,len(self.opcoes) - 1)
            if escolha == 0:
                break
            self.opcoes[escolha][1]()

class AppAgenda:
    @staticmethod
    def pede_nome():
        return(input('Nome: '))
    @staticmethod
    def pede_telefone():
        return(input('Telefone: '))
    @staticmethod
    def mostra_dados(dados):
        print('Nome: %s' % dados.nome)
        for i,telefone in enumerate(dados.telefones):
            print('{0} - Telefone: {1}'.format(i,telefone))
        print()
    def __init__(self,banco):
        self.agenda = DBAgenda(banco)
        self.menu = Menu()
        self.menu.adicionaopcao('Novo',self.novo)
        self.menu.adicionaopcao('Altera',self.altera)
        self.menu.adicionaopcao('Apaga',self.apaga)
        self.menu.adicionaopcao('Lista',self.lista)
        self.ultimo_nome = None
    def pede_tipo_telefone(self,padrao = None):
        for i,tipo in enumerate(self.agenda.tiposTelefone):
            print(' {0} - {1} '.format(i,tipo),end=None)
        t = valida_faixa_inteiro('Tipo: ',0,len(self.agenda.tiposTelefone)-1,padrao)
        return self.agenda.tiposTelefone[t]
    def pesquisa(self,nome):
        if type(nome) == str:
            nome = DBNome(nome)
        dado = self.agenda.pesquisaNome(nome)
        return dado
    def novo(self):
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = DBNome(novo)
        if self.pesquisa(nome) != None:
            print('Nome já existe!')
            return
        registro = DBDadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.novo(registro)
    def apaga(self):
        nome = AppAgenda.pede_nome()
        if(nulo_ou_vazio(nome)):
            return
        p = self.pesquisa(nome)
        if p != None:
            self.agenda.apaga(p)
        else:
            print('Nome não encontrado.')
    def altera(self):
        nome = AppAgenda.pede_nome()
        if(nulo_ou_vazio(nome)):
            return
        p = self.pesquisa(nome)
        if p != None:
            print('\nEncontrado:\n')
            AppAgenda.mostra_dados(p)
            print('Digite enter caso não queira alterar o nome')
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                p.nome.nome = novo
            self.menu_telefones(p)
            self.agenda.atualiza(p)
        else:
            print('Nome não encontrado!')
    def menu_telefones(self,dados):
        while True:
            print('\nEditando telefones\n')
            AppAgenda.mostra_dados_telefone(dados)
            if(len(dados.telefones) > 0):
                print('\n[A] - alterar\n[D] - apagar\n', end = '')
            print('[N] - novo\n[S] - sair\n')
            operacao = input('Escolha uma operação: ')
            operacao = operacao.lower()
            if operacao not in ['a','d','n','s']:
                print('Operação inválida. Digita A, D, N ou S')
                continue
            if operacao == 'a' and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operacao == 'd' and len(dados.telefones) > 0:
                self.apaga_telefone(dados)
            elif operacao == 'n':
                self.novo_telefone(dados)
            elif operacao == 's':
                break
    def novo_telefone(self,dados):
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone):
            return
        if dados.pesquisaTelefone(telefone) != None:
            print('Telefone já existe')
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(DBTelefone(telefone,tipo))
    def apaga_telefone(self,dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posiçãodo número a apagar, enter para sair: ",
            0,len(dados.telefones)-1
        )
        if t == None:
            return
        dados.telefones.remove(dados.telefones[t])
    def altera_telefones(self,dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posição do número a alterar, enter para sair: ",
            0,len(dados.telefones)-1
        )
        if t == None:
            return
        telefone = dados.telefones[t]
        print('Telefone: %s' % telefone)
        print('Digite enter caso não queira alterar o número')
        novotelefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novotelefone):
            telefone.numero = novotelefone
        print('Digite enter caso não queira alterar o tipo')
        telefone.tipo = self.pede_tipo_telefone(self.agenda.tiposTelefone.pesquisa(telefone.tipo))
    def lista(self):
        print('\nAgenda')
        print('-' * 60)
        for e in self.agenda.lista():
            AppAgenda.mostra_dados(e)
        print('-' * 60)
    def execute(self):
        self.menu.execute()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = AppAgenda(sys.argv[1])
        app.execute()
    else:
        print('Erro: nome do banco de dados não informado')
        print('      agenda.py nome_do_banco')