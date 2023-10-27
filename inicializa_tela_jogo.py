import pygame
from constantes import *
from classe_player import Player
from classe_obstacles import Obstacle
from classe_background import Background

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('LabRun')
    player = Player() 
    background_imagem = Background('background.png') 
    obstacles = [Obstacle() for _ in range(4)]
    state = {'player': player, 'background' : background_imagem,  "grupo_obstacles" : pygame.sprite.Group(), "velocidade_tela" : velocidade_tela}
    state["grupo_obstacles"].add(obstacles)

    return window, state