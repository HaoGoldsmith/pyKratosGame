import pygame
from pygame.locals import *
from sys import exit
import random
from Classes import Vector2

background_image_filename = '1671682721_kalix-club-p-fon-dlya-prezentatsii-milnie-puziri-krasiv-41.jpg'
mouse_image_filename = 'Untitled-1.png'
bubble_img_filename = "bubble.png"

pygame.init()

dis_width = 640
dis_height = 480
screen_size = (dis_width, dis_height)
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption("Catch the bubble")
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
bubble_img = pygame.image.load(bubble_img_filename).convert_alpha()

sprite = mouse_cursor
# The x coordinate of our sprite
# Our clock object
clock = pygame.time.Clock()

'''скорость разных объектов'''


# x1 = 0.
# x2 = 0.
# # Speed in pixels per second
# speed = 250.
# frame_no = 0
#
# while True:
#  for event in pygame.event.get():
#     if event.type == QUIT:
#         exit()
#     screen.blit(background, (0,0))
#     screen.blit(sprite, (x1, 50))
#     screen.blit(sprite, (x2, 250))
#     time_passed = clock.tick(30)
#     time_passed_seconds = time_passed / 1000.0
#     distance_moved = time_passed_seconds * speed
#     x1 += distance_moved
#     if (frame_no % 5) == 0:
#         distance_moved = time_passed_seconds * speed
#         x2 += distance_moved * 5.
#         # If the image goes off the end of the screen, move it back
#         if x1 > 640.:
#             x1 = 0.
#         if x2 > 640.:
#             x2 = 0.
#     pygame.display.update()
#     frame_no += 1

def bubbles():
    bubble_size = random.randrange(20, 70)
    bubblex = round(random.randrange(bubble_size, dis_width - bubble_size) / 10.0) * 10.0
    bubbley = round(random.randrange(0, dis_height - 430) / 10.0) * 10.0
    if bubble_size < 35:
        bspeed = 450  # 100-150-120
    elif bubble_size > 55:
        bspeed = 750
    else:
        bspeed = 600
    bi = pygame.transform.scale(bubble_img, (bubble_size, bubble_size))
    return bi, bubblex, bubbley, bspeed

bubbles()
bubbles()
bubbles()
bubbles()
# bubbles_count = 0
# bubbles_array = []
# for i in range(15):
#     if bubbles_count < 5:
#         bi, bubblex, bubbley, bspeed = bubbles()
#         bubbles_array.append([bi, bubblex, bubbley, bspeed])
#         bubbles_count += 1
#     else:
#         bubbles_array.pop(0)
#         bi, bubblex, bubbley, bspeed = bubbles()
#         bubbles_array.append([bi, bubblex, bubbley, bspeed])
#         bubbles_count += 1

'''кусок с пузырьками'''
# for b in bubbles_array:
#     screen.blit(b[0], (b[1], b[2]))
#     time_passed = clock.tick(b[3])
#     time_passed_seconds = time_passed / 1000.0
#     distance_moved = time_passed_seconds * b[3]
#     b[2] += distance_moved
#     if b[2] > 480:
#         b[2] -= 480

# def Bubbles():
#     # pygame.time.wait(1500) #создает делэй между разными пузырьками
#     bubblex = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
#     bubbley = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0
#     bubble_size = random.randrange(20, 70)
#     bi = pygame.transform.scale(bubble_img, (bubble_size, bubble_size))
#     # size_load = []
#     # for i in range(5):
#     #     if i < 3:
#     #         bubble_size += 5
#     #     else:
#     #         bubble_size -= 5
#     #     size_load.append(bubble_size)
#     # bi_load =[]
#     # for j in size_load:
#     #     bi = pygame.transform.scale(bubble_img, (j, j))
#     #     bi_load.append(bi)
#     screen.blit(bi, [bubblex, bubbley, 10, 10])
#     pygame.display.update()
#     return
#     # for g in bi_load:
#     #     screen.blit(g,[bubblex, bubbley, 10, 10])
#
# while True:
#     pygame.time.wait(1500)
#     Bubbles()
#     pygame.display.update()


# '''тестовый запуск. ап - отжатие'''
# x, y = 300, 420
# move_x, move_y = 0, 0
# while True:
#     # event = pygame.event.wait()
#     # event_text.append(str(event))
#     # event_text = event_text[-screen_size[1]/font_height:]
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT:
#                 move_x = -1
#             elif event.key == K_RIGHT:
#                 move_x = +1
#             elif event.key == K_UP:
#                 move_y = -1
#             elif event.key == K_DOWN:
#                 move_y = +1
#         elif event.type == KEYUP:
#             if event.key == K_LEFT:
#                 move_x = 0
#             elif event.key == K_RIGHT:
#                 move_x = 0
#             elif event.key == K_UP:
#                 move_y = 0
#             elif event.key == K_DOWN:
#                 move_y = 0
#     x += move_x
#     y += move_y
#     # screen.fill((0, 0, 0))
#     # screen.fill(light_blue)
#     screen.blit(background, (0, 0))
#     screen.blit(mouse_cursor, (x, y))
#     Bubbles()
#     clock.tick(cat_speed)
#     pygame.display.update()
