# paddle class for the paddles to be drawn
# Written by Achintya Mathur
# Date: 7/05/2020

import pygame
from pygame.locals import *

pygame.init()

window_width = 700
window_height = 600


class Paddle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 7

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

    def moveUp(self):
        if self.y <= 0:
            self.y = y
        self.y -= self.velocity

    def moveDown(self):
        if self.y >= window_height:
            self.y = window_height
        self.y += self.velocity
