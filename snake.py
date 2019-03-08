import pygame
import time

class Snake:
    def __init__(self):
        self.head = [45, 45]
        self.speed = 10
        self.body = [[45, 45], [45, 45], [45, 45], [45, 45]]
        self.width = 10
        self.height = 10

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
            pygame.draw.rect(win, (0, 255, 100), (segment[0], segment[1], self.width, self.height))

    def transform(self):
        if self.head[0] >= 500:
            self.head[0] = 0
        elif self.head[0] <= 0:
            self.head[0] = 500
        elif self.head[1] <= 0:
            self.head[1] = 500
        elif self.head[1] >= 500:
            self.head[1] = 0

    def fruit_eaten(self, fruits):
        if self.head[0] >= fruits.X and self.head[0] <= fruits.X + fruits.width\
                and self.head[1] >= fruits.Y and self.head[1] <= fruits.Y + fruits.height\
                or self.head[0] >= fruits.X and self.head[0] <= fruits.X + fruits.width\
                and self.head[1] + self.height >= fruits.Y and self.head[1] + self.height <= fruits.Y + fruits.height\
                or self.head[0] + self.width >= fruits.X and self.head[0] + self.width <= fruits.X + fruits.width\
                and self.head[1] >= fruits.Y and self.head[1] <= fruits.Y + fruits.height:
                self.grow()
                return fruits.change_position()

    def grow(self):
        self.body.append([45, 45])


