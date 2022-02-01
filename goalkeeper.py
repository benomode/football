import pygame
import os
import random

goalkeeper_list = pygame.sprite.Group()

# WHITE = (100,100,100)
# OTHER = (100,100,100)
LEFT = 1
RIGHT = 2
STAY = 3

class Goalkeeper(pygame.sprite.Sprite):


    def __init__(self, x, y):

        super().__init__()

        print("*********** making goalkeeper")
        self.image = pygame.image.load(os.path.join('images', 'goalkeeper.png')).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y

        goalkeeper_list.add(self)

    def reset(self):
        print("reseting goalie position x to" + str(self.start_x) + " y to " + str(self.start_y))
        self.rect.x = self.start_x
        self.rect.y = self.start_y

    def dive(self):
        print("moving goalkeeper")

        # which direction should we move - LEFT; RIGHT or STAY

        direction = random.randint(1,3)

        if direction == LEFT:
            print("LEFT")
            self.rect.x = self.rect.x + 100
            # self.rect.y = y
        elif direction == RIGHT:
            print("RIGHT")
            self.rect.x = self.rect.x - 100
        else:
            print("STAY PUT")  
