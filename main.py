import pygame
from sys import exit

from pygame.constants import KEYDOWN

from variables import *
from classes import *   

def main():         

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    text_font = pygame.font.Font(FONT_PATH, FONT_SIZE)
    active = False


    players_group = pygame.sprite.Group()
    # Player One
    player_one = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_ONE_POS_X, PLAYER_ONE_POS_Y, PLAYER_SPEED)
    players_group.add(player_one)
    # Player Two
    player_two = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_TWO_POS_X, PLAYER_TWO_POS_Y, PLAYER_SPEED)
    players_group.add(player_two)

    # Ball
    ball_sprite = pygame.sprite.GroupSingle()
    ball = Ball(BALL_WIDTH, BALL_HEIGHT, BALL_INIT_POS_X, BALL_INIT_POS_Y, players_group)
    ball_sprite.add(ball)

    # run game func
    run_game = Run_Game(players_group, ball_sprite)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()    
            # Game Start
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball.move = True       

        pressed_keys = pygame.key.get_pressed()
        # Player Two Movement
        # Up Movement
        if pressed_keys[pygame.K_UP]:
            player_two.player_up()
        # Down Movement
        if pressed_keys[pygame.K_DOWN]:
            player_two.player_down()
        # Player One Movement
        # Up Movement
        if pressed_keys[pygame.K_w]:     
            player_one.player_up()
        # Down Movement   
        if pressed_keys[pygame.K_s]:
            player_one.player_down()
        # Game Reset
        if pressed_keys[pygame.K_r]:
            player_one.player_reset(PLAYER_ONE_POS_X)
            player_two.player_reset(PLAYER_TWO_POS_X)
            run_game.game_reset(screen)
        
        # Displaying screen
        screen.fill(BG_COLOR)
        pygame.draw.line(screen, DARK_GREY, MID_LINE_START, MID_LINE_END)
        
        # Displaying score
        run_game.display_score(screen, text_font)
    
        # Updating players, ball and score
        run_game.game_update(screen)
        # Ball Movement
        ball.ball_movement()

        pygame.display.flip()
        clock.tick(60)
        
if __name__ == '__main__':
    main()