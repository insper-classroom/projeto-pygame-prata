from constantes import *
import pygame

window = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('LabRun')

"""
Carregamento e redimensionamento da imagem de game over
"""
telagameover = pygame.image.load('Telagameover.png')
telagameover = pygame.transform.scale(telagameover, (largura_tela, altura_tela))


"""
Função que mostra a tela de game over
"""

def show_game_over_screen(window):
    window.blit(telagameover, (0, 0))