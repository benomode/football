import pygame
import os

player_list = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):


    def __init__(self):

        super().__init__()

        print("*********** making player")
        self.score = 0
        self.balls = 5

        player_list.add(self)

    def scored(self):
        print("PLAYER SCORED")
        self.score += 1
        print("PLAYER score is now" + str(self.score))

    def bonusscore(self, amount):
        print("PLAYER SCORED")
        self.score += amount
        print("PLAYER score is now" + str(self.score))     

    def bonusball(self, amount):
        print("PLAYER GOT BONUE BALL")
        self.balls += amount
        print("PLAYER now has {} balls".format(self.balls))       