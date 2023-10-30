import pygame
from random import randint
# from pygame.locals import *
# import sys

pygame.init()



# Declaração de variaveis
# cordenadas do carro amarelo
# valor maximo 545 e valor minimo 215
x = 375  
# cordenadas do carro amarelo
y = 100

# Posição dos objetos na tela
pos_x = 240
pos_y = 240

# Posição 2  dos objetos na tela
pos_y_car_ambulanc = 800
pos_y_car_polic = 800
pos_y_car_vermelho = 800

# Velocidade dos veiculos
velocidade = 10
velocidade_outros_veic = 6

# Timer do cronometro na tela
time = 0
tempo_segundos = 0

pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('musica/som_tela.mp3')
pygame.mixer.music.play()

musica_de_colisao = pygame.mixer.Sound('musica/colisao.wav')
# pygame.mixer.music.play(1)

fundo = pygame.image.load('./Imagens/asfalto.png')
car_amarelo = pygame.image.load('./Imagens/car_amarelo.png')
car_vermelho = pygame.image.load('./Imagens/car_vermelho.png')
car_polic = pygame.image.load('./Imagens/car_polic.png')
car_ambulanc = pygame.image.load('./Imagens/car_ambulanc.png')
batida = pygame.image.load('./Imagens/batida.png')

# Inserindo um timer na esquenda da tela
font = pygame.font.SysFont('arial black', 25)
texto = font.render("Tempo:", True, (255, 255, 255), (0, 30, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)


# Definir o tamanho da janela
janela = pygame.display.set_mode((800, 600))
# Define o nome na janela do jogo
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
    if comandos[pygame.K_RIGHT] and x <= 540:
        x += velocidade

    # Se atecla seta para esquerda for clicada
    if comandos[pygame.K_LEFT] and x >= 215:
        x -= velocidade

    # ********* Linha correspondente a colisão dos carros *******************
    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_car_ambulanc)) and ((x - 80 < pos_x - 136 and y + 180 > pos_y_car_ambulanc)):
        y = 1200
    
    if (pos_y_car_ambulanc <= -80):
        pos_y_car_ambulanc = randint(800, 1000)
        musica_de_colisao.play()   
            
    if (pos_y_car_polic <= -80):
        pos_y_car_polic = randint(1200, 2000)
        
    if (pos_y_car_vermelho <= -80):
        pos_y_car_vermelho = randint(2200, 3000)

    # Linha referente ao Timer
    if (time < 20):
        time += 1
    else:
        tempo_segundos += 1
        texto = font.render("Tempo:" + str(tempo_segundos), True, (255, 255, 255), (0, 30, 0))
        time = 0

    # Linha referente a velocidade dos 3 carros
    # Carro da ambulancia
    pos_y_car_ambulanc -= velocidade_outros_veic + 1
    
    # Carro da policia
    pos_y_car_polic -= velocidade_outros_veic + 6 

    # Carro dvermelho
    pos_y_car_vermelho -= velocidade_outros_veic + 5 
    # if (pos_y <= -200):
    #    pos_y = 600


    # importa a imagem do fundo
    janela.blit(fundo, (0, 0))

    # Criar um objeto Car_amarelo na tela
    janela.blit(car_amarelo, (x, y))

    # Criar um objeto Car_ambulanc na tela
    janela.blit(car_ambulanc, (pos_x + 140, pos_y_car_ambulanc))

    # Criar um objeto Car_polic na tela
    janela.blit(car_polic, (pos_x, pos_y_car_polic))

    # Criar um objeto Car_vermelho na tela
    janela.blit(car_vermelho, (pos_x + 260, pos_y_car_vermelho))

    # Criar um objeto texto time  na tela
    janela.blit(texto, pos_texto)

    # Preenche o espaço do circulo com cor neltra preto
    # Criar um objeto na tela um circulo
    # pygame.draw.circle(janela,(0, 255, 0), (x, y), 50)

    # Atualiza atela depois de feito o desenho
    pygame.display.update()

pygame.quit()
