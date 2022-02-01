import pygame
from target import target_list
from goalkeeper import goalkeeper_list
from goal import goal_list
from player import player_list
import random
from math import tan, atan, radians, degrees

WHITE = (255,255,255)
removeBallAfterMs = 1550   # number of milliseconds to wait until we remove the football


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.time = None

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)


        self.image = pygame.image.load("ball2.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.state="static"
        self.angle=0
        self.target = None
        self.shadow = None



    def update(self):

        if self.time is None:
                # did it hit a goal keeper sprite?
            saved_list = pygame.sprite.spritecollide(self, goalkeeper_list, False,pygame.sprite.collide_mask)
                # did it hit a goal sprite
            goalscored_list = pygame.sprite.spritecollide(self, goal_list, False)
            if saved_list and self.shadow.rect.y<335:
                print("SAVE !!!!!!!")
                self.stop()

            elif goalscored_list and self.shadow.rect.y<325:
                print("GOAL - hitting goal sprite")
                # give the player with the ball a goal
                self.player.scored()
                self.stop()

                hit_list = pygame.sprite.spritecollide(self, target_list, False)
                for target in hit_list:
                    print("GOAL - hitting the target")
                    #self.player.score += goal.score
                    #stats(self.player.score)
                    self.state = "stop"
                    self.time = pygame.time.get_ticks() # start a timer to remove the ball from the screen

        else:
                    # and x ms have elapsed, remove the football.
            if pygame.time.get_ticks() - self.time >= removeBallAfterMs:
                self.time = None
                self.reset()

    def curveRight(self, pixels):

        self.vx += pixels/100
        self.shadow.curveRight(pixels)

    def curveLeft(self, pixels):
        self.vx -= pixels/100
        self.shadow.curveLeft(pixels)

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def playerwithBall(self, player):
        self.player = player

    def stop(self):
        self.state = "stop"
        self.time = pygame.time.get_ticks() # start a timer to remove the ball from the screen

    def reset(self):
        self.rect.x = 480
        self.rect.y = 800
        self.rect.x = random.randint(200,800)
        self.target.kill()  # get rid of the target object
        self.shadow.rect.x = self.rect.x
        self.shadow.rect.y = self.rect.y
        self.shadow.ball = self
        self.state = "static"


    def shoot(self, pos):
        self.state = "moving"
        self.vx = (pos[0]-self.rect.x) / 100
        self.vy = (pos[1]-self.rect.y) / 100
        self.angle =  30 * (350-pos[1])/250
        #print(self.angle)
        self.shadow.shoot(pos)

    def move(self):
        self.rect.y += self.vy
        self.rect.y -= 5 * tan(radians(self.angle))
        self.rect.x += self.vx
        self.shadow.move()
        if self.rect.y < 0 or self.rect.x < 200 or self.rect.x > 750:
            self.state="reset"
