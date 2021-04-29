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
