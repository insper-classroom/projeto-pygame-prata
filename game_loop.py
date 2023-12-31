import pygame 
from classe_player import *
from classe_background import *
from classe_obstacles import Obstacle
from constantes import largura_tela, altura_tela, velocidade_tela, QUANTIDADE_AUMENTO_VELOCIDADE, MUDANCA_BACKGROUND
from tela_game_over import show_game_over_screen
from tela_inicio import show_tela_inicio
from classe_coracoes import item_coracao
from classe_item_imunidade import item_imunidade
from funcoes_adicionais import troca_musica, flash_white_screen

"""
Função que roda o jogo em um loop infinito
"""

def game_loop(window, state):
    
    """
    Variáveis do jogo
    """

    player = state['player']
    background_imagem = state['background']


    AUMENTAR_VELOCIDADE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(AUMENTAR_VELOCIDADE_EVENT, 20000) 

    tempo_surgimento_item = pygame.time.get_ticks()
    tempo_surgimento_coracao = pygame.time.get_ticks()


    """
    Loop infinito do jogo
    """

    while True:

        """
        Caso o jogo esteja rodando na tela de jogo, ou seja, funcionamento normal do jogo
        """
        if state ['tela'] == "jogo":

            """
            Toca a música principal do jogo e quando o background muda, toca a música da tela final, além de disparar o flash 
            """
            if state ["distancia_percorrida"] >= MUDANCA_BACKGROUND:
                
                if state ["teleporte"] == False:
                    state ["som_teleporte"].play()
                    state ["teleporte"] = True
               
                if state ["flash"] == True:
                    troca_musica(state, state ["musica_tela_final"])
                
                if state ["flash"] == False:
                    state ["flash"] = True
                    flash_white_screen(window)
                

            else:
                troca_musica(state, state ["musica_principal"])



            """
            Desenha background, dependendo da distancia percorrida (background inicial ou final)
            """

            background_imagem.desenha_background(window, state) 
        


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
            Adiciona novos itens de imunidade na tela e os movimenta 
            """

            for item in state ["grupo_itens"]:
                    
                    item.rect.x -= state ["velocidade_tela"]

                    if item.rect.x < -item.rect.width:
                        item.kill()

                    item.desenha_item(window)

                    if player.rect_player.colliderect(item.rect):
                        state ["som_especial"].play()
                        player.imunidade = True
                        item.kill()
                        player.imune_counter = pygame.time.get_ticks()
                    
            
            if pygame.time.get_ticks() - tempo_surgimento_item > 30000:

                tempo_surgimento_item = pygame.time.get_ticks()
                novo_item = item_imunidade()
                novo_item.adiciona_itens(state)

            """
            Adiciona novos itens de vida (corações) na tela e os movimenta
            """

            for itemcoracao in state ["grupo_coracao"]:
                
                itemcoracao.rect.x -= state ["velocidade_tela"]

                if itemcoracao.rect.x < -itemcoracao.rect.width:
                    itemcoracao.kill()

                if player.rect_player.colliderect(itemcoracao.rect):
                    if state ["vidas"] < 3:
                        state ["vidas"] += 1
                        state ["som_vida"].play()
                        itemcoracao.kill()

                itemcoracao.desenha_itemcoracao(window)

            if pygame.time.get_ticks() - tempo_surgimento_coracao > 40000:
                
                tempo_surgimento_coracao = pygame.time.get_ticks()
                novo_itemcoracao = item_coracao()
                novo_itemcoracao.adiciona_itens_coracao(state)


            """
            Movimentação dos componentes do jogo
            """

            player.movimenta_player(state)  
            
            background_imagem.movimenta_background(state)
                
                
            state ["distancia_percorrida"] +=  state["velocidade_tela"] / 30

            for obstacle in state ["grupo_obstacles"]:
                obstacle.movimenta_e_anima_obstacle(state)
                

                """
                Caso o player colida com um obstáculo, ele perde uma vida e morre quando elas chegam a 0
                """
                if player.rect_player.colliderect(obstacle.rect) and player.imunidade == False:

                    state ["som_choque"].play()
                    
                    if state ["vidas"] > 0:
                        state ["vidas"] -= 1
                        obstacle.kill ()
                        novo_obstacle = Obstacle()
                        novo_obstacle.adiciona_obstacles(state)
                        player.timer = 180
                    
                    if state ["vidas"] <= 0:
                        show_game_over_screen(window)
                        state ["tela"] = "game_over"


                if player.timer > 0:
                    player.timer -= 1

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
            fonte_pixelizada = state ["fonte_pixelizada"]
            distancia_percorrida = state ["distancia_percorrida"]
            texto_distancia = fonte_pixelizada.render(f"{int(distancia_percorrida)} M", True, (255, 255, 255))
            window.blit(texto_distancia, (largura_tela * 0.9, altura_tela * 0.12))
    

            """
            Mostra as vidas na tela 
            """
            fonte_coracao = state ["fonte_coracao"]
            coracao = chr (9829)
            coracoes = coracao * state ["vidas"]
            texto_vidas = fonte_coracao.render(f"{coracoes}", True, (255, 0, 0))
            window.blit (texto_vidas, (largura_tela * 0.9, altura_tela * 0.04))



    
        """
        Caso o jogo esteja rodando na tela de game over
        """

        if state ['tela'] == "game_over" and player.imunidade == False:
            
            show_game_over_screen(window)
            
            pygame.mixer.music.stop()

            fonte_pixelizada = state ["fonte_pixelizada"]
            distancia_percorrida = state ["distancia_percorrida"]
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
                    state ["distancia_percorrida"] = 0
                    state ["grupo_itens"] = pygame.sprite.Group ()
                    state ["vidas"] = 3
                    state ["grupo_coracao"] = pygame.sprite.Group ()
                    state ["teleporte"] = False
                    state ["flash"] = False

                    for _ in range (1):
                        item = item_imunidade()
                        item.adiciona_itens(state)

                    for _ in range (1):
                        itemcoracao = item_coracao()
                        itemcoracao.adiciona_itens_coracao(state)
                    




        """
        Caso o jogo esteja rodando na tela de início
        """
            
        if state ['tela'] == "inicio":
            show_tela_inicio(window)
            
            fonte_pixelizada = state ["fonte_pixelizada"]
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