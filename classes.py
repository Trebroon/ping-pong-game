# Classes used in game
from random import choice
import pygame
from variables import *

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREY)
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        
class Player(Block):
    def __init__(self, width, height, pos_x, pos_y, speed):
        super().__init__(width, height, pos_x, pos_y)
        self.speed = speed
        
    def player_up(self):
        if self.rect.y != 0:
            self.rect.y -= self.speed
    
    def player_down(self):
        if self.rect.bottom != SCREEN_HEIGHT:
            self.rect.bottom += self.speed
    
    def player_reset(self, pos_x):
        self.rect.center = (pos_x, PLAYER_ONE_POS_Y)

               
# Ball      
class Ball(Block):
    def __init__(self, width, height, pos_x, pos_y, players_group):
        super().__init__(width, height, pos_x, pos_y)
        self.players_group = players_group
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED * choice((1, -1))
        self.move = False
        
    def ball_movement(self):
        if self.move == False:
            self.rect.center = (BALL_INIT_POS_X, BALL_INIT_POS_Y)
        else:    
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisons()
        
    def collisons(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        if pygame.sprite.spritecollide(self, self.players_group, False):
            self.speed_x *= -1
    
    def reset_ball(self):
        self.rect.center = (BALL_INIT_POS_X, BALL_INIT_POS_Y)
        self.speed_x *= -1
        self.move = False
                  
        
class Run_Game:
    def __init__(self, players_group, ball_group):
        self.players_group = players_group
        self.ball_group = ball_group
        self.player_one_score = 0
        self.player_two_score = 0
        
    def score_count(self):
        if self.ball_group.sprite.rect.x >= SCREEN_WIDTH + 20:
            self.player_one_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.x <= 0 - 20:
            self.player_two_score += 1
            self.ball_group.sprite.reset_ball()
        
    def display_score(self,screen, text_font):
        # Player one score
        player_one_text = text_font.render(f'{self.player_one_score}', True, DARK_GREY)
        player_one_text_rect = player_one_text.get_rect(center = (P1_SCORE_POS_X, P1_SCORE_POS_Y))
        # Player two score
        player_two_text = text_font.render(f'{self.player_two_score}', True, DARK_GREY)
        player_two_text_rect = player_two_text.get_rect(center = (P2_SCORE_POS_X, P2_SCORE_POS_Y))
        # Show score on screen
        screen.blit(player_one_text, player_one_text_rect)
        screen.blit(player_two_text, player_two_text_rect)
        
    def game_reset(self, screen):
        self.player_one_score = 0
        self.player_two_score = 0
        self.game_update(screen)        
        
    def game_update(self,screen):
        self.score_count()
        self.players_group.draw(screen)
        self.ball_group.draw(screen)
            
        
        
        
