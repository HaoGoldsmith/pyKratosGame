import pygame
from pygame.locals import *
from sys import exit
import random

# from Classes import Vector2, Bubble
#
background_image_filename = '1671682721_kalix-club-p-fon-dlya-prezentatsii-milnie-puziri-krasiv-41.jpg'
mouse_image_filename = 'Untitled-1.png'
bubble_img_filename = "bubble.png"
#
pygame.init()
#
dis_width = 640
dis_height = 480
screen_size = (dis_width, dis_height)
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption("Catch the bubble")
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
bubble_img = pygame.image.load(bubble_img_filename).convert_alpha()
#


font = pygame.font.SysFont("arial", 32)
font_height = font.get_linesize()
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))

    pressed_key_text = []
    pressed_keys = pygame.key.get_pressed()
    print(pressed_keys)
    y = font_height

    # for k, p in enumerate(pressed_keys):
    #     if p:
    #         key_name = pygame.key.name(k)
    #         text_surface = font.render(key_name + " pressed", True, (0, 0, 0))
    #         screen.blit(text_surface, (8, y))
    #         y += font_height
    pygame.display.update()
