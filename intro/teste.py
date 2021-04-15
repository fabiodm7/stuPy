'''
from cliente import cliente
from contas import conta

joao = cliente("Joao da Silva","11987577806")
maria = cliente("Maria da Silva","11986677786")

ccJoaoMaria = conta([joao,maria],'00001',500)
ccJoao = conta([joao],'00002',1000)

ccJoaoMaria.saque(50)
ccJoao.deposito(300)
ccJoaoMaria.saque(190)
ccJoao.deposito(95.15)
ccJoaoMaria.saque(250)
ccJoaoMaria.extrato()
ccJoao.extrato()
ccJoaoMaria.saque(100000)
ccJoaoMaria.resumo()
ccJoao.resumo()

jose = cliente("Jose da Silva","11987577806")

ccJoaoJose = conta([joao,jose],'00003',500)

ccJoaoJose.extrato()

from cliente import cliente
from banco import banco
from contas import conta
joao = cliente('Joao da Silva','3241-5599')
maria = cliente('Maria Silva','7231-9955')
jose = cliente('Jose Vargas','9721-3040')
contaJoaoMaria = conta([joao,maria],100)
contaJose = conta([jose],10)
tatu = banco('Tatu')
tatu.abreConta(contaJoaoMaria)
tatu.abreConta(contaJose)
tatu.listaContas()
'''
import regiao as rg

saoPauloCidade = rg.cidade('Sao Paulo', 100000, 'SP')
saoCarlos = rg.cidade('Sao Carlos', 50000, 'SP')
saoBernardo = rg.cidade('Sao Bernardo do Campo', 25000, 'SP')
santoAndre = rg.cidade('Santo Andre', 25000, 'SP')

paulo = rg.cidade('Paulo', 100000, 'RJ')
carlos = rg.cidade('Carlos', 50000, 'RJ')
bernardo = rg.cidade('Bernardo do Campo', 25000, 'RJ')
andre = rg.cidade('Andre', 25000, 'RJ')

cotia = rg.cidade('Cotia', 50000, 'MG')
beloHorizonte = rg.cidade('Belo Horizonte', 100000, 'MG')
triangulo = rg.cidade('Triangulo Mineiro', 50000, 'MG')

saoPaulo = rg.estado('Sao Paulo','SP')
rioJaneiro = rg.estado('Rio de Janeiro','RJ')
minasGerais = rg.estado('Minas Gerais','MG')

saoPaulo.novaCidade([saoBernardo,saoCarlos,saoPauloCidade,santoAndre])
rioJaneiro.novaCidade([andre,bernardo,carlos,paulo])
minasGerais.novaCidade([beloHorizonte,cotia,triangulo])

saoPaulo.resumo()
rioJaneiro.resumo()
minasGerais.resumo()