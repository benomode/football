import pygame
import os
import random
import time
from spritesheet import Spritesheet


goalkeeper_list = pygame.sprite.Group()

# WHITE = (100,100,100)
# OTHER = (100,100,100)
BLACK = (0,0,0)


class Goalkeeper(pygame.sprite.Sprite):


    def __init__(self, position):

        super().__init__()

        print("*********** making goalkeeper")
        gk_spritesheet = Spritesheet(os.path.join('images', 'goalkeeper.png'))
            # load the images for the static view of the goalie from the sprite list using the names in the goalkeeper.json file
        self.gk_ready_animate = [pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_1.png'), (330, 330))
                            , pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_8.png'), (330, 330))]
        self.gk_dive_left_animate = [pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_5.png'), (330, 330))
                            , pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_4.png'), (330, 330))]
        self.gk_dive_right_animate = [pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_2.png'), (330, 330))
                            , pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_3.png'), (330, 330))]                            
        self.gk_dive_stay_animate = [pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_8.png'), (330, 330))
                                    ]                            
        self.gk_dive_jump_animate = [pygame.transform.scale(gk_spritesheet.parse_sprite('goalkeeper_animation_6.png'), (330, 330))
                                    ]                            
        self.current_image_array = self.gk_ready_animate

        self.delay = 0
        self.start = 0
        self.rect = pygame.Rect(position, (0, 0))
        self._set_image(0)

        self.start_x = self.rect.x
        self.start_y = self.rect.y

        goalkeeper_list.add(self)
        self._set_cycle_animation(True)
        self.show(self.current_image_array)

    def _set_cycle_animation(self, cycle_animation = True):
        self.cycle_animation = cycle_animation

    def _get_cycle_animation(self):
        return self.cycle_animation

    def reset(self):
        # print("reseting goalie position x to" + str(self.start_x) + " y to " + str(self.start_y))
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self._set_cycle_animation(True)
        self.show(self.gk_ready_animate)


    def _set_image(self, image_num):
        # print("setting image for goalkeeper current image array is " + str(len(self.current_image_array)))
        self.image_num = image_num
        # self.image = self.gk_ready_animate[self.image_num]
        self.image = self.current_image_array[self.image_num]
        self.rect.size = self.image.get_rect().size


    def _set_rect_position(self, animate_move):
            # move the image based on animate_move passed in
        self.rect.x = self.rect.x + self.animate_move[0]
        self.rect.y = self.rect.y + self.animate_move[1]             

    def show(self, current_image_array, animate_move = (0, 0), delay = 0.8):
        # group.add(self)
        self.current_image_array = current_image_array
        # print(">>> show")
        self.image_num = 0
        self.delay = delay
        self.animate_move = animate_move
        self._set_rect_position(animate_move)
   
        self._set_image(0)
        self.start = time.time()


    def update(self):
        if self.alive() and time.time() - self.start > self.delay:
                    # only cycle to next image if there are more in the current array
                    # do not loop back to the first image if the cycle_animation is set to False
                if self.image_num + 1 < len(self.current_image_array) or self._get_cycle_animation():
                    # print("--->>>>>>>>>>>>> goalie image_num = " + str(self.image_num) + " len image is " + str(len(self.current_image_array)))
                        # cycle through the array of images
                    self.image_num = (self.image_num + 1) % len(self.current_image_array)
                    self._set_rect_position(self.animate_move)
                        # print("changed image num to " + str(self.image_num))
                    self._set_image(self.image_num)
                        # reset start time
                    self.start = time.time()


    def dive(self):
        LEFT = 1
        RIGHT = 2
        STAY = 3
        JUMP = 4

        # print("moving goalkeeper")

        # which direction should we move the goalie as we look at him - LEFT; RIGHT or STAY

        direction = random.randint(1,4)

        if direction == LEFT:
            print("LEFT")
            # self.rect.x = self.rect.x - 100
            self._set_cycle_animation(False)
            animate_move = (-100, 0)
            self.show(self.gk_dive_left_animate, animate_move, 1.2)
            # self.rect.y = y
        elif direction == RIGHT:
            print("RIGHT")
            # self.rect.x = self.rect.x + 100
            self._set_cycle_animation(False)
            animate_move = (75, 0)
            self.show(self.gk_dive_right_animate, animate_move, 1.2)
        elif direction == STAY:
            print("STAY PUT")
            self._set_cycle_animation(False)
            animate_move = (0, 0)
            self.show(self.gk_dive_stay_animate, animate_move)            
        elif direction == JUMP:
            print("JUMP")
            self._set_cycle_animation(False)
            animate_move = (0, 0)
            self.show(self.gk_dive_jump_animate, animate_move)            
