import pygame 
import random
from game_loop import *

class Obstacle(pygame.sprite.Sprite):
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

        self.rect = self.obstacle_type[self.current_frame].get_rect(x=largura_tela + random.randint (0,900), y=random.randint(0, altura_tela - self.obstacle_type[self.current_frame].get_height()))
    def movimenta_e_anima_obstacle(self, state):

        self.animation_counter += 1
        
        if self.animation_counter == self.animation_interval:
            self.current_frame = (self.current_frame + 1) % len(self.obstacle_type)
            self.animation_counter = 0
        
        self.rect.x -= state ["velocidade_tela"]

    def reset_posicao(self):
        self.rect.x = largura_tela + random.randint (0, 600)  
        max_y = altura_tela - self.rect.height
        self.rect.y = random.randint(300, max_y)

    def adiciona_obstacles (self, state):

        while pygame.sprite.spritecollideany(self, state["grupo_obstacles"]) != None:
            self.reset_posicao()
        
        state ["grupo_obstacles"].add(self)
        
        
    def desenha_obstacles(self, window):

        window.blit(self.obstacle_type[self.current_frame], (self.rect.x, self.rect.y))
