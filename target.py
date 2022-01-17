import pygame
import os

target_list = pygame.sprite.Group()

class target(pygame.sprite.Sprite):


    def __init__(self, x, y):

        super().__init__()
        print("*********** making target")
        self.image = pygame.image.load(os.path.join('images', 'target.png')).convert_alpha()
#        self.image = pygame.image.load('target.png').convert_alpha()        
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
