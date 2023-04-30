import pygame
from pygame.locals import *
from sys import exit
import random
from Classes import Vector2, Bubble

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

black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (240,248,255)
yellow = (255, 255, 102)

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []
text_surface = font.render("Pygame is cool!", False, (0,0,0), (255, 255, 255))

# pygame.time.set_timer(pygame.USEREVENT, 3000)
clock = pygame.time.Clock()
cat_block = 10
cat_speed = 250

bubblex = round(random.randrange(0, dis_width - cat_block) / 10.0) * 10.0
bubbley = round(random.randrange(0, dis_height - cat_block) / 10.0) * 10.0


def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width / 6, dis_height / 3])

# def Bubbles():
#     # pygame.time.wait(1500) #создает делэй между разными пузырьками
#     # pygame.time.delay(1500)
#     bubblex = round(random.randrange(0, dis_width - cat_block) / 10.0) * 10.0
#     bubbley = round(random.randrange(0, dis_height - cat_block) / 10.0) * 10.0
#     bubble_size = random.randrange(20, 70)
#     size_load = []
#     for i in range(5):
#         if i < 3:
#             bubble_size += 5
#         else:
#             bubble_size -= 5
#         size_load.append(bubble_size)
#     bi_load =[]
#     for j in size_load:
#         bi = pygame.transform.scale(bubble_img, (j, j))
#         bi_load.append(bi)
#     for g in bi_load:
#         pygame.time.delay(1500)
#         screen.blit(g,[bubblex, bubbley, cat_block, cat_block])

# def bubbles(num):
#     bubbles_array = []
#     if len(bubbles_array) != num:
#         for i in range(num-len(bubbles_array)):
#             bubblex = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
#             bubbley = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0
#             bubble_size = random.randrange(20, 70)
#             if bubble_size<35:
#                 bspeed =450 #100-150-120
#             elif bubble_size>55:
#                 bspeed = 750
#             else:
#                 bspeed = 600
#             bi = pygame.transform.scale(bubble_img, (bubble_size, bubble_size))
#             bubbles_array.append([bi, bubblex, bubbley, bspeed])
#     return bubbles_array

# def bubbles():
#     bubble_size = random.randrange(20, 70)
#     bubblex = round(random.randrange(bubble_size, dis_width - bubble_size) / 10.0) * 10.0
#     bubbley = round(random.randrange(0, dis_height - 430) / 10.0) * 10.0
#     if bubble_size < 35:
#         bspeed = 450  # 100-150-120
#     elif bubble_size > 55:
#         bspeed = 750
#     else:
#         bspeed = 600
#     bi = pygame.transform.scale(bubble_img, (bubble_size, bubble_size))
#     return bi, bubblex, bubbley, bspeed

def bubbles():
    bsize = random.randrange(20, 70)
    bubblex = round(random.randrange(bsize, dis_width - bsize) / 10.0) * 10.0
    bubbley = round(random.randrange(0, dis_height - 430) / 10.0) * 10.0
    bubble = Bubble(bubblex, bubbley, bsize)
    return bubble


    # bubls = pygame.sprite.Group()
    # bubbles_array = []
    # for i in range(num):
    #     bsize = random.randrange(20, 70)
    #     bubblex = round(random.randrange(bsize, dis_width - bsize) / 10.0) * 10.0
    #     bubbley = round(random.randrange(0, dis_height - 430) / 10.0) * 10.0
    #     bubbles_array.append(Bubble(bubblex, bubbley, bubls, bsize))



def gameloop(num):
    game_over = False
    game_close = False
    # x1 = dis_width / 2
    # y1 = 100
    # x, y = 300, 420
    x, y = dis_width, dis_height
    x_change, y_change = 0, 0
    # bubls = pygame.sprite.Group()
    bubbles_array = []
    for i in range(num):
        bubbles_array.append(bubbles())
    while not game_over:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        x_change = -1
                    elif event.key == K_RIGHT:
                        x_change = +1
            x += x_change
            y += y_change
            screen.blit(background, (0, 0))
            # for b in bubbles_array:
            #     i = 0
            #     for i in range(5):
            #         screen.blit(b[0], (b[1], b[2]))
            #         time_passed = clock.tick(b[3])
            #         time_passed_seconds = time_passed / 1000.0
            #         distance_moved = time_passed_seconds * b[3]
            #         b[2] += distance_moved
            #         if b[2] > 480:
            #             b[2] -= 480
            # bubls.draw(screen)
            for b in bubbles_array:
                screen.blit(b.image, b.rect)
                time_passed = clock.tick(b.speed)
                time_passed_seconds = time_passed / 1000.0
                distance_moved = time_passed_seconds * b.speed
                b.rect.y += distance_moved
                print(b,  b.speed,    b.rect.y)
                if b.rect.y > 480:
                    bubbles_array.remove(b)
                    b.kill()
                    new_bubble = bubbles()
                    bubbles_array.append(new_bubble)
            pygame.display.update()
            screen.blit(mouse_cursor, (x, y))
            # clock.tick(cat_speed) #cкорость движения кота зависит от скорости пузыря
            # pygame.display.update()
    pygame.quit()
    quit()


gameloop(3)

