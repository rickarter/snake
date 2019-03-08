import pygame
from control import Control
from snake import Snake
from fruits import Fruits

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption(('Snake'))

control = Control()
snake = Snake()
fruits = Fruits()

while control.flag_games:
    if control.flag_pause:
        pygame.time.delay(1)
        control.control()
        win.fill((0, 0, 0))

        snake.draw(win)
        snake.move(control)
        snake.transform()
        snake.animation()

        fruits.create_fruit(win)

    else:
        control.on_pause()