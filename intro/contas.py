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