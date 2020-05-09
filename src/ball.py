import pygame
from pygame.locals import *

pygame.init()
window_width = 700
window_height = 600


class Ball(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.xv = 8
        self.yv = 8

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def bounce(self):
        pass
