import math
import pygame as pg
import random


class Kratos(pg.sprite.Sprite):


    def __init__(self, x, y, image, speed = 5):
        pg.sprite.Sprite.__init__(self)

        self.size = 50

        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (self.size, self.size))

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = speed


    # def move(self, x_change, image):
    #     if x_change == 1:
    #         self.image = pg.image.load(image).convert_alpha() #каждый раз загружает, не лучше ли загрузить раз и поместить спрайты в список?
    #         self.rect.x += self.speed
    #     elif x_change == -1:
    #         self.image = pg.transform.flip(pg.image.load(image).convert_alpha(), True, False)
    #         self.rect.x -= self.speed
    #
    #
    # def catch(self, x_change, image, y_change, image2):
    #     if y_change == 1:
    #         self.image = pg.image.load(image2).convert_alpha()
    #     elif y_change == -1:
    #         self.move(x_change, image)


    def move(self, x_change, image, y_change, image2):
        if x_change == 1:
            self.image = pg.image.load(image).convert_alpha() #каждый раз загружает, не лучше ли загрузить раз и поместить спрайты в список?
            self.rect.x += self.speed
            if y_change == 1:
                self.image = pg.image.load(image2).convert_alpha()

        elif x_change == -1:
            self.image = pg.transform.flip(pg.image.load(image).convert_alpha(), True, False)
            self.rect.x -= self.speed
            if y_change == 1:
                self.image = pg.image.load(image2).convert_alpha()





