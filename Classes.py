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

    def __init__(self, x, y, size, group=None, image = 'bubble.png'):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (size, size))

        self.rect = self.image.get_rect(center=(x, y))

        self.x_coordinate = x

        self.y_coordinate = y

        # self.add(group)

        self.size = size

        if size < 35:
            self.speed = 50  # 100-150-120
        elif size > 55:
            self.speed = 100
        else:
            self.speed = 75


    def update(self, H, distance_moved=None):
        # self.rect.y += distance_moved
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()

