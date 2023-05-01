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

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (240, 248, 255)
yellow = (255, 255, 102)

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []
text_surface = font.render("Pygame is cool!", False, (0, 0, 0), (255, 255, 255))

pygame.time.set_timer(pygame.USEREVENT, 500)
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


def bubbles(group):
    bsize = random.randrange(20, 70)
    bubblex = round(random.randrange(bsize, dis_width - bsize) / 10.0) * 10.0
    bubbley = round(random.randrange(0, dis_height - 430) / 10.0) * 10.0
    bubble = Bubble(bubblex, bubbley, bsize, group)
    return bubble


def bubble_collision(main_list, second_list, group, num=1):
    # проверка на то ,что они листы + трай кэтч
    while len(main_list) < num:
        if len(main_list) == 0:
            new_bubble = bubbles(group)
            main_list.append(new_bubble)
            second_list.append(new_bubble.rect)
        else:
            new_bubble = bubbles(group)
            collision = new_bubble.rect.collidelist(second_list)
            if collision != -1:
                new_bubble.kill()
            else:
                main_list.append(new_bubble)
                second_list.append(new_bubble.rect)
    return


def gameloop(num):
    game_over = False
    game_close = False
    x, y = dis_width, dis_height
    x_change, y_change = 0, 0
    bubls = pygame.sprite.Group()
    bubbles_array = []
    bubbles_rects = []
    if num > 10:
        num = 10
    bfirst = bubbles(bubls)
    bubbles_array.append(bfirst)
    # bubble_collision(bubbles_array, bubbles_rects, bubls)  # cоздаем самый первый пузырик
    time_passed = clock.tick(144)
    time_passed_seconds = time_passed / 1000.0
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
                if event.type == USEREVENT:
                    if num > len(bubbles_array):
                        i = bubbles(bubls)
                        bubbles_array.append(i)
                    # if len(bubbles_array) < 4:
                    #     print (bubbles_array)
                    #     print(len(bubbles_array))
                    #     bubble_collision(bubbles_array, bubbles_rects, bubls, 3)
            x += x_change
            y += y_change
            screen.blit(background, (0, 0))
            bubls.draw(screen)
            pygame.display.update()
            pygame.time.delay(20)
            bubls.update(dis_height, time_passed_seconds)
            for b in bubbles_array:
                distance_moved = time_passed_seconds * b.speed  # 60
                if b.rect.y < 480:
                    b.rect.y += distance_moved
                else:
                    bubbles_array.remove(b)
                    b.kill()
                    bubble_collision(bubbles_array, bubbles_rects, bubls, num)
            # for b in bubbles_array:
            #     time_passed = clock.tick(144)
            #     time_passed_seconds = time_passed / 1000.0
            #     distance_moved = time_passed_seconds * b.speed ** 2  # 60
            #     if b.rect.y < 480:
            #         b.rect.y += distance_moved
            #     else:
            #         bubbles_array.remove(b)
            #         b.kill()
            #         bubble_collision(bubbles_array, bubbles_rects, bubls, num)
            # pygame.display.update()
            # pygame.time.delay(20)
            screen.blit(mouse_cursor, (x, y))
            # clock.tick(cat_speed) #cкорость движения кота зависит от скорости пузыря
            # pygame.display.update()
    pygame.quit()
    quit()


gameloop(7)
