background_image_filename = '1671682721_kalix-club-p-fon-dlya-prezentatsii-milnie-puziri-krasiv-41.jpg'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
fullscreen = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                fullscreen = not fullscreen
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                exit()
        if fullscreen:
            screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
        else:
            screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.blit(background, (0, 0))
    pygame.display.update()

