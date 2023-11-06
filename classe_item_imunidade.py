import pygame 
from constantes import largura_tela, altura_tela 
import random 


"""
Classe que representa o item de imunidade
"""

class item_imunidade (pygame.sprite.Sprite):

    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('item_imunidade.png')
        self.rect = self.image.get_rect()

        self.rect.x = largura_tela
        self.rect.y = random.randint(300, altura_tela - self.rect.height)


    """
    Função que desenha o item na tela
    """

    def desenha_item (self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    """
    Função que reseta a posição do item, caso ele surja na mesma posição um obstaculo
    """
    def reset_posicao(self):
        self.rect.x = largura_tela + random.randint (100, 600)  
        max_y = altura_tela - self.rect.height - 100
        self.rect.y = random.randint(300, max_y)

    """
    Função que adiciona o item  ao grupo de itens do jogo, assim o validando
    """

    def adiciona_itens (self, state):

        while pygame.sprite.spritecollideany(self, state["grupo_obstacles"]) != None:
            self.reset_posicao()
        
        state ["grupo_itens"].add(self)