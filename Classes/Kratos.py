import math
import pygame as pg
import random


class Kratos(pg.sprite.Sprite):


    def __init__(self, x, y, image, size, speed_scale = 0.06, anims = None):
        #cat speed lvl1 - 0.06, lvl2 - 0.08, lvl3 - 0.1
        pg.sprite.Sprite.__init__(self)

        self.size = size

        self.image = pg.transform.scale(image,(self.size, self.size))

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = size*speed_scale

        self.anim = anims
        self.frame = 0  # текущий кадр
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 60  # как быстро кадры меняются



    def catch(self,y_change, image2):
        if y_change == -1:
            self.image = pg.transform.scale(image2,(self.size, self.size))
        elif y_change == 1:
            self.image = pg.transform.flip(pg.transform.scale(image2,(self.size, self.size)), True, False)


    def walk(self, flip=False):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
            if flip:
                self.image = pg.transform.flip(pg.transform.scale(self.anim[self.frame],(self.size, self.size)), True, False)
            else:
                self.image = pg.transform.scale(self.anim[self.frame], (self.size, self.size))


    def move(self, x_change, y_change, image2):
        if x_change == 1:
            self.walk(False)
            self.rect.x += self.speed
            self.catch(y_change, image2)
        elif x_change == -1:
            self.walk(True)
            self.rect.x -= self.speed
            self.catch(-y_change, image2)


    def level_up(self, bubbles_popped):
        if 15 < bubbles_popped < 35:
            self.speed = self.size*0.08
        elif bubbles_popped > 35:
            self.speed = self.size*0.1
        else:
            self.speed = self.size*0.06






