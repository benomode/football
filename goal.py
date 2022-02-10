import pygame
from target import target
from target import EXTRA_GOAL
from target import EXTRA_BALL

WHITE = (100,100,100)
OTHER = (100,100,100)

goal_list = pygame.sprite.Group()

class Goal(pygame.sprite.Sprite):


    def __init__(self, color, width, height):

        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(OTHER)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        goal_list.add(self)

    def createBonusTarget(self):
        print("hello")
        print("$ creating bonus targets {}".format(EXTRA_GOAL))
        print("create between {} and {}".format(self.rect.x, self.rect.y))

        mytarget = target(250, 150, 2, EXTRA_GOAL)
        mytarget = target(450, 200, 2, EXTRA_BALL)
        # mytarget = target(mx-25, my-25, EXTRA_GOAL)
