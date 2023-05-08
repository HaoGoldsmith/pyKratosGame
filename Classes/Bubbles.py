import math
import pygame as pg
import random


class Bubble(pg.sprite.Sprite):

    def __init__(self, x, y, size, group, image):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(image, (size, size))

        self.rect = self.image.get_rect(center=(x, y))

        self.add(group)

        self.size = size

        self.pop = 0


        if size in range(20, 30):
            self.speed = 5  # 50-100-75
        elif size in range(30, 40):
            self.speed = 8
        elif size in range(40, 50):
            self.speed = 10
        elif size in range(50, 60):
            self.speed = 12
        else:
            self.speed = 14

    def update(self, H, time_passed_seconds, image):
        # self.image = pg.transform.scale(image, (self.size, self.size))
        distance_moved = time_passed_seconds * self.speed ** 2
        if self.rect.y < (H - self.size):
            self.rect.y += distance_moved
        else:
            self.kill()

        if self.pop != 0:
            self.image = pg.transform.scale(image, (self.size, self.size))

