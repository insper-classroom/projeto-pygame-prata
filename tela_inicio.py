from constantes import *
import pygame

window = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('LabRun')

"""
Carregamento e redimensionamento da imagem de tela inicial
"""
telainicio = pygame.image.load('Telainicio.png')
telainicio = pygame.transform.scale(telainicio, (largura_tela, altura_tela))

"""
Função que mostra a tela inicial
"""

def show_tela_inicio(window):
    window.blit(telainicio, (0, 0))