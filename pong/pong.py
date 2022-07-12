# https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

import pygame
pygame.init()
from paddle import Paddle
from ball import Ball
from bullet import Bullet

bg = (0,0,0)
fg = (255,255,255)

paddle_speed = 5

scoreA = 0
scoreB = 0

# Open a new window
window_size = (700,500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("POOOOOOOOOOOOOOOOOOOOONG")

# Create the objects 

paddleA = Paddle(fg, 10, 100)
paddleA.rect.x = 20 # Setting Position
paddleA.rect.y = 200

paddleB = Paddle(fg, 10, 100)
paddleB.rect.x = 670 # Setting Position
paddleB.rect.y = 200

ball = Ball(fg, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

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
        

# MAIN LOOP
bulletAShot = False
bulletBShot = False
while carryOn:
    for event in pygame.event.get(): # User did a something
        if event.type == pygame.QUIT: # User exited the game
            carryOn = False
    
    # Inputs
    keys = pygame.key.get_pressed()
    # player A
    if keys[pygame.K_w]:
        paddleA.moveUp(paddle_speed)
    if keys[pygame.K_s]:
        paddleA.moveDown(paddle_speed)

    if keys[pygame.K_d] and not bulletAShot:
        bulletA.rect.x = 20
        bulletA.rect.y = paddleA.rect.x

    # player B
    if keys[pygame.K_UP]:
        paddleB.moveUp(paddle_speed)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(paddle_speed)

    if keys[pygame.K_LEFT] and not bulletBShot:
        bulletB.rect.x = 200
        bulletB.rect.y = paddleB.rect.x


    # Game Logic
    all_sprites_list.update() # Refresh list

    # Check if the ball bounces against the walls
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
    
    # Detect collisions between ball & paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    # Visuals
    screen.fill(bg)
    # Display Scores
    font = pygame.font.Font(None, 900)
    text = font.render(str(scoreA), 0, (20,20,20))
    screen.blit(text, (-50,10))
    text = font.render(str(scoreB), 0, (20,20,20))
    screen.blit(text, (420,10))
    
    all_sprites_list.draw(screen)


    pygame.display.flip() # Update screen with changes

    clock.tick(60) # Set FPS


pygame.quit()