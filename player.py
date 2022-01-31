import pygame
import os

player_list = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):


    def __init__(self):

        super().__init__()

        print("*********** making player")
        self.score = 0

        player_list.add(self)

    def scored(self):
        print("PLAYER SCORED")
        self.score += 1
        print("PLAYER score is now" + str(self.score))