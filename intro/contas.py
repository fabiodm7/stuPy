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