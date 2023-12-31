import pygame 
import random
from game_loop import *


"""
classe que representa os obstáculos
"""


class Obstacle(pygame.sprite.Sprite):
    
    """
    Construtor da classe, definição de variáveis e inicialização de sprites
    """

    def __init__(self):
        self.sprite_obstacle_type_1 = []
        self.sprite_obstacle_type_2 = []

        
        self.sprite_obstacle_type_1.append(pygame.image.load('sprite/Snapshot.PNG'))
        self.sprite_obstacle_type_1.append(pygame.image.load(f'sprite/Snapshot_1.PNG'))
        self.sprite_obstacle_type_1.append(pygame.image.load(f'sprite/Snapshot_2.PNG'))
        self.sprite_obstacle_type_1.append(pygame.image.load(f'sprite/Snapshot_3.PNG'))
        self.sprite_obstacle_type_1.append(pygame.image.load(f'sprite/Snapshot_4.PNG'))
        self.sprite_obstacle_type_1.append(pygame.image.load(f'sprite/Snapshot_5.PNG'))
        self.sprite_obstacle_type_1.append(pygame.image.load(f'sprite/Snapshot_6.PNG'))
        
        self.sprite_obstacle_type_2.append(pygame.image.load(f'sprite/Snapshot_7.PNG'))
        self.sprite_obstacle_type_2.append(pygame.image.load(f'sprite/Snapshot_8.PNG'))
        self.sprite_obstacle_type_2.append(pygame.image.load(f'sprite/Snapshot_9.PNG'))
        self.sprite_obstacle_type_2.append(pygame.image.load(f'sprite/Snapshot_10.PNG'))
        self.sprite_obstacle_type_2.append(pygame.image.load(f'sprite/Snapshot_11.PNG'))
        self.sprite_obstacle_type_2.append(pygame.image.load(f'sprite/Snapshot_12.PNG'))
        

        self.obstacle_type = random.choice([self.sprite_obstacle_type_1, self.sprite_obstacle_type_2]) 
        self.current_frame = 0

        self.animation_interval = 7
        self.animation_counter = 0

        pygame.sprite.Sprite.__init__(self)

        self.rect = self.obstacle_type[self.current_frame].get_rect(x=largura_tela + random.randint (100,900), y=random.randint(0, altura_tela - 20 - self.obstacle_type[self.current_frame].get_height()))
    

    """
    Função que movimenta e anima o obstáculo
    """

    def movimenta_e_anima_obstacle(self, state):

        self.animation_counter += 1
        
        if self.animation_counter == self.animation_interval:
            self.current_frame = (self.current_frame + 1) % len(self.obstacle_type)
            self.animation_counter = 0
        
        self.rect.x -= state ["velocidade_tela"]


    """
    Função que reseta a posição do obstáculo, caso ele surja na mesma posição que outro
    """
    def reset_posicao(self):
        self.rect.x = largura_tela + random.randint (100, 600)  
        max_y = altura_tela - self.rect.height - 20
        self.rect.y = random.randint(300, max_y)

    """
    Função que adiciona o obstáculo ao grupo de obstáculos do jogo, assim o validando
    """

    def adiciona_obstacles (self, state):

        while pygame.sprite.spritecollideany(self, state["grupo_obstacles"]) != None:
            self.reset_posicao()
        
        state ["grupo_obstacles"].add(self)
   
        
    """
    Função que desenha o obstáculo na tela
    """
    def desenha_obstacles(self, window):

        window.blit(self.obstacle_type[self.current_frame], (self.rect.x, self.rect.y))