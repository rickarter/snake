import pygame
import time

class Snake:
    def __init__(self):
        self.head = [45, 45]
        self.speed = 10
        self.body = [[45, 45], [45, 45], [45, 45], [45, 45]]

    def move(self, control):
        if control.flag_direction == 'RIGHT':
            self.head[0] += self.speed
        elif control.flag_direction == 'LEFT':
            self.head[0] -= self.speed
        elif control.flag_direction == 'UP':
            self.head[1] -= self.speed
        elif control.flag_direction == 'DOWN':
            self.head[1] += self.speed


    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw(self, win):
        for segment in self.body:
            pygame.draw.rect(win, (0, 255, 100), (segment[0], segment[1], 10, 10))

    def transform(self):
        if self.head[0] >  500:
            self.head[0] = 0
        elif self.head[0] <  0:
            self.head[0]= 500
        elif self.head[1] < 0:
            self.head[1] = 500
        elif self.head[1] >  500:
            self.head[1] = 0

    def fruit_eaten(self, fruits):
        if fruits.X >= self.head[0] and fruits.X <= (self.head[0] + 10) and fruits.Y >= (self.head[1] - 10) and fruits.Y <= self.head[1]:
            return fruits.change_position()


