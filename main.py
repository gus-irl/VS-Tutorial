import pygame
import sys
import os

from pygame.locals import *

pygame.init() 

class ScrollingBackground:
    def __init__(self, screenheight, screenwidth):
        self.img = pygame.image.load(imagefile)
        self.coord = [0,0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]
    def Show(self, surface):
        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((900,800)) # Sets app resolution

bg = pygame.image.load(os.path.join("./", "background.png"))

pygame.mouse.set_visible(0) # Hide Cursor, uses number as input

pygame.display.flip()

pygame.display.set_caption("spAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAce") # Set the title of the game

open = True
while open:
    pygame.display.update()
    x,y = pygame.mouse.get_pos() # Keep track of mouse position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
    screen.fill((0,0,0))
    clock.tick(60)
    screen.blit(bg, (0,0))
pygame.quit()
quit()