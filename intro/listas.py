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