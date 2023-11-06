import pygame 
from constantes import largura_tela, altura_tela 
import random 


"""
Classe que representa o item de ganhar vidas, ou seja, os corações
"""

class item_coracao (pygame.sprite.Sprite):

    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = (pygame.transform.scale (pygame.image.load('sprite_coracao.png'), (60, 40)))
        self.rect = self.image.get_rect()
        
        self.rect.x = largura_tela
        self.rect.y = random.randint(self.rect.height + 50, altura_tela - self.rect.height - 100)


    """
    Função que desenha o item na tela
    """

    def desenha_itemcoracao (self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    """
    Função que reseta a posição do item, caso ele surja na mesma posição um obstaculo
    """
    def reset_posicao_coracao(self):
        self.rect.x = largura_tela + random.randint (100, 600)  
        max_y = altura_tela - self.rect.height - 100
        self.rect.y = random.randint(300, max_y)

    """
    Função que adiciona a vida ao grupo de itens de vida do jogo, assim o validando
    """

    def adiciona_itens_coracao (self, state):

        while pygame.sprite.spritecollideany(self, state["grupo_obstacles"]) != None or pygame.sprite.spritecollideany(self, state ["grupo_itens"]) != None:
            self.reset_posicao_coracao()
        
        state ["grupo_coracao"].add(self)