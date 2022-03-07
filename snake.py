from dataclasses import dataclass
from matplotlib.pyplot import draw
import pygame
import random
from colors import *
from dataclasses import dataclass

@dataclass
class Segment:
    x: int
    y: int


class Snake:

    def __init__(self,
                surface,
                net,
                freq
                ):

        self.surface = surface
        self.net = net
        self.size = net.block_size
        self.net_size = (net.n_blocks_in_x*self.size, net.n_blocks_in_y*self.size)

        self.head = Segment(
            x = random.randint(0, net.n_blocks_in_x) * self.size,
            y = random.randint(0, net.n_blocks_in_y) * self.size
        )
        self.segments = []

        self.freq = freq
        self.vx = 0
        self.vy = 0
        
        self.apple = Segment(
            random.randint(0, self.net.n_blocks_in_y-1) * self.size,
            random.randint(0, self.net.n_blocks_in_y-1) * self.size
        )

        self.draw_apple()
        print(self.apple)

        pygame.draw.rect(self.surface,
                        DARK_GREEN,
                        pygame.Rect(self.head.x, self.head.y, self.size, self.size))


    def set_dir(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.vx = 0
            self.vy = -1
        elif keys[pygame.K_DOWN]:
            self.vx = 0
            self.vy = 1
        elif keys[pygame.K_RIGHT]:
            self.vx = 1
            self.vy = 0
        elif keys[pygame.K_LEFT]:
            self.vx = -1
            self.vy = 0

    def move(self):
        self.head.x += self.vx * self.size
        self.head.y += self.vy * self.size

        if self.head.x > self.net_size[0]-self.size:
            self.head.x = 0

        if self.head.x < 0:
            self.head.x = self.net_size[0]-self.size
        
        if self.head.y > self.net_size[1]-self.size:
            self.head.y = 0

        if self.head.y < 0:
            self.head.y = self.net_size[1]-self.size


    def add_seg(self):
        if self.apple.x == self.head.x and self.apple.y == self.head.y:
            self.apple_new_pos()
            self.segments.append(Segment(0,0))

    def draw_snake(self):
        self.surface.fill(GRAY)
        pygame.draw.rect(self.surface,
                        DARK_GREEN,
                        pygame.Rect(self.head.x, self.head.y, self.size, self.size))

        for segment in self.segments:
            pygame.draw.rect(self.surface,
                        DARK_GREEN,
                        pygame.Rect(segment.x, segment.y, self.size, self.size))

    def apple_new_pos(self):
        self.apple.x = random.randint(0, self.net.n_blocks_in_y-1) * self.size
        self.apple.y = random.randint(0, self.net.n_blocks_in_y-1) * self.size

    def draw_apple(self):
        pygame.draw.rect(self.surface,
                        RED,
                        pygame.Rect(self.apple.x, self.apple.y, self.size, self.size))

    def draw_game(self):
        self.draw_snake()
        self.draw_apple()