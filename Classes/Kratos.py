import math
import pygame as pg
import random


class Kratos(pg.sprite.Sprite):


    def __init__(self, x, y, image, speed = 3, size = 50):
        #cat speed lvl1 - 3, lvl2 - 4, lvl3 - 5
        pg.sprite.Sprite.__init__(self)

        self.size = size

        self.image = pg.transform.scale(image, (self.size, self.size))

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = speed


    def catch(self,y_change, image2):
        if y_change == 1:
            self.image = image2


    def move(self, x_change, image, y_change, image2):
        if x_change == 1:
            self.image = image
            self.rect.x += self.speed
            self.catch(y_change, image2)
        elif x_change == -1:
            self.image = pg.transform.flip(image, True, False)
            self.rect.x -= self.speed
            self.catch(y_change, image2)








