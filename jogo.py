import pygame
import time
import random


pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Nave Asteroides")

nave = pygame.image.load("nave.png")
larguraNave = 110
fundo = pygame.image.load("espaco.jpg")
missel = pygame.image.load("asteroide.png")
explosaoSound = pygame.mixer.Sound("explosao.mp3")
misselSound = pygame.mixer.Sound("som ast.mp3")
misselSound.set_volume(0.2)
def mostraNave(x, y):
    gameDisplay.blit(nave, (x, y))
def mostraMissel(x, y):
    gameDisplay.blit(missel, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Desvios:"+str(contador), True, white)
    gameDisplay.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    escreverTela("Fim de Jogo!")
def game():
    pygame.mixer.music.load("som esp.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    navePosicaoX = largura*0.42
    navePosicaoY = altura*0.8
    movimentoX = 0
    velocidade = 20
    misselAltura = 250
    misselLargura = 200
    misselVelocidade = 3
    misselX = random.randrange(0, largura)
    misselY = -200
    desvios = 0
    pygame.mixer.Sound.play(misselSound)
    
    
    while True:
       
        acoes = pygame.event.get()  
       
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (1, 1))
        
        escreverPlacar(desvios)
        misselY = misselY + misselVelocidade
        mostraMissel(misselX, misselY)
        if misselY > altura:
            misselY = -200
            misselX = random.randrange(0, largura)
            desvios = desvios+1
            misselVelocidade += 3
            pygame.mixer.Sound.play(misselSound)
        navePosicaoX += movimentoX
        if navePosicaoX < 0:
            navePosicaoX = 0
        elif navePosicaoX > largura-larguraNave:
            navePosicaoX = largura-larguraNave
        
        if navePosicaoY < misselY + misselAltura:
            if navePosicaoX < misselX and navePosicaoX+larguraNave > misselX or misselX+misselLargura > navePosicaoX and misselX+misselLargura < navePosicaoX+larguraNave:
                dead()
        
        mostraNave(navePosicaoX, navePosicaoY)
        pygame.display.update()
        clock.tick(60)  
game()
