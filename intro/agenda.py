import sys
import pickle
from functools import total_ordering

def nulo_ou_vazio(texto):
    return texto == None or not texto.strip()

def valida_faixa_inteiro(pergunta,inicio,fim,padra = None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao != None:
                entrada = padrao
            valor = int(entrada)
            if inicio <= valor <= fim:
                return (valor)
        except ValueError:
            print('Valor inválido, favor digitar entre %d e %d' % (inicio,fim))

def valida_faixa_inteiro_ou_branco(pergunta,inicio,fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print('Valor inválido, favor digitar entre %d e %d' % (inicio,fim))

class ListaUnica:
    def __init__(self,elem_class):
        self.lista = []
        self.elem_class = elem_class
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
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1
    def verifica_tipo(self,elem):
        if type(elem) != self.elem_class:
            raise TypeError('Tipo inválido')
    def ordena(self,chave = None):
        self.lista.sort(key=chave)

@total_ordering
class Nome:
    def __init__(self,nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    def __repr__(self):
        return ''