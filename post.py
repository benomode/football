import pygame
WHITE = (255,255,255)

class post(pygame.sprite.Sprite):


    def __init__(self, color, width, height):

        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)



        pygame.draw.rect(self.image, color, [0, 0, width, height])


        self.rect = self.image.get_rect()

