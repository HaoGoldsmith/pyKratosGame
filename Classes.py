import math
import pygame as pg
import random


class Vector2(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2):
        return Vector2(P2.x - P1.x, P2.y - P1.y)

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude


class Bubble(pg.sprite.Sprite):

    def __init__(self, x, y, size, group, image='bubble.png'):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (size, size))

        self.rect = self.image.get_rect(center=(x, y))

        # self.x_coordinate = x
        #
        # self.y_coordinate = y

        self.add(group)

        self.size = size

        if size in range(20, 30):
            self.speed = 10  # 50-100-75
        elif size in range(30, 40):
            self.speed = 15
        elif size in range(40, 50):
            self.speed = 20
        elif size in range(50, 60):
            self.speed = 25
        else:
            self.speed = 30

    # def update(self, H, time_passed_seconds):
    #     # self.rect.y += distance_moved
    #     distance_moved = time_passed_seconds * self.speed ** 2  # 60
    #     # if self.rect.y < (H-self.size):
    #     if self.rect.y < (H - self.size*1.2): #размер модельки курсора?
    #         self.rect.y += distance_moved
    #     elif (H - self.size*1.2) <= self.rect.y <= (H - self.size):
    #         self.image = pg.transform.scale(pg.image.load('bubble1.png').convert_alpha(), (self.size, self.size))
    #         self.rect.y += distance_moved
    #     else:  #часть долетает до края до того, как выполнится второе условие
    #         self.kill()


    def update(self, H, time_passed_seconds):
        # self.rect.y += distance_moved
        distance_moved = time_passed_seconds * self.speed ** 2  # 60
        if self.rect.y < (H-self.size):
            self.rect.y += distance_moved
        else:  #часть долетает до края до того, как выполнится второе условие
            self.kill()
