import pygame
from pygame.locals import *
from sys import exit
import random

# from Classes import Vector2, Bubble
#
background_image_filename = '1671682721_kalix-club-p-fon-dlya-prezentatsii-milnie-puziri-krasiv-41.jpg'
mouse_image_filename = 'Kratos.png'
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
my_clock = pygame.time.Clock()
my_clock.tick(60)


class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
           self.anim_frame_count = (self.anim_frame_count + 1 ) % 60
           self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0,
                       50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)

    def contains_point(self, pt):
         """ Return True if my sprite rectangle contains  pt """
         (my_x, my_y) = self.posn
         my_width = self.image.get_width()
         my_height = self.image.get_height()
         (x, y) = pt
         return ( x >= my_x and x < my_x + my_width and
                  y >= my_y and y < my_y + my_height)

    def handle_click(self):
         if self.anim_frame_count == 0:
            self.anim_frame_count = 5

# Load the sprite sheet
all_sprites = []
duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")

# Instantiate two duke instances, put them on the chessboard
duke1 = DukeSprite(duke_sprite_sheet,(10, 0))
duke2 = DukeSprite(duke_sprite_sheet,(100, 50))

# Add them to the list of sprites which our game loop manages
all_sprites.append(duke1)
all_sprites.append(duke2)

while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict["pos"]
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

            # Ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()

        # Draw a fresh background (a blank chess board)
        # ... same as before ...

        # Ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(screen)

        pygame.display.flip()