import requests
import random
import time
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
resposta = requests.get(url)
palavras = resposta.content.splitlines()
palavras = [palavra.decode('utf-8') for palavra in palavras]
random_palavras = random.sample(palavras, 10)# print(random_palavras)
pontos = 0
tic = time.perf_counter()
for palavra in random_palavras:
    print(palavra)
    entrada = input()
    if entrada == palavra:
        pontos = pontos + 1
toc = time.perf_counter()
print(pontos)
print(toc-tic)