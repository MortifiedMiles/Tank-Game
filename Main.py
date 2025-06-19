import pygame
import sys
from constants import *
from Tank import tank

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width,window_height))
    clock = pygame.time.Clock()
    player1 = tank(window)
    player2 = tank(window, player2_color, 772, 480, 100, {'left': pygame.K_a, 'right': pygame.K_d, 'aim_up': pygame.K_w, 'aim_down': pygame.K_s, 'shoot': pygame.K_TAB})
    players = [player1, player2]

    # initialize loop
    while True:
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
                            print(f'collide {bullet.x}')

        # Screen and Object Rendering
        window.fill(blue)
        pygame.draw.polygon(window, brown, ground_fill_points)
        pygame.draw.lines(window, green, False, ground_points, 3)
        for player in players:
            player.draw()
            for bullet in player.bullets:
                bullet.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()