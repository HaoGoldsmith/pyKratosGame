import math
import pygame as pg
import random


class Bubble(pg.sprite.Sprite):

    def __init__(self, x, y, size, group, image, W):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(image, (size, size))

        self.rect = self.image.get_rect(center=(x, y))

        self.add(group)

        self.size = size

        scales = (0.03, 0.045, 0.06, 0.075, 0.09, 0.105)
        if size in range(int(W*scales[0]), int(W*scales[1])):
            self.speed = 5  # 50-100-75
        elif size in range(int(W*scales[1]), int(W*scales[2])):
            self.speed = 8
        elif size in range(int(W*scales[2]), int(W*scales[3])):
            self.speed = 10
        elif size in range(int(W*scales[3]), int(W*scales[4])):
            self.speed = 12
        else:
            self.speed = 14


    def update(self, H, time_passed_seconds):
        distance_moved = time_passed_seconds * self.speed ** 2
        if self.rect.y < (H - self.size):
            self.rect.y += distance_moved
        else:
            self.kill()



