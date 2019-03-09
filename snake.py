import pygame


class Snake:
    def __init__(self):
        self.head = [10, 10]
        self.speed = 7
        self.body = [[10, 10]]
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
        if self.head[0] <= 0:
            self.head[0] = 490
        elif self.head[0] >= 500:
            self.head[0] = 0
        elif self.head[1] <= 0:
            self.head[1] = 490
        elif self.head[1] >= 500:
            self.head[1] = 0

    def fruit_eaten(self, fruits):
        if fruits.X <= self.head[0] <= fruits.X + fruits.width \
                and fruits.Y <= self.head[1] <= fruits.Y + fruits.height \
                or fruits.X <= self.head[0] <= fruits.X + fruits.width \
                and fruits.Y <= self.head[1] + self.height <= fruits.Y + fruits.height \
                or fruits.X <= self.head[0] + self.width <= fruits.X + fruits.width \
                and fruits.Y <= self.head[1] <= fruits.Y + fruits.height:
            self.grow()
            return fruits.change_position()

    def grow(self):
        self.body.append([-10, -10])

    def eat_oneself(self):
        count = 0
        for i in self.body:
            if i == self.head and count != 0:
                self.body = self.body[0:count:1]
            count += 1