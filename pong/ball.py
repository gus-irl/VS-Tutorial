import pygame
from random import randint
BLACK = (0,0,0)



class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width ,height): 
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.ball_rotation = 10
        pygame.draw.rect(self.image, color, [0,0,width, height], 0, 0)




        self.speed = 3
        self.speed_multiplier = 0
        self.original_velocity = [self.speed, randint(4,8)]
        self.velocity = [self.speed, randint(0,0)]

        self.rect = self.image.get_rect()

    def rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pg.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect
    def update(self):
        # self.ball_rotation += 1

        # rotate

        # lastPos = self.image.get_rect().center

        # rotated_ball = pygame.transform.rotate(self.image, 45)
        # rotated_ball.get_rect().center = lastPos
        # self.image = rotated_ball
        # self.rect.x = lastPos[0] - 5
        # self.rect.y = lastPos[1] - 5

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


        # rotated_ball_rect = rotated_ball.get_rect(center = (self.rect.x, self.rect.y))
        
        # self.rect = rotated_ball_rect





    def bounce(self, score = 1, direction = False, hit_paddle = False, screen_size_x = 0):


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

        if (hit_paddle):
            if (direction == "Right"):
                # self.velocity[0] = -self.original_velocity[0]
                # self.velocity[0] = -self.velocity[0]
                self.rect.x = screen_size_x - 30
                # self.speed_multiplier = 0
                # self.original_velocity[0] -= self.speed_multiplier
            elif (direction == "Left"):
                # self.velocity[0] = self.original_velocity[0]
                # self.velocity[0] = self.velocity[0]
                self.rect.x = 30
                # self.speed_multiplier = 0
            if (self.speed_multiplier < 2):
                self.speed_multiplier += .2
                self.velocity[0] += self.speed_multiplier
        else:
            self.speed_multiplier = 0
            # self.velocity[0] = self.original_velocity[0]
            if (direction == "Right"):
                self.velocity[0] = self.original_velocity[0]
                # self.velocity[0] = self.velocity[0]
                self.rect.x = self.rect.x - 20
                # self.speed_multiplier = 0
                # self.original_velocity[0] -= self.speed_multiplier
            elif (direction == "Left"):
                self.velocity[0] = -self.original_velocity[0]
                # self.velocity[0] = -self.velocity[0]
                self.rect.x = self.rect.x + 20
                # self.speed_multiplier = 0
                # self.original_velocity[0] += self.speed_multiplier
            # elif (self.speed_multiplier < 2):
            #     self.speed_multiplier += 0.2

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