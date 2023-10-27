import pygame 
from constantes import largura_tela, altura_tela
from game_loop import *


class Background(pygame.sprite.Sprite):
    
    def __init__(self, imagem):
        self.surface_background = pygame.image.load(imagem)
        self.surface_background = pygame.transform.scale(self.surface_background, (largura_tela, altura_tela))
        self.rect_background_esquerda = self.surface_background.get_rect(topleft=(0, 0))
        self.rect_background_direita = self.surface_background.get_rect(topleft=(largura_tela, 0))
        pygame.sprite.Sprite.__init__(self)

    def movimenta_background(self, state):
        
        self.rect_background_esquerda.x -= state ["velocidade_tela"]
        self.rect_background_direita.x -= state ["velocidade_tela"] 

        if self.rect_background_esquerda.x <= -largura_tela:
            self.rect_background_esquerda.x = largura_tela
        if self.rect_background_direita.x <= -largura_tela:
            self.rect_background_direita.x = largura_tela

    def desenha_background(self, window):
        window.blit(self.surface_background, self.rect_background_esquerda)
        window.blit(self.surface_background, self.rect_background_direita)