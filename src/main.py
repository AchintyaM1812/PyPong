# Simple python pong game using pygame
# Written by Achintya Mathur
# Date: 7/05/2020

import pygame
from pygame.locals import *
from players import Paddle
import sys

pygame.init()
clock = pygame.time.Clock()

width = 700
height = 600
dimensions = (width, height)
frameRate = 60

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

window = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Pong")


def refresh():
    window.fill(black)
    pygame.draw.line(window, white, (width / 2, 0), (width / 2, height), 3)
    player.draw(window)
    opponent.draw(window)


player = Paddle(10, height / 2 - 50, 25, 100, green)
opponent = Paddle(width - 35, height / 2 - 50, 25, 100, green)

running = True
while running:

    clock.tick(frameRate)

    events = pygame.event.get()
    pygame.event.pump()
    keys = pygame.key.get_pressed()

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
