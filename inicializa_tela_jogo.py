import pygame
from constantes import *
from classe_player import Player
from classe_obstacles import Obstacle
from classe_background import Background


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
    obstacles = [Obstacle() for _ in range(4)]

    pygame.mixer.music.load('main-theme.mp3')

    state = {'player': player, 'background' : background_imagem,  "grupo_obstacles" : pygame.sprite.Group(), "velocidade_tela" : velocidade_tela, "tela" : "inicio", "musica_principal" : pygame.mixer.music, "musica_tocando" : False}
    state["grupo_obstacles"].add(obstacles)

    return window, state