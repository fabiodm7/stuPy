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
