import pygame
from target import target_list
import random

WHITE = (255,255,255)
removeBallAfterMs = 1550   # number of milliseconds to wait until we remove the football


class Shadow(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.time = None

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)


        self.image = pygame.image.load("shadow.png").convert_alpha()
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.state="static"

        self.ball = None




    def curveRight(self, pixels):
        self.vx += pixels/100


    def curveLeft(self, pixels):
        self.vx -= pixels/100


    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0



    def shoot(self, pos):
        self.state = "moving"
        self.vx = (pos[0]-self.rect.x) / 100
        self.vy = (pos[1]-self.rect.y) / 100


    def move(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.y < 100 or self.rect.x < 200 or self.rect.x > 750:
            self.state="reset"
