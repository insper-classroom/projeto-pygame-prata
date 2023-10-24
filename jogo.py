import pygame

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('Corre!')
    return window

def recebe_eventos():
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    return game

def desenha(window):
    window.fill((0, 0, 0))
    pygame.display.update()

def game_loop(window):
    # TODO: receber assets como argumento e repassar para desenha
    while recebe_eventos():
        desenha(window)


if __name__ == '__main__':
    # TODO: receber assets aqui e repassar para game_loop
    w = inicializa()
    game_loop(w)
