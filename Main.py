import pygame
import sys
from constants import *
from Tank import tank
from Text import simple_text

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width,window_height))
    clock = pygame.time.Clock()
    player1 = tank(window, 'Player1')
    player2 = tank(window, 'Player2', player2_color, 772, 480, 100, {'left': pygame.K_a, 'right': pygame.K_d, 'aim_up': pygame.K_w, 'aim_down': pygame.K_s, 'shoot': pygame.K_TAB})
    players = [player1, player2]

    tint_screen = pygame.Surface((window_width, window_height))
    tint_screen.fill(black)
    tint_screen.set_alpha(128)

    end_game_text = simple_text(window, f"Nobody Wins", 0, 0, white, 'Comic Sans MS', 50)

    # initialize loop
    running = True
    while True:
        if running:
            dt = clock.tick(frames_per_second) / 100
            # Event checker
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            for player in players:
                player.update(dt)
                for bullet in player.bullets:
                    bullet.update()
                    for other_player in players:
                        if other_player != player:
                            if other_player.collide(value = bullet):
                                end_game_text.text = f"{player.name} Wins. Press Enter to restart"
                                running = False

            # Screen and Object Rendering
            window.fill(blue)
            pygame.draw.polygon(window, brown, ground_fill_points)
            pygame.draw.lines(window, green, False, ground_points, 3)
            for player in players:
                player.draw()
                for bullet in player.bullets:
                    bullet.draw()
            pygame.display.update()
        
        else:
            dt = clock.tick(frames_per_second) / 100
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = True
                        player1.x, player1.y = 144, 480
                        player2.x, player2.y = 772, 480
            
            window.fill(blue)
            pygame.draw.polygon(window, brown, ground_fill_points)
            pygame.draw.lines(window, green, False, ground_points, 3)
            for player in players:
                player.draw()
            window.blit(tint_screen, (0,0))
            end_game_text.print_text()

            pygame.display.update()
                

if __name__ == "__main__":
    main()