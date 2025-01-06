import pygame
from pygame.locals import *

class Apple:
    def __init__(self, X, Y):
        self.appleLocation = [X, Y]
        self.appleImage = pygame.image.load("Images/Apple.png").convert()
