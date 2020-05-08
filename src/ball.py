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
        self.velocity = []

    def draw(self, window):
        pass

    def move(self):
        pass

    def bounce(self):
        pass
