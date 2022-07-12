import pygame
from random import randint
BLACK = (0,0,0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, color, size):
        super().__init__()


        self.image = pygame.Surface([size, size])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,size,size], 0, 10 )

        if (player == "A"):
            self.velocity = [-4, 0]
        else:
            self.velocity = [4, 0]

        self.rect = self.image.get_rect()