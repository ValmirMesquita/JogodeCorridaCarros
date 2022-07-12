import pygame
from random import randint
pygame.init()
from pygame.locals import *
import  sys

# Declaração de variaveis
# cordenadas do carro amarelo
x = 375  # valor maximo 545 e valor minimo 200
# cordenadas do carro amarelo
y = 175

# Posição dos objetos na tela
pos_x = 240
pos_y_car_ambulanc = 800

# Posição 2  dos objetos na tela
pos_y_car_polic = 800
pos_y_car_vermelho = 800


velocidade = 10
velocidade_outros_veic = 10

fundo = pygame.image.load('./Imagens/asfalto.png')
car_amarelo = pygame.image.load('./Imagens/car_amarelo.png')
car_vermelho = pygame.image.load('./Imagens/car_vermelho.png')
car_polic = pygame.image.load('./Imagens/car_polic.png')
car_ambulanc = pygame.image.load('./Imagens/car_ambulanc.png')

# Definir o tamanho da janela
janela = pygame.display.set_mode((800, 600))
#Define o nome na janela do jogo
pygame.display.set_caption("Jogo de corrida Duda e Leleti")

# Linha correspondente ao abrir e fechar tela
janela_aberta = True
while janela_aberta:
    # Tempo de delay para imagem na tela
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Cria os comandos de movimentos do objeto na tela
    # Quando for precionado um tecla
    comandos = pygame.key.get_pressed()

    # Se atecla seta para cima for clicada
    if comandos[pygame.K_UP]:
        y -= velocidade

    # Se atecla seta para Baixo for clicada
    if comandos[pygame.K_DOWN]:
        y += velocidade

    # Se atecla seta para direita for clicada
    if comandos[pygame.K_RIGHT]:
        x += velocidade

    # Se atecla seta para esquerda for clicada
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    if (pos_y_car_ambulanc  <= -180) and (pos_y_car_polic <= -180) and (pos_y_car_vermelho <= -180):
        pos_y_car_ambulanc  = randint(800,2000)
        pos_y_car_polic = randint(800,2000)
        pos_y_car_vermelho = randint(800,2000)

    pos_y_car_ambulanc -= velocidade_outros_veic
    pos_y_car_polic -= velocidade_outros_veic + 6 # Carro da policia
    pos_y_car_vermelho -= velocidade_outros_veic + 5 # Carro dvermelho
    # if (pos_y <= -200):
    #    pos_y = 600


    # importa a imagem do fundo
    janela.blit(fundo,(0,0))

    # Criar um objeto Car_amarelo na tela
    janela.blit(car_amarelo,(x, y))

    # Criar um objeto Car_ambulanc na tela
    janela.blit(car_ambulanc, (pos_x + 140, pos_y_car_ambulanc ))

    # Criar um objeto Car_polic na tela
    janela.blit(car_polic, (pos_x, pos_y_car_polic ))

    # Criar um objeto Car_vermelho na tela
    janela.blit(car_vermelho, (pos_x +260, pos_y_car_vermelho))


    # Preenche o espaço do circulo com cor neltra preto
    # Criar um objeto na tela um circulo
    # pygame.draw.circle(janela,(0, 255, 0), (x, y), 50)

    # Atualiza atela depois de feito o desenho
    pygame.display.update()



pygame.quit()
