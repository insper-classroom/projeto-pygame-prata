import pygame


"""
Função que gerencia a troca de músicas entre a música principal e a música da tela final
"""

def troca_musica(state, nova_musica):
    if state['musica_atual'] == nova_musica and pygame.mixer.music.get_busy():
        return


    pygame.mixer.music.load(nova_musica)
    pygame.mixer.music.play(-1) 


    state['musica_atual'] = nova_musica


"""
Funcão que gerencia o flash na troca de background
"""

def flash_white_screen(window):
    white_surface = pygame.Surface(window.get_size())
    white_surface.fill((255, 255, 255))  
    window.blit(white_surface, (0, 0))    
    pygame.display.flip()                 
    pygame.time.wait(100)    