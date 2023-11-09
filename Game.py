import pygame
import Client
import time
from Board import Board
SCREEN_SIZE = (800, 800)


def check_winner(screen, my_pick, enm):
    if my_pick == 'rock' and enm == 'scissors' or my_pick == 'paper' and enm == 'rock' or my_pick == 'scissors' and enm == 'paper':
        text = 'You Won'
        b_color = (50, 255, 50)
        t_color = (20, 150, 20)
    if enm == 'rock' and my_pick == 'scissors' or enm == 'paper' and my_pick == 'rock' or enm == 'scissors' and my_pick == 'paper':
        text = 'You Lost'
        b_color = (255, 50, 50)
        t_color = (150, 20, 20)
    if enm == my_pick :
        text = 'Draw'
        b_color = (255, 255, 255)
        t_color = (20, 20, 20)

    screen.fill(b_color)
    font = pygame.font.Font('FiraSans-Black.ttf', 64)
    text = font.render(text, True, t_color, b_color)
    textrec = text.get_rect()
    textrec.center = (400, 400)
    screen.blit(text, textrec)
    pygame.display.flip()
    time.sleep(3)


def game():
    my_pick = None
    running = True
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Rock Paper Scissors')
    screen.fill((200, 255, 200))
    pygame.display.flip()
    board = Board()
    board.draw(screen)
    
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                my_pick = board.draw_pick(screen, False, x, y)
            if my_pick is not None:
                Client.connect()
                Client.send(my_pick.zfill(8))
                enm = Client.receive()
                board.draw_enemy_pick(screen, enm)
                time.sleep(2)
                check_winner(screen, my_pick, enm)
                screen.fill((200, 255, 200))
                board.draw(screen)
                my_pick = None
        

if __name__ == '__main__':
    game()
