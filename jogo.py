import pygame
from constantes import *
import random

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('LabRun')
    player = Player() 
    background_imagem = Background('background.png') 
    obstacles = [Obstacle() for _ in range(2 )]
    state = {'player': player, 'background' : background_imagem,  "grupo_obstacles" : pygame.sprite.Group()}
    state["grupo_obstacles"].add(obstacles)

    return window, state

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

        self.rect = self.obstacle_type[self.current_frame].get_rect(x=largura_tela + 50, y=altura_tela * 0.5)

    def movimenta_e_anima_obstacle(self):

        self.animation_counter += 1
        if self.animation_counter == self.animation_interval:
            self.current_frame = (self.current_frame + 1) % len(self.obstacle_type)
            self.animation_counter = 0
        
        self.rect.x -= velocidade_tela

    def reset_posicao(self):
        self.rect.x = largura_tela + random.randint (0, 600)  
        self.rect.y = random.randint(100 , altura_tela) 

    def adiciona_obstacles (self, state):

        while pygame.sprite.spritecollideany(self, state["grupo_obstacles"]) != None:
            self.reset_posicao()
        
        state ["grupo_obstacles"].add(self)

    def desenha_obstacles(self, window):
        
        window.blit(self.obstacle_type[self.current_frame], (self.rect.x, self.rect.y))


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
        pygame.sprite.Sprite.__init__(self)

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
    distancia_percorrida = 0
    fonte = pygame.font.Font(None, 36)

    AUMENTAR_VELOCIDADE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(AUMENTAR_VELOCIDADE_EVENT, 20000) 



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

            elif event.type == AUMENTAR_VELOCIDADE_EVENT:
                global velocidade_tela
                velocidade_tela += QUANTIDADE_AUMENTO_VELOCIDADE

        player.movimenta_player()  
        background_imagem.movimenta_background()  
        distancia_percorrida += velocidade_tela / 30


        for obstacle in state ["grupo_obstacles"]:
            obstacle.movimenta_e_anima_obstacle()
            
            if player.rect_player.colliderect(obstacle.rect):
                pygame.quit()

            if obstacle.rect.x < -obstacle.rect.width:
                obstacle.kill()
                novo_obstacle = Obstacle()
                novo_obstacle.adiciona_obstacles(state)


        background_imagem.desenha_background(window)  
        player.desenha_player(window) 

        texto_distancia = fonte.render(f"{int(distancia_percorrida)} M", True, (255, 255, 255))
        window.blit(texto_distancia, (largura_tela * 0.9, altura_tela * 0.03))
    
        for obstacle in state ["grupo_obstacles"]:
            obstacle.desenha_obstacles(window)

        pygame.display.flip()  



if __name__ == '__main__':
    w, s = inicializa()
    game_loop(w, s)