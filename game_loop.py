import pygame 
from constantes import *
from classe_player import Player
from classe_background import Background
from classe_obstacles import Obstacle

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