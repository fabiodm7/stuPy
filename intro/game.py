# TEORIA:
'''
# importa o pygame
import pygame

# inicializa o modulo do pygame
pygame.init()

# definindo o tamanho da tela para o Pygame
dis_width = 600 # largura
dis_height = 400 # altura

dis = pygame.display.set_mode((dis_width,dis_height))

red = (219, 31, 31)
green = (44, 219, 31)

squareSize = 20
circleRadius = 10

positionX = 200
positionY = 100

# definindo um título que irá aparecer na janela
pygame.display.set_caption('Primeiro jogo')

# função que será o loop do jogo a ser desenvolvido
def gameLoop():
    gameOver = False

    while not gameOver:
        pygame.display.update()
        # captura as teclas que foram pressionadas
        for event in pygame.event.get():
            # verifica se o evento foi um evento para finalizar
            if event.type == pygame.QUIT:
                # marcamos que o jogo foi finalizado para sari do loop
                gameOver = True
        
        # desenha um retangulo
        pygame.draw.rect(dis,red,[positionX,positionY,squareSize,squareSize])
        # desenha um circulo
        pygame.draw.circle(dis,green,(positionX+200,positionY),circleRadius)
        
    # saindo do jogo
    pygame.quit()
    
    # # loop principal que ira rodar o jogo
    # while True:
    #     continue

# chamamos a função para executar o nosso gameLoop
gameLoop()
'''
'''
# Cobra
import pygame
import random

azul = (50, 100, 213)
laranja = (205, 102, 0)
verde = (0, 255, 0)

dimensoes = (600, 600)### VALORES INICIAIS ###

x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake da Kenzie')

tela.fill(azul)

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])

def mover_cobra(dx, dy, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
                
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy
    
    lista_cobra.append([x_novo, y_novo])
    
    del lista_cobra[0]
    
    return dx, dy, lista_cobra

def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]
    
    x_novo = head[0] + dx
    y_novo = head[1] + dy    
    
    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])    
    
    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])    
    
    return x_comida, y_comida, lista_cobra

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(
        dx, dy, x_comida, y_comida, lista_cobra)
    print(lista_cobra)    

    clock.tick(20)
'''
# TEORIA
import pygame
red = (219,31,31)
black = (0,0,0)

squareSize = 20

# vai ser utilizado para determinar quantos frames por segundo
clock = pygame.time.Clock()

# velocidade que o nosso desenha irá se mover
speed = 10

disWidth = 600
disHeight = 400

dis = pygame.display.set_mode((disWidth,disHeight))

pygame.display.set_caption('Meu jogo')

def gameLoop():
    gameOver = False

    # posição inicial
    positionX = disWidth/2
    positionY = 0

    while not gameOver:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
        
        dis.fill(black)

        pygame.draw.rect(dis, red, [positionX,positionY,squareSize,squareSize])

        # utilizando o speed para alterar o posicionamento do retangulo
        positionY += speed

        if positionY > (disHeight - squareSize):
            positionY = disHeight - squareSize
        if positionY < 0:
            positionY = 0
        if positionX > (disWidth - squareSize):
            positionX = disWidth - squareSize
        if positionX < 0:
            positionX = 0

        pygame.display.update()

        # definindo para ser 10 frames por segundo no maximo
        clock.tick(speed)
    
    pygame.quit()

# chamamos a função para executar o nosso gameLoop
gameLoop()