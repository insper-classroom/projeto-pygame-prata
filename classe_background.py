import pygame 
from constantes import largura_tela, altura_tela, MUDANCA_BACKGROUND
from game_loop import *

"""
classe que representa o background
"""
class Background(pygame.sprite.Sprite):
    
    """
    Construtor da classe, definição de variáveis e inicialização de sprites
    """

    def __init__(self, imagem, imagem2):

        self.surface_background = pygame.image.load(imagem)
        self.surface_background = pygame.transform.scale(self.surface_background, (largura_tela, altura_tela))

        self.surface_background2 = pygame.image.load(imagem2)
        self.surface_background2 = pygame.transform.scale(self.surface_background2, (largura_tela, altura_tela))


        self.rect_background_esquerda = self.surface_background.get_rect(topleft=(0, 0))
        self.rect_background_direita = self.surface_background.get_rect(topleft=(largura_tela, 0))

        self.rect_background_esquerda2 = self.surface_background2.get_rect(topleft=(0, 0))
        self.rect_background_direita2 = self.surface_background2.get_rect(topleft=(largura_tela, 0))


        pygame.sprite.Sprite.__init__(self)


    """
    Função que movimenta o background de acordo com a velocidade da tela e muda ele de acordo com a distância percorrida
    """

    def movimenta_background(self, state):
        
        self.rect_background_esquerda.x -= state ["velocidade_tela"]
        self.rect_background_direita.x -= state ["velocidade_tela"]

        self.rect_background_esquerda2.x -= state ["velocidade_tela"]
        self.rect_background_direita2.x -= state ["velocidade_tela"]

        if self.rect_background_esquerda.x <= -largura_tela:
            self.rect_background_esquerda.x = largura_tela
        
        if self.rect_background_direita.x <= -largura_tela:
            self.rect_background_direita.x = largura_tela

        if self.rect_background_esquerda2.x <= -largura_tela:
            self.rect_background_esquerda2.x = largura_tela
        
        if self.rect_background_direita2.x <= -largura_tela:
            self.rect_background_direita2.x = largura_tela
        
        
    """
    Função que desenha o background (este sendo diferente dependendo da distância percorrida)
    """
    
    def desenha_background(self, window, state):
        
        if state ["distancia_percorrida"] < MUDANCA_BACKGROUND:
            window.blit(self.surface_background, (self.rect_background_esquerda.x, self.rect_background_esquerda.y))
            window.blit(self.surface_background, (self.rect_background_direita.x, self.rect_background_direita.y))

        elif state ["distancia_percorrida"] == MUDANCA_BACKGROUND:
            window.fill ((255,255,255))

        else:
            window.blit(self.surface_background2, (self.rect_background_esquerda2.x, self.rect_background_esquerda2.y))
            window.blit(self.surface_background2, (self.rect_background_direita2.x, self.rect_background_direita2.y))