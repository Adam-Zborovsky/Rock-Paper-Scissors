import pygame
import time
from Board import Board
SCREEN_SIZE = (800, 800)


def game():
    running = True
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Rock Paper Scissors')
    screen.fill((255, 255, 255))
    pygame.display.flip()
    board = Board()
    board.draw(screen)

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                board.draw_pick(screen, x, y)

if __name__ == '__main__':
    game()
