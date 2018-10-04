import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((200, 80))
pygame.display.set_caption('blue')
screen.fill((0, 0, 255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
