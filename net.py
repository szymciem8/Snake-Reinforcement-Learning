import pygame
import math

class Net:

    def __init__(self, surface, n_blocks):
        self.surface = surface

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.block_size = self.width/n_blocks
        self.n_blocks_in_x = n_blocks
        self.n_blocks_in_y = math.floor(self.height/self.block_size)

        self.x_hover = 0
        self.y_hover = 0

        #Creation of a net
        for i in range(self.n_blocks_in_x):
            pygame.draw.line(surface,
                                pygame.Color(150,150,150),
                                [i*self.block_size, 0],
                                [i*self.block_size, self.height])
 
        for i in range(self.n_blocks_in_y):
            pygame.draw.line(surface,
                                pygame.Color(150,150,150),
                                [0, i*self.block_size],
                                [self.width, i*self.block_size])
