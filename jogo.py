import pygame
from constantes import *
import random

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Corre!')
    return window

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        self.surface_obstacle = pygame.Surface((30, 30))
        self.surface_obstacle.fill((255, 0, 0))
        self.rect_obstacle = self.surface_obstacle.get_rect(
            x=largura_tela, y=altura_tela * 0.5
        )

    def move_obstacle(self):
        self.rect_obstacle.x -= velocidade_tela
        if self.rect_obstacle.right < 0:
            self.rect_obstacle.x = largura_tela
            self.rect_obstacle.y = random.randint(100, altura_tela - 100)  

    def draw_obstacle(self, window):
        window.blit(self.surface_obstacle, self.rect_obstacle)


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        self.surface_player = pygame.Surface((50, 25))
        self.surface_player.fill((0, 255, 0))
        self.rect_player = self.surface_player.get_rect(x=largura_tela * 0.1, y=altura_tela * 0.5)
        self.velocidade_vertical = 0
        self.impulso = 0.6
        self.gravidade = 0.01

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
        if self.rect_player.y > altura_tela - self.rect_player.height:
            self.rect_player.y = altura_tela - self.rect_player.height
            self.velocidade_vertical = 0

            if tecla_apertada[pygame.K_SPACE]:
                self.velocidade_vertical = -self.impulso

    
    def desenha_player(self, window):
        window.blit(self.surface_player, self.rect_player)




class Background(pygame.sprite.Sprite):
    
    def __init__(self, imagem):
        self.surface_background = pygame.image.load(imagem)
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





def game_loop(window):
    
    player = Player() 
    background_imagem = Background('Background_pygame_project.webp') 

    distancia_percorrida = 0
    fonte = pygame.font.Font(None, 36) 

    tempo_passado = 0
    tempo_de_aumento_velocidade = 20000
    incremento_velocidade = 0.2
    tempo_entre_frames = pygame.time.Clock()


    obstacles = [Obstacle() for _ in range(5)]


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        tempo_passado += tempo_entre_frames.tick()

        if tempo_passado >= tempo_de_aumento_velocidade:
            global velocidade_tela
            velocidade_tela += incremento_velocidade
            tempo_passado -= tempo_de_aumento_velocidade

        player.movimenta_player()  
        background_imagem.movimenta_background()  
        distancia_percorrida += velocidade_tela / 50

        for obstacle in obstacles:
            obstacle.move_obstacle()
            if player.rect_player.colliderect(obstacle.rect_obstacle):
                
                pygame.quit()
                return

        background_imagem.desenha_background(window)  
        player.desenha_player(window) 

        texto_distancia = fonte.render(f"{int(distancia_percorrida)} M ", True, (255, 255, 255))
        window.blit(texto_distancia, (largura_tela * 0.9, altura_tela * 0.1))
    
        for obstacle in obstacles:
            obstacle.draw_obstacle(window)

        pygame.display.update()  



if __name__ == '__main__':
    w = inicializa()
    game_loop(w)