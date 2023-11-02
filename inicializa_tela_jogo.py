import pygame
from constantes import *
from classe_player import Player
from classe_obstacles import Obstacle
from classe_background import Background
from classe_item_imunidade import item_imunidade


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
    background_imagem = Background('background.png') 

    fonte_pixelixada = pygame.font.Font('fonte_pixelizada.ttf', 30)

    pygame.mixer.music.load('main-theme.mp3')

    state = {'player': player, 'background' : background_imagem,  "grupo_obstacles" : pygame.sprite.Group(), "velocidade_tela" : velocidade_tela, "tela" : "inicio", "musica_principal" : pygame.mixer.music, "musica_tocando" : False, "fonte_pixelixada" : fonte_pixelixada, "grupo_itens" : pygame.sprite.Group ()}

    for _ in range(4):
        obstacle = Obstacle()
        obstacle.adiciona_obstacles(state)

    for _ in range (1):
        item = item_imunidade()
        item.adiciona_itens(state)

    return window, state