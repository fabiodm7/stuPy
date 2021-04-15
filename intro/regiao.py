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