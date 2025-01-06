import pygame
from pygame.locals import *

class Snake:
    def __init__(self):
        self.snakeHeadPosition = [100, 100]
        self.snakeBody = [
            [100, 100],
            [100, 80],
            [100, 60],
            [100, 40],
        ]
        self.bodyImage = pygame.image.load("Images/Snake_Segment.png").convert()
        self.snakeDirection = "DOWN"
        self.score = 0

    # Moves the snake depending on the direction
    def move(self):
        # Updates snake head depending on snakeDirection
        if self.snakeDirection == "UP":
            self.snakeHeadPosition[1] -= 20
        elif self.snakeDirection == "DOWN":
            self.snakeHeadPosition[1] += 20
        elif self.snakeDirection == "LEFT":
            self.snakeHeadPosition[0] -= 20
        elif self.snakeDirection == "RIGHT":
            self.snakeHeadPosition[0] += 20

        # Update the snake body
        self.snakeBody.insert(0, list(self.snakeHeadPosition))
        self.snakeBody.pop()

    # Method that updates the direction of the snake
    def changeDirection(self, newDirection):
        # Changes snakeDirection if newDirection is legal
        if newDirection == "UP" and self.snakeDirection != "DOWN":
            self.snakeDirection = "UP"
        elif newDirection == "DOWN" and self.snakeDirection != "UP":
            self.snakeDirection = "DOWN"
        elif newDirection == "LEFT" and self.snakeDirection != "RIGHT":
            self.snakeDirection = "LEFT"
        elif newDirection == "RIGHT" and self.snakeDirection != "LEFT":
            self.snakeDirection = "RIGHT"

    # Checks for a collision 
    def checkCollision(self):
        for segment in self.snakeBody[1:]:
            if self.snakeHeadPosition == segment:
                return True
        if self.snakeHeadPosition[0] < 0 or self.snakeHeadPosition[0] > 400:
            return True
        if self.snakeHeadPosition[1] < 0 or self.snakeHeadPosition[1] > 400:
            return True
        return False

    # Checks for a collision with an apple
    def checkAppleCollision(self, appleCoordinates):
        if (appleCoordinates == self.snakeHeadPosition):
            self.score += 1
            return True
        return False
    
    # Grows the end of the snake
    def grow(self):
        self.snakeBody.append(self.snakeBody[-1])
        
        
