import pygame 
from constantes import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        self.surface_player = pygame.Surface((25, 50))
        self.surface_player.fill((0, 255, 0))
        self.rect_player = self.surface_player.get_rect(x=largura_tela * 0.1, y=altura_tela * 0.5)
        self.velocidade_vertical = 0
        self.impulso = 3
        self.gravidade = 0.1

    def movimenta_player(self):
        
        tecla_apertada = pygame.key.get_pressed()

        if tecla_apertada[pygame.K_SPACE]:
            self.velocidade_vertical = -self.impulso
        else:
            self.velocidade_vertical += self.gravidade

        self.rect_player.y += self.velocidade_vertical

        # Limite superior
        if self.rect_player.y < 0:
            self.rect_player.y = 0
            self.velocidade_vertical = 0

        # Limite inferior
        if self.rect_player.y > altura_chao - self.rect_player.height:
            self.rect_player.y = altura_chao - self.rect_player.height
            self.velocidade_vertical = 0

            if tecla_apertada[pygame.K_SPACE]:
                self.velocidade_vertical = -self.impulso


    def desenha_player(self, window):
        window.blit(self.surface_player, self.rect_player)