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