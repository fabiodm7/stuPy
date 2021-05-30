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
'''
