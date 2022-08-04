# https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

import pygame
import os
from PIL import Image
pygame.init()
from paddle import Paddle
from ball import Ball
from bullet import Bullet
from random import randint


bg = (30,30,30)
fg = (255,255,255)

puased = False

paddle_speed = 6

scoreA = 0
scoreB = 0

red_opacity_A = 255
red_opacity_B = 255

# Open a new window
window_size = [900,700]
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600, 600)
# window_size = [70,50]
screen = pygame.display.set_mode((window_size[0], window_size[1]))
pygame.display.set_caption("pOOOOOOOOOOOOOOOOOOOOONg")


# Create the objects 

paddleA = Paddle(fg, 20, 100)
paddleA.rect.x = 0 # Setting Position
paddleA.rect.y = window_size[1] / 2

paddleB = Paddle((255,255,255), 20, 100)
paddleB.rect.x = window_size[0] - 20 # Setting Position
paddleB.rect.y = window_size[1] / 2


ball = Ball(fg, 10, 10)
ball.rect.x = 345
ball.rect.y = window_size[1] / 2

bulletA = Bullet("A", fg, 10)
bulletA.rect.x = -100
bulletA.rect.y = 0 

bulletB = Bullet("B", fg, 10)
bulletB.rect.x = -100
bulletB.rect.y = 0

# All the sprites in the game
all_sprites_list = pygame.sprite.Group() 
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


carryOn = True # Loop carries on until user exits
clock = pygame.time.Clock() # Control how fast the screen updates
        

def set_color(img, color):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            color.a = img.get_at((x, y)).a  # Preserve the alpha value.
            img.set_at((x, y), color)  # Set the color of the pixel.

# def fadeVar(object, _from, _to):
#     fade = _from
    


# MAIN LOOP
bulletAShot = False
bulletBShot = False

score_multiplier_text_color = (70,70,70)
score_multiplier_green = 255
last_multiplier = 0

scoreA_text_white = 255
scoreA_text_color = (scoreA_text_white, scoreA_text_white, scoreA_text_white)
scoreB_text_white = 255
scoreB_text_color = (scoreB_text_white, scoreB_text_white, scoreB_text_white)

ball_rotation = 0

