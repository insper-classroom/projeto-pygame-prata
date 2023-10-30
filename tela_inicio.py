from constantes import *
import pygame

window = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('LabRun')

# Carrega a imagem de fundo
telainicio = pygame.image.load('Telainicio.png')
telainicio = pygame.transform.scale(telainicio, (largura_tela, altura_tela))

def show_tela_inicio(window):
    window.blit(telainicio, (0, 0))
    pygame.display.flip()