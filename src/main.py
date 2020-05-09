# Simple python pong game using pygame
# Written by Achintya Mathur
# Date: 7/05/2020

import pygame
from pygame.locals import *
import sys

pygame.init()
clock = pygame.time.Clock()

window_width = 700
window_height = 600
dimensions = (window_width, window_height)
frameRate = 35

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

window = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Pong")


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
        self.y -= self.velocity
        if self.y <= 0:
            self.y = 0

    def moveDown(self):
        self.y += self.velocity
        if self.y + self.height >= window_height:
            self.y = window_height - self.height


ball = pygame.Rect(window_width / 2 - 10, window_height / 2 - 10, 20, 20)
ball_x_velocity = 8
ball_y_velocity = 8
player = Paddle(10, window_height / 2 - 50, 25, 100, green)
opponent = Paddle(window_width - 35, window_height / 2 - 50, 25, 100, green)


def refresh():
    window.fill(black)
    pygame.draw.line(window, white, (window_width / 2, 0),
                     (window_width / 2, window_height), 3)
    pygame.draw.ellipse(window, red, ball)
    player.draw(window)
    opponent.draw(window)
    ball.x += ball_x_velocity
    ball.y += ball_y_velocity


running = True
while running:

    clock.tick(frameRate)

    events = pygame.event.get()
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if ball.top <= 0 or ball.bottom >= window_height:
        ball_y_velocity *= -1

    if ball.left <= 0 or ball.right >= window_width:
        ball_x_velocity *= -1

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if keys[pygame.K_UP]:
                player.moveUp()

            if keys[pygame.K_DOWN]:
                player.moveDown()

            if keys[pygame.K_w]:
                opponent.moveUp()

            if keys[pygame.K_s]:
                opponent.moveDown()

    refresh()
    pygame.display.update()

pygame.display.quit()
sys.exit()
