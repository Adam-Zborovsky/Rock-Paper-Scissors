import pygame
import time
pygame.init()


class Board:
    def draw(self, screen):
        rock = pygame.transform.scale(pygame.image.load('images/rock.png'), (175, 175))
        paper = pygame.transform.scale(pygame.image.load('images/paper.png'), (175, 175))
        scissors = pygame.transform.scale(pygame.image.load('images/scissors.png'), (175, 175))
        screen.blit(rock, (100,550))
        screen.blit(paper, (312.5,550))
        screen.blit(scissors, (525,550))

        pygame.draw.line(screen, (0, 150, 0), (200,280), (600,280), 4)
        pygame.draw.circle(screen, (0, 150, 0), (200,281), 2)
        pygame.draw.circle(screen, (0, 150, 0), (600,281), 2)

        font = pygame.font.Font('FiraSans-Black.ttf', 36)
        text = font.render("You'r Pick", True, (20, 150, 20), (255, 255, 255))
        textrec = text.get_rect()
        textrec.center = (400,310)
        screen.blit(text, textrec)

        font = pygame.font.Font('FiraSans-Black.ttf', 36)
        text = font.render("Opponent's Pick", True, (20, 150, 20), (255, 255, 255))
        textrec = text.get_rect()
        textrec.center = (400,250)
        screen.blit(text, textrec)

        pygame.display.flip()


    def draw_pick(self, screen, x, y):
        pick = ""
        if 550 < y < 725:
            if 100 < x < 275:
                pick = 'rock'
            if 312.5 < x < 487.5:
                pick = 'paper'
            if 525 < x < 700:
                pick = 'scissors'
        item = pygame.transform.scale(pygame.image.load(f"images/{pick}.png"), (175, 175))
        screen.blit(item, (315,335))
        pygame.display.flip()
        return pick
