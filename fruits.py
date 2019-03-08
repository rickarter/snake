import pygame
import random


class Fruits:
    def __init__(self):
        self.X = random.randint(0, 490)
        self.Y = random.randint(0, 490)
        self.width = 10
        self.height = 10

    def create_fruit(self, win):
        pygame.draw.rect(win, (255, 0, 100), (self.X, self.Y, self.width, self.height))

    def change_position(self):
        self.X = random.randint(0, 490)
        self.Y = random.randint(0, 490)