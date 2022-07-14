import pygame
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width ,height): 
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,width, height], 0, 10)

        self.speed = randint(2, 4)
        self.speed_multiplier = 1
        self.original_velocity = [self.speed, randint(4,8)]
        self.velocity = [self.speed, randint(0,0)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


    def bounce(self, score = 1, direction = False):
        # "Padding" to not cause bugginess (?)
        if (direction == "Right"):
            self.rect.x = self.rect.x + 20
            self.speed_multiplier = 0
            self.velocity[0] = -self.original_velocity[0]
            # self.original_velocity[0] -= self.speed_multiplier
        elif (direction == "Left"):
            self.rect.x = self.rect.x - 20
            self.speed_multiplier = 0
            self.velocity[0] = self.original_velocity[0]
            # self.original_velocity[0] += self.speed_multiplier
        else:
            self.speed_multiplier += 0.25
            # self.speed += self.speed_multiplier

        # print("Speed Multiplier: " + str(self.speed_multiplier))
        # print("Velocity: " + str(self.velocity))

        # self.original_velocity[0] = -(self.original_velocity[0] + self.speed_multiplier)
        # self.velocity[0] = -(self.velocity[0] + self.speed_multiplier)
            
        self.velocity[1] = randint(-8,8)

        if (self.velocity[0] > 0):
            self.velocity[0] = -(self.velocity[0] + self.speed_multiplier)
        else:
            self.velocity[0] = -(self.velocity[0] - self.speed_multiplier)

        # if (score % 3 == 0):
        #     self.velocity[0] = self.velocity[0] * 4
        # else:
        #     self.velocity[0] = self.original_velocity[0]
            

    def bounceY(self):
        if (self.velocity[1] > 0):
            self.rect.y = self.rect.y - 10
        else:
            self.rect.y = self.rect.y + 10
        self.velocity[1] = -self.velocity[1]