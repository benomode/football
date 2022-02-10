import pygame
import os

target_list = pygame.sprite.Group()

EXTRA_GOAL = 2
EXTRA_BALL = 1

class target(pygame.sprite.Sprite):

    def __init__(self, x, y, value, targettype):

        super().__init__()
        print("*********** making target")
        self.image = pygame.image.load(os.path.join('images', 'target.png')).convert_alpha()
#        self.image = pygame.image.load('target.png').convert_alpha()        
        self.x = x
        self.y = y
        self.value = value
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.targetType = targettype

        target_list.add(self)
