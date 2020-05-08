# Simple python pong game using pygame
# Written by Achintya Mathur
# Date: 7/05/2020

import pygame
from pygame.locals import *
from players import Paddle
import sys

pygame.init()

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
window.fill(black)
pygame.draw.line(window, white, (width / 2, 0), (width / 2, height), 3)

player = Paddle(10, height / 2 - 50, 25, 100, green)
opponent = Paddle(width - 35, height / 2 - 50, 25, 100, green)
player.draw(window)
opponent.draw(window)


running = True
clock = pygame.time.Clock()
while running:

    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if keys[pygame.K_UP]:
                player.moveUp()

            if keys[pygame.K_DOWN]:
                player.moveDown()

            if keys[pygame.K_RIGHT]:
                opponent.moveUp()

            if keys[pygame.K_LEFT]:
                opponent.moveDown()

    pygame.display.update()
    clock.tick(frameRate)

pygame.display.quit()
sys.exit()
