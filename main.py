from time import time
import pygame
import sys
import os

from pygame.locals import *

pygame.init() 

class ScrollingBackground:
    def __init__(self, screenheight, imagefile):
        self.img = pygame.image.load(imagefile)
        self.coord = [0,0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]
    def Show(self, surface):
        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)
    def UpdateCoords(self, speed_y, time):
        distance_y = speed_y * time
        self.coord[1] += distance_y
        self.coord2[1] += distance_y
        if self.coord2[1] >= 0:
            self.coord[1] = self.y_original
            self.coord2[1] = self.y2_original



clock = pygame.time.Clock()

screenwidth, screenheight = (480, 600)

framerate = 60

bg_speed = 100

screen = pygame.display.set_mode((screenwidth,screenheight)) # Sets app resolution

StarField = ScrollingBackground(screenheight, "background.png")

pygame.mouse.set_visible(0) # Hide Cursor, uses number as input

# pygame.display.flip()

pygame.display.set_caption("spAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAce") # Set the title of the game

open = True
while open:
    time = clock.tick(framerate) / 1000.0
    StarField.UpdateCoords(bg_speed, time)
    StarField.Show(screen)
    pygame.display.update()

    x,y = pygame.mouse.get_pos() # Keep track of mouse position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
    screen.fill((0,0,0))
    # screen.blit(bg, (0,0))
pygame.quit()
quit()