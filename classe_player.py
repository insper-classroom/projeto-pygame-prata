import pygame 
from constantes import largura_tela, altura_tela, altura_chao
from game_loop import *

"""
Classe que representa o player
"""

class Player(pygame.sprite.Sprite):
    
    """
    Construtor da classe, definição de variáveis e inicialização de sprites
    """

    def __init__(self):

        self.sprite_player_correndo = []
        self.sprite_player_pulando = []

        """
        Inicialização do sprite do player
        """
        self.largura_player = 50
        self.altura_player = 70
        
        self.sprite_player_correndo.append(pygame.transform.scale(pygame.image.load('sprites_player/playercorre1.png'), (self.largura_player, self.altura_player)))
        self.sprite_player_correndo.append(pygame.transform.scale(pygame.image.load('sprites_player/playercorre2.png'), (self.largura_player, self.altura_player)))
        self.sprite_player_correndo.append(pygame.transform.scale(pygame.image.load('sprites_player/playercorre3.png'), (self.largura_player, self.altura_player)))

        self.sprite_player_pulando.append(pygame.transform.scale(pygame.image.load('sprites_player/playerpula1.png'), (self.largura_player, self.altura_player)))
        self.sprite_player_pulando.append(pygame.transform.scale(pygame.image.load('sprites_player/playerpula2.png'), (self.largura_player, self.altura_player)))
        self.sprite_player_pulando.append(pygame.transform.scale(pygame.image.load('sprites_player/playerpula3.png'), (self.largura_player, self.altura_player)))


        """
        Variáveis de controle de animação e movimentação do player
        """

        self.current_frame_run= 0
        self.current_frame_jump= 0

        self.animation_interval_run = 7
        self.animation_counter_run = 0

        self.animation_interval_jump = 15
        self.animation_counter_jump = 0

        self.rect_player = self.sprite_player_correndo[self.current_frame_run].get_rect(x=largura_tela * 0.1, y=altura_tela * 0.5)

        self.velocidade_vertical = 0
        self.impulso = 3
        self.gravidade = 0.1

        self.altura_chao = altura_chao
        self.is_jumping = False

        self.imunidade = False 
        self.imune_duration = 5000

    """
    Função que movimenta o player
    """

    def movimenta_player(self, state):
        
        tecla_apertada = pygame.key.get_pressed()

        """
        Caso a tecla espaço seja apertada, o player pula
        """

        if tecla_apertada[pygame.K_SPACE]:
            if not self.is_jumping:
                self.velocidade_vertical = -self.impulso
                self.is_jumping = True
                self.current_frame_jump = 0
        

        """
        Caso o player esteja pulando, ele é animado
        """

        if self.is_jumping:
            if self.velocidade_vertical < 0:
                self.animation_counter_jump += 1
                if self.animation_counter_jump == self.animation_interval_jump:
                    self.current_frame_jump = 1
                    self.animation_counter_jump = 0

            if self.velocidade_vertical > 0:
                self.current_frame_jump = 2 

        
        self.velocidade_vertical += self.gravidade
        self.rect_player.y += self.velocidade_vertical

        """
        Caso o player esteja no chão, ele não pode cair mais
        """

        if self.rect_player.y < 0:
            self.rect_player.y = 0
            self.velocidade_vertical = 0

        """
        Caso o player esteja no teto, ele não pode subir mais
        """
        if self.rect_player.y > altura_chao - self.rect_player.height:
            self.rect_player.y = altura_chao - self.rect_player.height
            self.velocidade_vertical = 0
            self.is_jumping = False

        """
        Player voa para cima caso a tecla espaço seja apertada e o player não esteja no chão 
        """
        if tecla_apertada[pygame.K_SPACE]:
            self.velocidade_vertical = -self.impulso


        """
        Controla a imunidade do player
        """

        if self.imunidade:
            self.largura_player = 200
            self.altura_player = 300
            self.rect_player.size = (self.largura_player, self.altura_player)
            self.atualiza_escala_player()


        """"
        Controla fim da imunidade do player
        """

        if self.imunidade and pygame.time.get_ticks() - self.imune_counter > self.imune_duration:
            self.imunidade = False
            self.largura_player = 50
            self.altura_player = 70
            self.rect_player.size = (self.largura_player, self.altura_player)
            self.atualiza_escala_player()


    """
    Função que atualiza escala da sprite do player
    """     

    def atualiza_escala_player(self):

        escala = (self.largura_player, self.altura_player)
    
        self.sprite_player_correndo = [pygame.transform.scale(image, escala) for image in self.sprite_player_correndo]
        
        self.sprite_player_pulando = [pygame.transform.scale(image, escala) for image in self.sprite_player_pulando]

    """
    Função que desenha o player na tela e controla sua animação de acordo com o estado
    """

    def desenha_player(self, window):
        if self.is_jumping:
            player_image = self.sprite_player_pulando[self.current_frame_jump]
        else:
            player_image = self.sprite_player_correndo[self.current_frame_run]
            self.animation_counter_run += 1
            if self.animation_counter_run == self.animation_interval_run:
                self.current_frame_run = (self.current_frame_run + 1) % len(self.sprite_player_correndo)
                self.animation_counter_run = 0

        window.blit(player_image, self.rect_player)

