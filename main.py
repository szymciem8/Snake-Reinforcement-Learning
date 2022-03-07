import pygame
from colors import *
from net import *
from snake import *
import time

# Constants
WIDTH, HEIGHT = 600, 600

pygame.init()
pygame.display.set_caption('Snake Reinforcement Learning')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(GRAY)

clock = pygame.time.Clock()

net = Net(screen, 30)
snake = Snake(screen, net, 1)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.set_dir()
    snake.add_seg()

    snake.move()
    snake.draw_game()

    clock.tick(10)
    pygame.display.update()