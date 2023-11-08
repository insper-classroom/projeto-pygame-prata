import pygame
from constantes import *
from classe_player import Player
from classe_obstacles import Obstacle
from classe_background import Background
from classe_item_imunidade import item_imunidade
from classe_coracoes import item_coracao


"""
Inicialização do jogo seus componentes
"""

def inicializa():
    pygame.init()
    pygame.mixer.init()
   
    """
    Inicialização da tela do jogo
    """
    window = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('LabRun')
   

    """
    Inicialização dos componentes do jogo (player, background, obstaculos etc.)
    """
    player = Player() 
    background_imagem = Background('background.png', 'background2.png') 

    fonte_pixelixada = pygame.font.Font('fonte_pixelizada.ttf', 30)

    fonte_coracao = pygame.font.Font ("PressStart2P.ttf", 30)

    pygame.mixer.music.load('main-theme.mp3')
    som_teleporte = pygame.mixer.Sound("teleporte.mp3")

    state = {'player': player, 'background' : background_imagem,  "grupo_obstacles" : pygame.sprite.Group(), "velocidade_tela" : velocidade_tela, "tela" : "inicio", "musica_principal" : "main-theme.mp3", "fonte_pixelizada" : fonte_pixelixada, "grupo_itens" : pygame.sprite.Group (), "vidas": 3, "fonte_coracao" : fonte_coracao, "grupo_coracao" : pygame.sprite.Group (), "distancia_percorrida" : 0, "musica_tela_final" : "tela-final.mp3", 'musica_atual' : None, "flash" : False, "som_teleporte" : som_teleporte, "teleporte" : False} 

    for _ in range(4):
        obstacle = Obstacle()
        obstacle.adiciona_obstacles(state)

    for _ in range (1):
        item = item_imunidade()
        item.adiciona_itens(state)

    for _ in range (1):
        itemcoracao = item_coracao()
        itemcoracao.adiciona_itens_coracao(state)

    return window, state