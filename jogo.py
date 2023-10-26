import pygame
from constantes import *
import random

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('LabRun')
    player = Player() 
    background_imagem = Background('background.png') 
    obstacles = [Obstacle() for _ in range(10)]
    state = {'player': player, 'background' : background_imagem, 'obstacles' : obstacles}

    return window, state

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite_obstacle_type_1 = []
        self.sprite_obstacle_type_2 = []
        # self.sprite_obstacle_type_3 = []

        
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
        
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_13.PNG'))
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_14.PNG'))
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_15.PNG'))
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_16.PNG'))
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_17.PNG'))
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_18.PNG'))
        # self.sprite_obstacle_type_3.append(pygame.image.load(f'sprite/Snapshot_19.PNG'))

        self.obstacle_type = random.choice([self.sprite_obstacle_type_1, self.sprite_obstacle_type_2])
        self.current_frame = 0

        self.rect = self.obstacle_type[self.current_frame].get_rect(x=largura_tela + 50, y=altura_tela * 0.5)

    def move_obstacle(self):
        # self.rect_obstacle.x -= velocidade_tela
        # if self.rect_obstacle.right < 0:
            # self.rect_obstacle.x = random.randint (largura_tela, largura_tela * 2)
            # self.rect_obstacle.y = random.randint(100, altura_tela - 100)  
        self.current_frame = (self.current_frame + 1) % len(self.obstacle_type)
        # self.rect = self.obstacle_type[self.current_frame].get_rect(x=largura_tela, y=random.randint(100, altura_tela - 100))
        self.rect.x -= velocidade_tela

    def draw_obstacle(self, window):
        
        window.blit(self.obstacle_type[self.current_frame], (self.rect.x, self.rect.y))
        print(self.rect)


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




class Background(pygame.sprite.Sprite):
    
    def __init__(self, imagem):
        self.surface_background = pygame.image.load(imagem)
        self.surface_background = pygame.transform.scale(self.surface_background, (largura_tela, altura_tela))
        self.rect_background_esquerda = self.surface_background.get_rect(topleft=(0, 0))
        self.rect_background_direita = self.surface_background.get_rect(topleft=(largura_tela, 0))

    def movimenta_background(self):
        
        self.rect_background_esquerda.x -= velocidade_tela
        self.rect_background_direita.x -= velocidade_tela 

        if self.rect_background_esquerda.x <= -largura_tela:
            self.rect_background_esquerda.x = largura_tela
        if self.rect_background_direita.x <= -largura_tela:
            self.rect_background_direita.x = largura_tela

    def desenha_background(self, window):
        window.blit(self.surface_background, self.rect_background_esquerda)
        window.blit(self.surface_background, self.rect_background_direita)





def game_loop(window, state):
    
    player = state['player']
    background_imagem = state['background']
    obstacles = state['obstacles']
    distancia_percorrida = 0
    fonte = pygame.font.Font(None, 36) 



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        player.movimenta_player()  
        background_imagem.movimenta_background()  
        distancia_percorrida += velocidade_tela / 20

        for obstacle in obstacles:
            obstacle.move_obstacle()
            if player.rect_player.colliderect(obstacle.rect):
                
                pygame.quit()
                return

        background_imagem.desenha_background(window)  
        player.desenha_player(window) 

        texto_distancia = fonte.render(f"{int(distancia_percorrida)} M", True, (255, 255, 255))
        window.blit(texto_distancia, (largura_tela * 0.9, altura_tela * 0.03))
    
        for obstacle in obstacles:
            obstacle.draw_obstacle(window)

        pygame.display.update()  



if __name__ == '__main__':
    w, s = inicializa()
    game_loop(w, s)