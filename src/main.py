# Simple python pong game using pygame
# Written by Achintya Mathur
# Date: 7/05/2020

import pygame
from pygame.locals import *
from random import randint
import sys

pygame.init()
clock = pygame.time.Clock()

window_width = 700
window_height = 600
dimensions = (window_width, window_height)
frameRate = 35

bgcolor = (25, 25, 25)
ball_color = (randint(0, 255), randint(0, 255), randint(0, 255))
paddle_color = (randint(0, 255), randint(0, 255), randint(0, 255))
line_color = (randint(0, 255), randint(0, 255), randint(0, 255))

window = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Pong, FPS: " + str(int(clock.get_fps())))

player = pygame.Rect(10, window_height / 2 - 50, 26, 100)
opponent = pygame.Rect(window_width - 36, window_height / 2 - 50, 26, 100)
paddle_velocity = 35

ball = pygame.Rect(window_width / 2 - 10, window_height / 2 - 10, 20, 20)
ball_x_velocity = 8
ball_y_velocity = 8


def draw_paddles():
    pygame.draw.rect(window, paddle_color, player)
    pygame.draw.rect(window, paddle_color, opponent)


def move_player_paddle_up():
    if player.top <= 0:
        player.top = 0
    player.top -= paddle_velocity


def move_opponent_paddle_up():
    if opponent.top <= 0:
        opponent.top = 0
    opponent.top -= paddle_velocity


def move_player_paddle_down():
    if player.bottom >= window_height:
        player.bottom = window_height
    player.bottom += paddle_velocity


def move_opponent_paddle_down():
    if opponent.bottom >= window_height:
        opponent.bottom = window_height
    opponent.bottom += paddle_velocity


def draw_ball():
    pygame.draw.ellipse(window, ball_color, ball)


def move_ball():
    ball.x += ball_x_velocity
    ball.y += ball_y_velocity


def refresh():
    window.fill(bgcolor)
    pygame.draw.line(window, line_color, (window_width / 2, 0),
                     (window_width / 2, window_height), 3)
    draw_paddles()
    draw_ball()
    move_ball()


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

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_x_velocity *= -1

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if keys[pygame.K_UP]:
                move_player_paddle_up()

            if keys[pygame.K_DOWN]:
                move_player_paddle_down()

            if keys[pygame.K_w]:
                move_opponent_paddle_up()

            if keys[pygame.K_s]:
                move_opponent_paddle_down()

    refresh()
    pygame.display.update()

pygame.display.quit()
sys.exit()
