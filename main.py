import pygame
from sys import exit

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
    if pressed_keys[pygame.K_UP]:
        player_two_rect.y -= player_speed
    if pressed_keys[pygame.K_DOWN]:
        player_two_rect.y += player_speed
    if pressed_keys[pygame.K_w]:
        player_one_rect.y -= player_speed
    if pressed_keys[pygame.K_s]:
        player_one_rect.y += player_speed

    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y
    
    screen.fill('black')
    screen.blit(player_one_surf, player_one_rect)
    screen.blit(player_two_surf, player_two_rect)
    pygame.draw.ellipse(screen, 'grey', ball_rect)
    
    

    pygame.display.flip()
    clock.tick(60)