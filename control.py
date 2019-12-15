import pygame

from pygame.locals import *

class Control:
    def __init__(self):
        self.flag_games = True
        self.flag_direction = 'RIGHT'
        self.flag_pause = False
        self.timer = pygame.time.Clock()

    def control(self):
        self.timer.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_games = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.flag_direction != 'LEFT':
                    self.flag_direction = 'RIGHT'
                elif event.key == K_LEFT and self.flag_direction != "RIGHT":
                    self.flag_direction = 'LEFT'
                elif event.key == K_UP and self.flag_direction != "DOWN":
                    self.flag_direction = 'UP'
                elif event.key == K_DOWN and self.flag_direction != "UP":
                    self.flag_direction = 'DOWN'
                elif event.key == K_ESCAPE:
                    self.flag_games = False
                elif event.key == K_SPACE:
                    if self.flag_pause:
                        self.flag_pause = False
                    elif not self.flag_pause:
                        self.flag_pause = True
        pygame.display.update()

    def on_pause(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_games = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if self.flag_pause:
                        self.flag_pause = False
                    elif not self.flag_pause:
                        self.flag_pause = True

    def change_speed(self, snake):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            snake.speed = 1
        if keys[pygame.K_2]:
            snake.speed = 2
        if keys[pygame.K_3]:
            snake.speed = 3
        if keys[pygame.K_4]:
            snake.speed = 4
        if keys[pygame.K_5]:
            snake.speed = 5
        if keys[pygame.K_6]:
            snake.speed = 6
        if keys[pygame.K_7]:
            snake.speed = 7
        if keys[pygame.K_8]:
            snake.speed = 8
        if keys[pygame.K_9]:
            snake.speed = 9
        if keys[pygame.K_0]:
            snake.speed = 10
