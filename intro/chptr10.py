'''
Exercícios do capítulo 10 do livro "Introdução ao python"
de Nilo Ney Coutinho Menezes

Classes e objetos

# TEORIA: Modelagem de uma televisão
class televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv = televisão()
print('TV Ligada: ',tv.ligada)
print('TV Canal: ',tv.canal)
tvSala = televisão()
tvSala.ligada = True
tvSala.canal = 4
print('TV Ligada: ',tvSala.ligada)
print('TV Canal: ',tvSala.canal)

# Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão
# e atribua tamanhos e marcas diferentes. Depois, imprima o valor desses atributos de
# forma a confirmar a independência dos valores de cada instância (objeto).
class televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = None
        self.marca = None

tv = televisão()
tv.tamanho = '32"'
tv.marca = 'LG'
print('TV tamanho: ',tv.tamanho)
print('TV marca: ',tv.marca)
tvSala = televisão()
tvSala.tamanho = '42"'
tvSala.marca = 'Samsung'
print('TV tamanho: ',tvSala.tamanho)
print('TV marca: ',tvSala.marca)

# TEORIA: Adição de métodos para mudar o canal
class televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = None
        self.marca = None
    def mudaCanalDiminui(self):
        self.canal -= 1
    def mudaCanalAumenta(self):
        self.canal += 1

tv = televisão()
tv.ligada = True
tv.mudaCanalAumenta()
tv.mudaCanalAumenta()
tv.tamanho = '32"'
tv.marca = 'LG'
print('TV tamanho: ',tv.tamanho)
print('TV marca: ',tv.marca)
print('TV ligada: ',tv.ligada)
print('TV Canal: ',tv.canal)

# TEORIA: Verificação da faixa de canais
class televisao:
    def __init__(self,min,max):
        self.ligada = False
        self.canal = 2
        self.tamanho = None
        self.marca = None
        self.cmin = min
        self.cmax = max
    def mudaCanalDiminui(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def mudaCanalAumenta(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = televisao(1,99)
for x in range(0,120):
    tv.mudaCanalAumenta()
print(tv.canal)
for x in range(0,120):
    tv.mudaCanalDiminui()
print(tv.canal)

# Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe
# televisão de forma a receber o canal inicial em seu construtor
class televisao:
    def __init__(self,min,max,c0):
        self.ligada = False
        self.canal = c0
        self.tamanho = None
        self.marca = None
        self.cmin = min
        self.cmax = max
    def mudaCanalDiminui(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def mudaCanalAumenta(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = televisao(1,99,5)
print(tv.canal)

# Modifique a classe televisão de forma que, se pedirmos para mudar o canal para baixo,
# além do mínimo, ela vá para o canal máximo. Se mudarmos para cima, além do canal
# máximo, que volte ao canal mínimo
class televisao:
    def __init__(self,min,max,c0):
        self.ligada = False
        self.canal = c0
        self.tamanho = None
        self.marca = None
        self.cmin = min
        self.cmax = max
    def mudaCanalDiminui(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
    def mudaCanalAumenta(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv = televisao(1,10,1)
for x in range(0,20):
    print(tv.canal)
    tv.mudaCanalAumenta()

# utilizando o que aprendemos com funções, modifique o construtor da classe televisão
# de forma que min e max sejam parâmetros opcionais, onde min vale 2 e max vale 14,
# caso outro valor não seja passado
class televisao:
    def __init__(self,cmin = 2,cmax = 14):
        self.ligada = False
        self.canal = cmin
        self.tamanho = None
        self.marca = None
        self.cmin = cmin
        self.cmax = cmax
    def mudaCanalDiminui(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
    def mudaCanalAumenta(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv = televisao()
for x in range(0,20):
    print(tv.canal)
    tv.mudaCanalAumenta()

# Utilizando a classe televisão modificada no exercício anterior, crie duas instâncias,
# especificando o valor de min e max por nome
tvMin = televisao(5)
print('tvMin')
for x in range(0,20):
    print(tvMin.canal)
    tvMin.mudaCanalAumenta()
tvMax = televisao(2,19)
print('tvMax')
for x in range(0,20):
    print(tvMax.canal)
    tvMax.mudaCanalAumenta()

# TEORIA: Classe clientes / Exemplo de banco
class cliente:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

# Programa teste.py que importa a classe cliente do arquivo cliente.py
from cliente import cliente
joao = cliente("Joao da Silva","11987577806")
maria = cliente("Maria da Silva","11986677786")

# Altere o programa teste.py de forma a importar a classe conta. Crie uma conta
# correte para os clientes João e Maria

from cliente import cliente
from contas import conta

joao = cliente("Joao da Silva","11987577806")
maria = cliente("Maria da Silva","11986677786")

ccJoaoMaria = conta([joao,maria],'00001',2000)

ccJoaoMaria.resumo()
ccJoaoMaria.saque(1000)
ccJoaoMaria.resumo()
ccJoaoMaria.saque(50)
ccJoaoMaria.resumo()
ccJoaoMaria.deposito(200)
ccJoaoMaria.resumo()

# TEORIA: Conta com registro de operações e extrato
class conta:
    def __init__(self,clientes,numero,saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.opercacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: %s Saldo: %10.2f' % (self.numero,self.saldo))
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.opercacoes.append(['Saque',valor])
    def deposito(self,valor):
        self.saldo += valor
        self.opercacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        for o in self.opercacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

# Modifique o programa para imprimir o extrato das contas
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