direction_switch = True
while carryOn:
    for event in pygame.event.get(): # User did a something
        if event.type == pygame.QUIT: # User exited the game
            carryOn = False

        if event.type == pygame.KEYUP:
            if keys[pygame.K_SPACE]:
                if puased:
                    puased = False

                else:
                    bg_surface = pygame.Surface([window_size[0], window_size[1]])
                    bg_surface.fill((30,30,30))
                    bg_surface.set_alpha(200)

                    screen.blit(bg_surface, (0,0))

                    screen.blit(pygame.font.Font(None, int(window_size[0] / 4)).render("PAUSED", 1, (255,0,0)), (50, 50))

                    puased = True

    # Inputs
    keys = pygame.key.get_pressed()


    if not puased:
        # player A
        paddle_multiplier_A = 1
        # Boost
        if keys[pygame.K_LCTRL] or keys[pygame.K_LSHIFT]:
            # ball.image = pygame.transform.rotate(ball.image, ball.ball_rotation)
            if (red_opacity_A > 20):
                paddle_multiplier_A = 3
                red_opacity_A -= 8
        else:
            red_opacity_A = 255
        if keys[pygame.K_w]:
            paddleA.moveUp(paddle_speed * paddle_multiplier_A)
        if keys[pygame.K_s]:
            paddleA.moveDown(paddle_speed * paddle_multiplier_A)

        if keys[pygame.K_d] and not bulletAShot:
            bulletA.rect.x = 20
            bulletA.rect.y = paddleA.rect.x

        # player B
        paddle_multiplier_B = 1
        if keys[pygame.K_RCTRL] or keys[pygame.K_RSHIFT]:
            # ball.image = pygame.transform.rotate(ball.image, -ball.ball_rotation)
            if (red_opacity_B > 20):
                paddle_multiplier_B = 3
                red_opacity_B -= 8
        else:
            red_opacity_B = 255
        if keys[pygame.K_UP]:
            paddleB.moveUp(paddle_speed * paddle_multiplier_B)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(paddle_speed * paddle_multiplier_B)

        if keys[pygame.K_LEFT] and not bulletBShot:
            bulletB.rect.x = 200
            bulletB.rect.y = paddleB.rect.x

        # paddleA.color = ( 255, red_opacity_A, red_opacity_A)
        set_color(paddleA.image, pygame.Color( 255, red_opacity_A, red_opacity_A))
        set_color(paddleB.image, pygame.Color( 255, red_opacity_B, red_opacity_B))

        # Game Logic
        all_sprites_list.update() # Refresh list

        # if (ball.rect.x >= window_size[0]) or (ball.rect.x <= 0):
            # if (scoreA % 1 == 0) or (scoreB % 1 == 0):


        # Resize window effect
        # if (direction_switch):
        #     window_size[0] = window_size[0] - 1
        #     window_size[1] = window_size[1] - 1

        # else:
        #     window_size[0] = window_size[0] + 1
        #     window_size[1] = window_size[1] + 1

        # paddleB.rect.x = window_size[0] - 20 
        # pygame.display.set_mode((window_size[0], window_size[1]))

        # if (window_size[0] == 400):
        #     direction_switch = False
        # elif (window_size[0] == 900):
        #     direction_switch = True

        # Check if the ball bounces against the walls
        if ball.rect.x >= window_size[0]:
            scoreA += 1
            scoreA_text_color = (255,255,255)
            ball.bounce(scoreA, "Left")
            ball.speed_multiplier = 0
            scoreA_text_white = 255
            ball.rect.x = window_size[0] - 10
        if ball.rect.x <= 0:
            scoreB += 1
            scoreB_text_color = (255,255,255)
            ball.bounce(scoreB, "Right")
            scoreB_text_white = 255
            ball.rect.x = 10


        if ball.rect.y >= window_size[1]:
            ball.bounceY()
            ball.rect.y = window_size[1] - 10
        if ball.rect.y < 0:
            ball.bounceY()
            ball.rect.y = 10
        
        # ball.rect = pygame.transform.rotate(ball.image, 10)

        # Detect collisions between ball & paddles
        # if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        #     ball.bounce()
            # ball.speed_multiplier += 1

        if pygame.sprite.collide_mask(ball, paddleA):
            ball.bounce(1, "Left", True, window_size[0])
        elif pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce(1, "Right", True, window_size[0])



        # Visuals
        screen.fill(bg)
        # Display Scores
        if (scoreA_text_white > 50):
            scoreA_text_white -= 6
            scoreA_text_color = (scoreA_text_white, scoreA_text_white, scoreA_text_white)

        font = pygame.font.Font(None, int(window_size[0] / 2 + 50))
        text = font.render(str(scoreA), 0, scoreA_text_color)
        screen.blit(text, (window_size[0] / 20, window_size[1] / 4))

        if (scoreB_text_white > 50):
            scoreB_text_white -= 6
            scoreB_text_color = (scoreB_text_white, scoreB_text_white, scoreB_text_white)
        text = font.render(str(scoreB), 0, scoreB_text_color)
        screen.blit(text, (window_size[1] / 1.5, window_size[1] / 4))
        
        font = pygame.font.Font(None, 50)

        # def fadeVarDown(fade, to):
            

        if (last_multiplier != ball.speed_multiplier):
            # score_multiplier_green -= 1
            # fadeVarDown(score_multiplier_green, 70)
            score_multiplier_green = 255
            last_multiplier = ball.speed_multiplier
        # else:
            # score_multiplier_text_color = (70,70,70)
        if (score_multiplier_green > 100):
            score_multiplier_green -= 8
            score_multiplier_text_color = (100,score_multiplier_green,100)

        text = font.render("Speed Multiplier: " + str(round(ball.speed_multiplier, 1)), 1, score_multiplier_text_color)
        screen.blit(text, (window_size[0] / 4, window_size[1] / 2))

        # Show Controls
        font = pygame.font.Font(None, 25)
        text = font.render("To Boost...", 1, (70,70,70))
        screen.blit(text, (window_size[0] / 4, window_size[1] / 2 + 50) )

        text = font.render("Player A: Left Shift, Left Ctrl", 1, (70,70,70))
        screen.blit(text, (window_size[0] / 4, window_size[1] / 2 + 80) )

        text = font.render("Player B: Right Shift, Right Ctrl", 1, (70,70,70))
        screen.blit(text, (window_size[0] / 4, window_size[1] / 2 + 110) )

        ball.ball_rotation += 10

        all_sprites_list.draw(screen)
        # pygame.transform.rotate(ball.image, 10)
        # screen.blit(pygame.transform.rotate(ball.image, ball_rotation), (ball.rect.x, ball.rect.y))

        # ball.image = pygame.transform.rotate(ball.image, ball_rotation)
    # else:
    #     bg_surface = pygame.Surface([window_size[0], window_size[1]])
    #     bg_surface.convert_alpha()
    #     bg_surface.set_alpha(100)
    #     # bg_surface.fill(pygame.Color(30, 30, 30))
    #     # pygame.Surface.set_alpha(bg_surface, 100)

    #     # pygame.draw.rect( bg_surface, pygame.Color(0, 0, 0, 100), [0,0,window_size[0], window_size[1]])

    #     screen.blit(bg_surface, (0,0))

    #     screen.blit(pygame.font.Font(None, int(window_size[0] / 4)).render("PAUSED", 1, (255,0,0)), (50, 50))


    # set_color(ball.image, pygame.Color(0, 0, 0))

    pygame.display.flip() # Update screen with changes

    clock.tick(60) # Set FPS
        

pygame.quit()