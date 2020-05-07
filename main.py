# Simple python pong game using pygame
# Written by Achintya Mathur
# Date: 7/05/2020

import pygame
import sys
from paddle import Paddle

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

player = Paddle(0, height / 2, 25, 75, green)
opponent = Paddle(width, heigth / 2, 25, 75, green)
player.draw(window)
opponent.draw(window)

running = True
clock = pygame.time.Clock()
while running:

    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    pygame.event.pump()

    for event in events:
        if event == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(frameRate)

pygame.quit()
sys.exit()
