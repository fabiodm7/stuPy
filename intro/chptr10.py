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
'''