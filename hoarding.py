import pygame
import time

white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)

hoarding_list = []

class Hoarding():


    def __init__(self, surface, text, hpos, color, size=40):

        super().__init__()

        print("*********** making hoarding")

        self.surface = surface
        self.text = text
        self.hpos = hpos
        self.color = color
        self.size = size
        # initialize
        self.position = 0
        self.font = pygame.font.SysFont("mono", self.size, bold=True)
        self.text_surface = self.font.render(self.text, True, self.color)        
        self.font = pygame.font.SysFont('timesnewroman', 30)

        hoarding_list.append(self)
        

    def set_text(self, text, delay = 2.0):
        self.text = text
        self.text_surface = self.font.render(self.text, True, "black")
        # self.text_surface.fill("yellow")
            # start the timer if this is the first text appended
        self.delay = delay
        self.position = 0

    def update(self, hpos=None):
        """update every frame"""
        if len(self.text) > 0:
            if hpos is not None:
                self.hpos = hpos
            self.surface.blit(self.text_surface, 
                (105, self.hpos), 
                (self.position, 0, self.surface.get_width(), self.size)
            )
            # print("self.position is {}".format(self.position))
            if self.position > -500: # self.text_surface.get_width():
                self.position -= 1
            else:
                print("should stop")
                self.text_surface.fill("yellow")
                self.text = ""

    def update2(self):

        if len(self.hoardingtext) == 0 and len(self.text) > 0:
            self.hoardingtext = self.text.pop(0)
            self.start = time.time()
            self.i = 100

        if self.i < 720 and len(self.hoardingtext) > 0 and time.time() - self.start > self.delay:
            self.start = time.time()
            print("hoarding text len > 0")
            print("hoarding i is {}".format(self.i))
           
            print("hoarding text is {}".format(self.hoardingtext) )
            offset = 0  # -124
            for l in self.hoardingtext:
                # print("letter is {}".format(l) )
                letter = self.font.render(l, False, orange, yellow)

                self.win.blit(letter, (offset + self.i, 470))
                offset += 22

            self.i += 80
        
            if self.i >= 720:
                self.hoardingtext = ""
        
            # letter1=self.font.render("H", False, orange, yellow)
            # letter2=self.font.render("E", False, orange, green)
            # letter3=self.font.render("M", False, orange, yellow)
            # letter4=self.font.render("A", False, orange, green)
            # letter5=self.font.render("N", False, orange, yellow)
            # letter6=self.font.render("T", False, orange, green)
            # letter7=self.font.render("H", False, orange, yellow)

            # Scrolling the text in bottom of the Screen.
            # self.win.blit(letter1, (-124 + self.i, 470))
            # self.win.blit(letter2, (-102 + self.i, 470))
            # self.win.blit(letter3, (-82 + self.i, 470))
            # self.win.blit(letter4, (-58 + self.i, 470))
            # self.win.blit(letter5, (-40 + self.i, 470))
            # self.win.blit(letter6, (-19 + self.i, 470))
            # self.win.blit(letter7, (0 + self.i, 470))
		
            # Decides the speed
            # of the text on screen

	