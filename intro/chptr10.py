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
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: %s Saldo: %10.2f' % (self.numero,self.saldo))
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque',valor])
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        for o in self.operacoes:
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

# Altere o programa de forma que a mensagem saldo insuficiente seja exibida caso
# haja tentativa de sacar mais dinheiro que o saldo disponível
class conta:
    def __init__(self,clientes,numero,saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: %s Saldo: %10.2f' % (self.numero,self.saldo))
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque',valor])
        else:
            print('Saldo insuficiente! Saldo atual: %10.2f' % self.saldo)
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

# Modifique o método classe Conta para exibir o nome e telefone de cada cliente
class conta:
    def __init__(self,clientes,numero,saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: %s Saldo: %10.2f' % (self.numero,self.saldo))
        # if len(self.clientes) > 1:
        for i in self.clientes:
            print('Cliente: %s Contato: %s' % (i.nome,i.telefone))
        # else:
        #     print('Cliente: %s Contato: %s' % (self.clientes.nome,self.clientes.telefone))
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque',valor])
        else:
            print('Saldo insuficiente! Saldo atual: %10.2f' % self.saldo)
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        self.resumo()
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

# Crie uma nova conta, agora tendo João e José como clientes e saldo igual a 500
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

# TEORIA: Classe banco
class banco:
    def __init__(self,nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
    def abreConta(self,conta):
        self.contas.append(conta)
    def listaContas(self):
        for c in self.contas:
            c.resumo()

# TEORIA: Criando objetos
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

# Crie classes para representar estados e cidades. Cada estado tem um nome, sigla 
# e cidades. Cada cidade tem nome e população. Escreva um programa de testes que crie 
# três estados com algumas cidades em cada um. Exiba a população de cada estado como 
# a soma da população de suas cidades.

# região.py
class estado:
    def __init__(self,nome,sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        self.populacao = 0
    def totalPop(self):
        for c in self.cidades:
            self.populacao += c.populacao
    def novaCidade(self,cidade):
        for c in cidade:
            self.cidades.append(c)
        self.totalPop()
    def resumo(self):
        print('Estado: %s\nSigla: %s\nHabitantes: %d' % (self.nome,self.sigla,self.populacao))
        print('Cidades:')
        for c in self.cidades:
            print('%s | %d' % (c.nome,c.populacao))

class cidade:
    def __init__(self,nome,populacao,siglaEstado):
        self.nome = nome
        self.populacao = populacao
        self.siglaEstado = siglaEstado

# teste.py
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

# TEORIA: Uso de herança para definir Conta Especial
class contaEspecial(conta):
    def __init__(self,clientes,numero,saldo=0,limite=0):
        conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque: ',valor])

# TEORIA: Criação e uso de uma ContaEspecial
from cliente import cliente
from contas import conta, contaEspecial
joao = cliente('Joao da Silva','777-1234')
maria = cliente('Maria da Silva','555-4321')
conta1 = conta([joao],1,1000)
conta2 = contaEspecial([maria,joao],2,500,1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()

# Modifique as classes Conta e ContaEspecial para que a operação de saque retorne
# verdadeiro se o saque foi efetuado e falso em caso contrário
class conta:
    def __init__(self,clientes,numero,saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: %s Saldo: %10.2f' % (self.numero,self.saldo))
        # if len(self.clientes) > 1:
        for i in self.clientes:
            print('Cliente: %s Contato: %s' % (i.nome,i.telefone))
        # else:
        #     print('Cliente: %s Contato: %s' % (self.clientes.nome,self.clientes.telefone))
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque',valor])
            return True
        else:
            print('Saldo insuficiente! Saldo atual: %10.2f' % self.saldo)
            return False
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        self.resumo()
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

# Altere a classe contaEspecial de forma que seu extrato exiba o limite e o total 
# disponível para saque
class contaEspecial(conta):
    def __init__(self,clientes,numero,saldo=0,limite=0):
        conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque: ',valor])
            return True
        else:
            print('Valor excede o limite de %10.2f! Saldo atual: %10.2f' % ((self.limite*-1),self.saldo))
            return False

class contaEspecial(conta):
    def __init__(self,clientes,numero,saldo=0,limite=0):
        conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque: ',valor])
            return True
        else:
            print('Valor excede o limite de %10.2f! Saldo atual: %10.2f' % ((self.limite*-1),self.saldo))
            return False
    def resumo(self):
        print('CC número: %s Saldo: %10.2f Limite: %10.2f' % (self.numero,self.saldo,(self.limite*-1)))
        # if len(self.clientes) > 1:
        for i in self.clientes:
            print('Cliente: %s Contato: %s' % (i.nome,i.telefone))
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        self.resumo()
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

# Observe o método saque das classes conta e contaEspecial. Modifique o método saque da
# classe conta de forma que a verificação da possibilidade de saque seja feita por um
# novo método, substituindo a condição atual. Esse novo método retornará verdadeiro se o
# o saque puder ser efetuado, e falso em caso contrário. Modifique a classe contaEspecial
# de forma a trabalhar com esse novo método. Verifique se você ainda precisa trocar o
# método saque de contaEspecial ou apenas o novo método criado para verificar a
# possibilidade de saque
class conta:
    def __init__(self,clientes,numero,saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: %s Saldo: %10.2f' % (self.numero,self.saldo))
        # if len(self.clientes) > 1:
        for i in self.clientes:
            print('Cliente: %s Contato: %s' % (i.nome,i.telefone))
        # else:
        #     print('Cliente: %s Contato: %s' % (self.clientes.nome,self.clientes.telefone))
    def temSaldo(self,valor):
        if self.saldo >= valor:
            return True
        else: return False
    def saque(self,valor):
        if self.temSaldo(valor): # self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque',valor])
            return True
        else:
            print('Saldo insuficiente! Saldo atual: %10.2f' % self.saldo)
            return False
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        self.resumo()
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

class contaEspecial(conta):
    def __init__(self,clientes,numero,saldo=0,limite=0):
        conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    def temSaldo(self,valor):
        if self.saldo + self.limite >= valor:
            return True
        else: return False
    def saque(self,valor):
        if self.temSaldo(valor): # self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque: ',valor])
            return True
        else:
            print('Valor excede o limite de %10.2f! Saldo atual: %10.2f' % ((self.limite*-1),self.saldo))
            return False
    def resumo(self):
        print('CC número: %s Saldo: %10.2f Limite: %10.2f' % (self.numero,self.saldo,(self.limite*-1)))
        # if len(self.clientes) > 1:
        for i in self.clientes:
            print('Cliente: %s Contato: %s' % (i.nome,i.telefone))
    def extrato(self):
        print('Extrato CC No.: %s\n' % self.numero)
        self.resumo()
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0],o[1]))
        print('\n    Saldo: %10.2f\n' % self.saldo)

# TEORIA: Classe listaUnica (listas.py)
class listaUnica:
    def __init__(self,elemClass):
        self.lista = []
        self.elemClass = elemClass
    def __len__(self):
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem__(self,p):
        return self.lista[p]
    def indiceValido(self,i):
        return i >= 0 and i < len(self.lista)
    def adiciona(self,elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)
    def remove(self,elem):
        self.lista.remove(elem)
    def pesquisa(self,elem):
        self.verificaTipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1
    def verificaTipo(self,elem):
        if type(elem) != self.elemClass:
            raise TypeError('Tipo inválido')
    def ordena(self,chave = None):
        self.lista.sort(key = chave)

# TEORIA: Classe nome(nomes.py)
class nome:
    def __init__(self,nome):
        if nome == None or not nome.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return '<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>'.format(id(self),self.nome,self.chave,type(self).__name__)
    def __eq__(self,outro):
        print('__eq__ Chamado')
        return self.nome == outro.nome
    def __lt__(self,outro):
        print('__lt__ Chamado')
        return self.nome < outro.nome

# TEORIA: Usando anotações(nomes.py)
from functools import total_ordering

@total_ordering

class Nome:
    def __init__(self,nome):
        if nome == None or not nome.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.nome = nome
        self.chave = Nome.criaChave(nome) #nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return '<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>'.format(id(self),self.nome,self.chave,type(self).__name__)
    def __eq__(self,outro):
        print('__eq__ Chamado')
        return self.nome == outro.nome
    def __lt__(self,outro):
        print('__lt__ Chamado')
        return self.nome < outro.nome
    @staticmethod
    def criaChave(nome):
        return nome.strip().lower()

# TEORIA: Classe Nome com propriedades(nome.py)
from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self,nome):
        # if nome == None or not nome.strip():
        #     raise ValueError('Nome não pode ser nulo nem em branco')
        self.nome = nome
        # self.chave = Nome.criaChave(nome) #nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return '<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>'.format(id(self),self.__nome,self.__chave,type(self).__name__)
    def __eq__(self,outro):
        print('__eq__ Chamado')
        return self.nome == outro.nome
    def __lt__(self,outro):
        print('__lt__ Chamado')
        return self.nome < outro.nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,valor):
        if valor == None or not valor.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.criaChave(valor)
    @staticmethod
    def criaChave(nome):
        return nome.strip().lower()

# TEORIA: Chave como propriedade apenas para leitura (nome.py)
from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self,nome):
        # if nome == None or not nome.strip():
        #     raise ValueError('Nome não pode ser nulo nem em branco')
        self.nome = nome
        # self.chave = Nome.criaChave(nome) #nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return '<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>'.format(id(self),self.__nome,self.__chave,type(self).__name__)
    def __eq__(self,outro):
        print('__eq__ Chamado')
        return self.nome == outro.nome
    def __lt__(self,outro):
        print('__lt__ Chamado')
        return self.nome < outro.nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,valor):
        if valor == None or not valor.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.criaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def criaChave(nome):
        return nome.strip().lower()
'''