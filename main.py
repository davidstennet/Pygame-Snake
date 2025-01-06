import pygame
import random
from pygame.locals import *
from snake import Snake
from apple import Apple


# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up the game window
gameScreen = pygame.display.set_mode((400, 440))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

# Creates snake and apple object
snake = Snake()
X = random.randrange(0, 400, 20)
Y = random.randrange(40, 440, 20)
apple = Apple(X, Y)

# Creates a font and text for the score
font = pygame.font.SysFont("Comic Sans MS", 34)
scoreText = font.render("Score: " + str(snake.score), False, (255, 255, 255))

# Custom event for moving the snake
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 150)

# Main game loop
running = True
notStarted = True
defeated = False
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                snake.changeDirection("UP")
            elif event.key == K_DOWN:
                snake.changeDirection("DOWN")
            elif event.key == K_LEFT:
                snake.changeDirection("LEFT")
            elif event.key == K_RIGHT:
                snake.changeDirection("RIGHT")
        elif event.type == MOVE_EVENT:
            snake.move()     

    # Checks for a collision and exits the game if there is one
    if snake.checkCollision():
        running = False

    # Checks if the snake head collides with an apple
    if snake.checkAppleCollision(apple.appleLocation):
        snake.grow()
        X = random.randrange(0, 400, 20)
        Y = random.randrange(40, 440, 20)
        while [X, Y] in snake.snakeBody:
            X = random.randrange(0, 400, 20)
            Y = random.randrange(40, 440, 20)
        apple.appleLocation = [X, Y]

    # Fill the screen with a color (RGB)
    gameScreen.fill((0, 0, 0))

    # Fills the screen with the snake, score, and apple locations
    for segment in snake.snakeBody :
        gameScreen.blit(snake.bodyImage, (segment[0], segment[1]))
    gameScreen.blit(apple.appleImage, apple.appleLocation)
    scoreText = font.render("Score: " + str(snake.score), False, (255, 255, 255))
    gameScreen.blit(scoreText, (0, 0))

    # Update the display
    pygame.display.flip()

    fps.tick(60)

        


# Quit Pygame
pygame.quit()