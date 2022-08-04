import pygame
BLACK = (0,0,0)
window_size = [700,700]


class Paddle(pygame.sprite.Sprite): # Paddle object
    def __init__(self, color, width, height):
        super().__init__() # Learn more about super cuz idk what this doing here man
        # self == the current class (I think)
        self.image = pygame.Surface([width, height]) # Image resolution
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.height = height
        self.color = color
        # self.red = 255
        # self.green = 255
        # self.blue = 255
        pygame.draw.rect(self.image, self.color, [0, 0, width, height], 0, 1000) # Draw the paddle

        self.rect = self.image.get_rect() # Get rectangle object that has the dimensions of the image (?)
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Check to not go off screen
        if self.rect.y < 0:
            self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        if (self.rect.y > window_size[1] - self.height):
            self.rect.y = window_size[1] - self.height