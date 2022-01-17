import pygame
from target import target_list

WHITE = (255,255,255)
removeBallAfterMs = 1550   # number of milliseconds to wait until we remove the football


class ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.time = None

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)


        self.image = pygame.image.load("ball2.png").convert_alpha()
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.state="static"


    def update(self):
        hit_list = pygame.sprite.spritecollide(self, target_list, False)
        # for target in hit_list:
        #     print("XXX GOAL !!!!!!!")
        if self.time is None: 
            hit_list = pygame.sprite.spritecollide(self, target_list, False)
            for target in hit_list:
                print("IT's A GOAL !!!!!!!")
                # self.player.score += goal.score
                # stats(self.player.score)
                self.state = "static"
                self.time = pygame.time.get_ticks() # start a timer to remove the ball from the screen

        else:
                    # and x ms have elapsed, remove the football.
            if pygame.time.get_ticks() - self.time >= removeBallAfterMs:
                self.kill()

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




