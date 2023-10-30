import pygame 
from constantes import largura_tela, altura_tela, altura_chao
from game_loop import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        # self.surface_player = pygame.Surface((25, 50))
        # self.surface_player.fill((0, 255, 0))
        self.sprite_player_correndo = []
        self.sprite_player_pulando = []

        self.sprite_player_correndo.append(pygame.image.load('sprites_player/playercorre1.png'))
        self.sprite_player_correndo.append(pygame.image.load('sprites_player/playercorre2.png'))
        self.sprite_player_correndo.append(pygame.image.load('sprites_player/playercorre3.png'))

        self.sprite_player_pulando.append(pygame.image.load('sprites_player/playerpula1.png'))
        self.sprite_player_pulando.append(pygame.image.load('sprites_player/playerpula2.png'))
        self.sprite_player_pulando.append(pygame.image.load('sprites_player/playerpula3.png'))

        self.current_frame_run= 0
        self.current_frame_jump= 0

        self.animation_interval_run = 7
        self.animation_counter_run = 0

        self.animation_interval_jump = 15
        self.animation_counter_jump = 0

        # self.rect_player = self.surface_player.get_rect(x=largura_tela * 0.1, y=altura_tela * 0.5)
        self.rect_player = self.sprite_player_correndo[self.current_frame_run].get_rect(x=largura_tela * 0.1, y=altura_tela * 0.5)

        self.velocidade_vertical = 0
        self.impulso = 3
        self.gravidade = 0.1

        self.altura_chao = altura_chao
        self.is_jumping = False



    def movimenta_player(self):
        
        tecla_apertada = pygame.key.get_pressed()

        if tecla_apertada[pygame.K_SPACE]:
            if not self.is_jumping:
                self.velocidade_vertical = -self.impulso
                self.is_jumping = True
                self.current_frame_jump = 0
        
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

        # Limite superior
        if self.rect_player.y < 0:
            self.rect_player.y = 0
            self.velocidade_vertical = 0

        # Limite inferior
        if self.rect_player.y > altura_chao - self.rect_player.height:
            self.rect_player.y = altura_chao - self.rect_player.height
            self.velocidade_vertical = 0
            self.is_jumping = False

        if tecla_apertada[pygame.K_SPACE]:
            self.velocidade_vertical = -self.impulso


    def desenha_player(self, window):
        # window.blit(self.surface_player, self.rect_player)
        if self.is_jumping:
            player_image = self.sprite_player_pulando[self.current_frame_jump]
        else:
            player_image = self.sprite_player_correndo[self.current_frame_run]
            self.animation_counter_run += 1
            if self.animation_counter_run == self.animation_interval_run:
                self.current_frame_run = (self.current_frame_run + 1) % len(self.sprite_player_correndo)
                self.animation_counter_run = 0

        window.blit(player_image, self.rect_player)