import pygame
import os

goalkeeper_list = pygame.sprite.Group()

# WHITE = (100,100,100)
# OTHER = (100,100,100)

class Goalkeeper(pygame.sprite.Sprite):


    def __init__(self, x, y):

        super().__init__()

        print("*********** making goalkeeper")
        self.image = pygame.image.load(os.path.join('images', 'goalkeeper.png')).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        goalkeeper_list.add(self)
