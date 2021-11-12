import pygame
from sys import exit
from random import choice

from settings import *
              

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)



# player one
player_one_surf = pygame.Surface((5,100))
player_one_surf.fill('grey')
player_one_rect = player_one_surf.get_rect(center = (50,300))

# playeyr two
player_two_surf = pygame.Surface((5,100))
player_two_surf.fill('grey')
player_two_rect = player_two_surf.get_rect(center = (950,300))

player_speed = 5

# ball
ball_surf = pygame.Surface((10,10))
ball_surf.fill('grey')
ball_rect = ball_surf.get_rect(center = (500,300))
ball_speed_x = 5
ball_speed_y = 5




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()           

    pressed_keys = pygame.key.get_pressed()
    # Player Two Movement
    # Up Movement
    if pressed_keys[pygame.K_UP]:
        if player_two_rect.y == 0:
            player_two_rect.y = 0
        else:
            player_two_rect.y -= player_speed
    # Down Movement
    if pressed_keys[pygame.K_DOWN]:
        if player_two_rect.bottom == 600:
            player_two_rect.bottom = 600
        else:
            player_two_rect.y += player_speed
    # Player One Movement
    # Up Movement
    if pressed_keys[pygame.K_w]:
        if player_one_rect.y == 0:
            player_one_rect.y = 0
        else:
            player_one_rect.y -= player_speed
    # Down Movement   
    if pressed_keys[pygame.K_s]:
        if player_one_rect.bottom == 600:
            player_one_rect.bottom = 600
        else:
            player_one_rect.y += player_speed

    # Ball Movement
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y
    if ball_rect.top <= 0 or ball_rect.bottom >= screen_height:
        ball_speed_y *= -1
    if ball_rect.left <= 0 or ball_rect.right >= screen_width:
        ball_speed_x *= -1
    
    
    
    screen.fill('black')
    screen.blit(player_one_surf, player_one_rect)
    screen.blit(player_two_surf, player_two_rect)
    pygame.draw.ellipse(screen, 'grey', ball_rect)
    
    

    pygame.display.flip()
    clock.tick(60)