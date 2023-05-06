import pygame
from pygame.locals import *
from sys import exit
import random
from Classes import Bubbles, Kratos

pygame.init()

'''screen'''
dis_width = 640
dis_height = 480
screen_size = (dis_width, dis_height)
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption("Catch the bubble")

'''image loads'''
background_image_filename = '1671682721_kalix-club-p-fon-dlya-prezentatsii-milnie-puziri-krasiv-41.jpg'
background = pygame.image.load(background_image_filename).convert()
cat_img = ['Kratos.png', 'nonono.png', 'byak.png', 'game_over.png', 'success.png']
cat_images_load = []
for image in cat_img:
    cat_images_load.append(pygame.image.load(image).convert_alpha())
cat_lose = Kratos.Kratos(dis_width / 2, dis_height / 2, cat_images_load[3], 0, 150)
cat_success = Kratos.Kratos(dis_width / 2, dis_height / 2, cat_images_load[4], 0, 150)
bubble_img = ['bubble.png', 'boom.png']
bubble_images_load = []
for img in bubble_img:
    bubble_images_load.append(pygame.image.load(img).convert_alpha())


'''colors'''
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (240, 248, 255)
yellow = (255, 255, 102)

'''fonts'''
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []
text_surface = font.render("Kratos is your emperor!", False, (0, 0, 0), (255, 255, 255))

'''clock'''
pygame.time.set_timer(pygame.USEREVENT, 500)
clock = pygame.time.Clock()


'''score text'''
def your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])


'''win or loss message'''
def message(msg, color, cat = cat_lose):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [20, cat.rect.y - dis_height / 10])
    screen.blit(cat.image, (cat.rect.x, cat.rect.y))


'''bubble creation'''
def bubbles(group):
    bsize = random.randrange(20, 70)
    bubblex = round(random.randrange(bsize, dis_width - bsize) / 10.0) * 10.0
    bubbley = round(random.randrange(0, dis_height - 430) / 10.0) * 10.0
    bubble = Bubbles.Bubble(bubblex, bubbley, bsize, group, bubble_images_load[0])
    return bubble


'''bubble collision - rewatch(rectcollide)!!!'''
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

    x, y = dis_width / 2, dis_height - 25
    cat = Kratos.Kratos(x, y, cat_images_load[0])
    x_change, y_change = 0, 0

    bubbles_popped = 0
    bubls = pygame.sprite.Group()
    bubbles_array = []
    bubbles_rects = []
    if num > 10:
        num = 10
    bfirst = bubbles(bubls)
    bubbles_array.append(bfirst)

    while not game_over:
        while game_close == True:
            screen.blit(background, (0, 0))
            if bubbles_popped < 20:
                message("Weakling! Press C to try again or ESC to lose your dignity", red)
            else:
                message("I am great hunter! Let's try again(C) or go to sleep(ESC)", red, cat_success)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                    game_close = False
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop(num)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                exit()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    y_change = -1
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_over = True
                elif event.key == K_LEFT:
                    x_change = -1
                elif event.key == K_RIGHT:
                    x_change = +1
                elif event.key == K_SPACE:
                    y_change = +1
            if event.type == USEREVENT:
                if num > len(bubbles_array):
                    i = bubbles(bubls)
                    bubbles_array.append(i)
        if cat.rect.x >= dis_width - cat.size or cat.rect.x < 0:
            game_close = True
        time_passed = clock.tick(60)
        time_passed_seconds = time_passed / 1000.0
        cat.move(x_change, cat_images_load[1], y_change, cat_images_load[2])
        screen.blit(background, (0, 0))
        screen.blit(cat.image, cat.rect)
        bubls.draw(screen)
        your_score(bubbles_popped)
        pygame.display.update()
        pygame.time.delay(25)
        bubls.update(dis_height, time_passed_seconds)
        for b in bubbles_array:
            print(f'{b.size},{b.speed}')
            distance_moved = time_passed_seconds * b.speed
            if b.rect.y < (480 - b.size):
                b.rect.y += distance_moved
                is_caught = pygame.Rect.colliderect(b.rect, cat.rect)
                if is_caught:
                    if keys[pygame.K_SPACE]:
                        b.image = pygame.transform.scale(bubble_images_load[1].convert_alpha(),
                                                         (b.size, b.size))  # do not working
                        bubbles_popped += 1
                        bubbles_array.remove(b)
                        b.kill()
                        bubble_collision(bubbles_array, bubbles_rects, bubls, num)
            else:
                bubbles_array.remove(b)
                b.kill()
                bubble_collision(bubbles_array, bubbles_rects, bubls, num)
    pygame.quit()
    quit()


gameloop(7)
