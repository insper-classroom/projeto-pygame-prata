import pygame 
from classe_player import *
from classe_background import *
from classe_obstacles import Obstacle
from constantes import largura_tela, altura_tela, velocidade_tela, QUANTIDADE_AUMENTO_VELOCIDADE
from tela_game_over import show_game_over_screen
from tela_inicio import show_tela_inicio
import random
from classe_item_imunidade import item_imunidade

"""
Função que roda o jogo em um loop infinito
"""

def game_loop(window, state):
    
    """
    Variáveis do jogo
    """

    player = state['player']
    background_imagem = state['background']
    distancia_percorrida = 0
    fonte = pygame.font.Font(None, 36)

    AUMENTAR_VELOCIDADE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(AUMENTAR_VELOCIDADE_EVENT, 20000) 

    tempo_surgimento_item = pygame.time.get_ticks()


    """
    Loop infinito do jogo
    """

    while True:

        """
        Caso o jogo esteja rodando na tela de jogo, ou seja, funcionamento normal do jogo
        """
        if state ['tela'] == "jogo":

            """
            Toca a música principal do jogo
            """

            if state ["musica_tocando"] == False:
                state ["musica_principal"].play()
                state ["musica_tocando"] = True

            """"
            Desenha background
            """
            background_imagem.desenha_background(window)  
            

            """
            Velociodade aumenta com o passar do tempo jogando
            """
            for event in pygame.event.get():
                
                if event.type == AUMENTAR_VELOCIDADE_EVENT:
                    state ['velocidade_tela'] += QUANTIDADE_AUMENTO_VELOCIDADE

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 
                
            """
            Adiciona novos itens na tela e os movimenta 
            """

            for item in state ["grupo_itens"]:
                    
                    item.rect.x -= state ["velocidade_tela"]

                    if item.rect.x < -item.rect.width:
                        item.kill()

                    item.desenha_item(window)

                    if player.rect_player.colliderect(item.rect):
                        player.imunidade = True
                        item.kill()
                        player.imune_counter = pygame.time.get_ticks()
                    
            
            if pygame.time.get_ticks() - tempo_surgimento_item > 30000:

                tempo_surgimento_item = pygame.time.get_ticks()
                novo_item = item_imunidade()
                novo_item.adiciona_itens(state)


            """
            Movimentação dos componentes do jogo
            """

            player.movimenta_player(state)  
            background_imagem.movimenta_background(state)  
            distancia_percorrida +=  state["velocidade_tela"] / 30

            for obstacle in state ["grupo_obstacles"]:
                obstacle.movimenta_e_anima_obstacle(state)
                

                """
                Caso o player colida com um obstáculo, o jogo acaba e a tela de game over é mostrada
                """
                if player.rect_player.colliderect(obstacle.rect) and player.imunidade == False:
                    show_game_over_screen(window)
                    state ["tela"] = "game_over"

                """
                Caso o obstáculo saia da tela, ele é removido e um novo obstáculo é adicionado
                """            
                if obstacle.rect.x < -obstacle.rect.width:
                    obstacle.kill()
                    novo_obstacle = Obstacle()
                    novo_obstacle.adiciona_obstacles(state)


            """
            Adiciona novos obstáculos na tela
            """
            for obstacle in state ["grupo_obstacles"]:
                obstacle.desenha_obstacles(window)

            """
            Desenha o player na tela
            """
            player.desenha_player(window)

            
            """
            Mostra a distância percorrida na tela
            """
            fonte_pixelizada = state ["fonte_pixelixada"]
            texto_distancia = fonte_pixelizada.render(f"{int(distancia_percorrida)} M", True, (255, 255, 255))
            window.blit(texto_distancia, (largura_tela * 0.9, altura_tela * 0.03))
    


    
        """
        Caso o jogo esteja rodando na tela de game over
        """

        if state ['tela'] == "game_over" and player.imunidade == False:
            
            show_game_over_screen(window)
            state ["musica_principal"].stop()
            state ["musica_tocando"] = False

            fonte_pixelizada = state ["fonte_pixelixada"]
            texto_distancia = fonte_pixelizada.render(f"SCORE: {int(distancia_percorrida)}", True, (0,0,0))
            window.blit(texto_distancia, (425, 369))

            texto_retry = fonte_pixelizada.render("CLIQUE EM QUALQUER LUGAR PARA REINICIAR", True, (255,255,255))
            window.blit(texto_retry, (160, 450))

            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                

                """
                Caso o jogador clique em qualquer lugar da tela, o jogo é reiniciado
                """

                if evento.type == pygame.MOUSEBUTTONUP:
                    state ["tela"] = "jogo"
                    state ["velocidade_tela"] = velocidade_tela
                    state ["player"] = player
                    state ["grupo_obstacles"] = pygame.sprite.Group()
                    
                    for _ in range(4):  
                        novo_obstacle = Obstacle()
                        novo_obstacle.adiciona_obstacles(state)

                    state ["background"] = background_imagem
                    distancia_percorrida = 0
                    state ["musica_tocando"] = False
                    state ["grupo_itens"] = pygame.sprite.Group ()

                    for _ in range (1):
                        item = item_imunidade()
                        item.adiciona_itens(state)
                    




        """
        Caso o jogo esteja rodando na tela de início
        """
            
        if state ['tela'] == "inicio":
            show_tela_inicio(window)
            
            fonte_pixelizada = state ["fonte_pixelixada"]
            texto_instrucao = fonte_pixelizada.render(f"PRESSIONE ESPACO PARA PULAR", True, (255, 255,255))
            window.blit(texto_instrucao, (250, 465))

            tecla_apertada = pygame.key.get_pressed()

            if tecla_apertada[pygame.K_SPACE]:
                state ["tela"] = "jogo"

            
            event = pygame.event.get()

            for evento in event:

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

                if evento.type == pygame.MOUSEBUTTONUP:
                    pos_mouse = pygame.mouse.get_pos()

                    if pos_mouse[0] > 350 and pos_mouse[0] < 650 and pos_mouse[1] > 350 and pos_mouse[1] < 450:
                        state ["tela"] = "jogo"


        pygame.display.flip()  