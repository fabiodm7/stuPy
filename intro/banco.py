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