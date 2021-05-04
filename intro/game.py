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

# Cobra
import pygame
import random

pygame.init()
pygame.display.init()
pygame.font.init()

azul = (50, 100, 213)
laranja = (205, 102, 0)
verde = (0, 255, 0)
amarelo = (255,255,102)

dimensoes = (600, 600)

### VALORES INICIAIS ###
x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20

# fonte = pygame.font.Font(None,35)

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
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])    
    
    return x_comida, y_comida, lista_cobra

def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        raise Exception

def verifica_mordeu(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]
    for x,y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception

def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra)-1)
    escore = fonte.render("Pontuação: " + pts, True, amarelo)
    tela.blit(score,[1,1])

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(
        dx, dy, x_comida, y_comida, lista_cobra)
    print(lista_cobra)    
    verifica_parede(lista_cobra)
    verifica_mordeu(lista_cobra)
    # atualizar_pontos(lista_cobra)

    clock.tick(12)
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

scoreFont = pygame.font.SysFont('/usr/share/fonts/truetype/freefont/FreeSans.ttf',35)

player = pygame.image.load('/home/fdmedina/Imagens/Crop Captura de tela de 2021-04-23 20-32-17.png')

playerRect = player.get_rect()

charSpeed = [speed,speed]

def verifyGameBounds(positionX,positionY):
    if positionY > (disHeight - squareSize):
        positionY = disHeight - squareSize
    if positionY < 0:
        positionY = 0
    if positionX > (disWidth - squareSize):
        positionX = disWidth - squareSize
    if positionX < 0:
        positionX = 0

    return (positionX,positionY)

def gameLoop():
    gameOver = False

    # posição inicial
    positionX = disWidth / 2
    positionY = disHeight / 2

    # # usaremos para controlar a movimentação
    x1Change = 0
    y1Change = 0
    
    score = 100

    while not gameOver:
        displayScore(score)
        pygame.display.update()

        # # usaremos para controlar a movimentação
        # x1Change = 0
        # y1Change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1Change = -speed
                    y1Change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1Change = speed
                    y1Change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1Change = 0
                    y1Change = -speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1Change = 0
                    y1Change = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y1Change = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_a:
                    x1Change = 0

        dis.fill(black)

        pygame.draw.rect(dis, red, [positionX,positionY,squareSize,squareSize])

        positionX += x1Change
        positionY += y1Change

        positionX,positionY = verifyGameBounds(positionX,positionY)
        # utilizando o speed para alterar o posicionamento do retangulo
        # positionY += speed

        pygame.display.update()

        # definindo para ser 10 frames por segundo no maximo
        clock.tick(speed)
    
    pygame.quit()

def displayScore(score):
    msgScore = scoreFont.render('Your score: ' + str(score),True,yellow)
    dis.blit(msgScore,[0,0])
# chamamos a função para executar o nosso gameLoop
gameLoop()
'''