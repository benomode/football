import pygame
WHITE = (100,100,100)
OTHER = (100,100,100)

class goal(pygame.sprite.Sprite):


    def __init__(self, color, width, height):

        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(OTHER)



        pygame.draw.rect(self.image, color, [0, 0, width, height])


        self.rect = self.image.get_rect()