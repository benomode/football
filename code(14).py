#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:
#
# Created:     23/04/2021
# Copyright:   (c) 15hunt 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame, sys
import math
import random
from target import target
from target import target_list
mainClock = pygame.time.Clock()
from pygame.locals import *
from ball import Ball
from shadow import Shadow


pygame.init()

#SETS THE WIDTH AND HEIGHT OF THE WINDOW
SCREENWIDTH=1000
SCREENHEIGHT=900
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
#NAMING MY WINDOW WHEN THE GAME LOADS UP
pygame.display.set_caption("Freekick Frenzy")
arrow=pygame.image.load("arrow.png")
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

score = 0
font = pygame.font.SysFont(None, 20)
WHITE = (255, 255, 255)
OTHER = (100,100,100)
BLACK = (0,0,0)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():

    bg = pygame.image.load("images/backgroundmain.jpg")
    click=False
    while True:





        screen.blit(bg, (0 , 0))
        font = pygame.font.SysFont(None, 60)
        draw_text('F', font, (255, 204, 102), screen, 330, 250)
        draw_text('r', font, (255, 255, 153), screen, 355, 250)
        draw_text('e', font, (255, 204, 102), screen, 372, 250)
        draw_text('e', font, (255, 255, 153), screen, 395, 250)
        draw_text('k', font, (255, 204, 102), screen, 420, 250)
        draw_text('i', font, (255, 255, 153), screen, 443, 250)
        draw_text('c', font, (255, 204, 102), screen, 455, 250)
        draw_text('k', font, (255, 255, 153), screen, 478, 250)
        draw_text('F', font, (255, 204, 102), screen, 520, 250)
        draw_text('r', font, (255, 255, 153), screen, 545, 250)
        draw_text('e', font, (255, 204, 102), screen, 562, 250)
        draw_text('n', font, (255, 255, 153), screen, 585, 250)
        draw_text('z', font, (255, 204, 102), screen, 610, 250)
        draw_text('y', font, (255, 255, 153), screen, 630, 250)




        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250, 350, 200, 50)
        button_2 = pygame.Rect(550, 350, 200, 50)



        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                help()
        pygame.draw.rect(screen, (0,0,0), button_1)
        font = pygame.font.SysFont(None, 80)
        draw_text("START", font, (102, 255, 153), screen, 260, 350)
        pygame.draw.rect(screen, (0,0,0), button_2)
        draw_text('HELP', font, (255, 102, 102), screen, 590, 350)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():

    bg = pygame.image.load("images/backgroundgame.png")

    score = 0

    from post import post

    post1 = post(WHITE, 10, 250)
    post1.rect.x = 200
    post1.rect.y = 100

    post2 = post(WHITE, 10, 250)
    post2.rect.x = 800
    post2.rect.y = 100

    post3 = post(WHITE, 600, 10)
    post3.rect.x = 200
    post3.rect.y = 100

    # from bar import bar

    # bar = bar(BLACK, 1200, 80)
    # bar.rect.x = 0
    # bar.rect.y = 0


    ball = Ball(WHITE, 35, 35)
    ball.rect.x = 480
    ball.rect.y = 800
    ball.rect.x = random.randint(200,800)
    shadow = Shadow(WHITE, 35, 35)
    shadow.rect.x = ball.rect.x
    shadow.rect.y = ball.rect.y


    ball.shadow = shadow
    shadow.ball = ball

    from goal import goal

    goal = goal(OTHER, 600, 250)
    goal.rect.x = 200
    goal.rect.y = 100



    all_sprites_list = pygame.sprite.Group()


    all_sprites_list.add(post1)
    all_sprites_list.add(post2)
    all_sprites_list.add(post3)
    all_sprites_list.add(shadow)
    all_sprites_list.add(ball)
    all_sprites_list.add(goal)
    # all_sprites_list.add(bar)
    # all_sprites_list.add(target)

    click=False
    running = True
    scored=False
    while running:
        screen.blit(bg, (0 , 0))

        font = pygame.font.SysFont(None, 60)
        draw_text('F', font, (255, 204, 102), screen, 330, 30)
        draw_text('r', font, (255, 255, 153), screen, 355, 30)
        draw_text('e', font, (255, 204, 102), screen, 372, 30)
        draw_text('e', font, (255, 255, 153), screen, 395, 30)
        draw_text('k', font, (255, 204, 102), screen, 420, 30)
        draw_text('i', font, (255, 255, 153), screen, 443, 30)
        draw_text('c', font, (255, 204, 102), screen, 455, 30)
        draw_text('k', font, (255, 255, 153), screen, 478, 30)
        draw_text('F', font, (255, 204, 102), screen, 520, 30)
        draw_text('r', font, (255, 255, 153), screen, 545, 30)
        draw_text('e', font, (255, 204, 102), screen, 562, 30)
        draw_text('n', font, (255, 255, 153), screen, 585, 30)
        draw_text('z', font, (255, 204, 102), screen, 610, 30)
        draw_text('y', font, (255, 255, 153), screen, 630, 30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        #GAME CODE HERE

        if shadow.rect.y<325 and ball.rect.y>100 and ball.rect.y<350 and ball.rect.x>200 and ball.rect.x<800 and scored==False:
            score+=1
            scored=True
            ball.state="reset"


        font = pygame.font.SysFont(None, 20)
        draw_text("Score - " + str(score),font,(255,255,255), screen, 50, 50)



        pos = pygame.mouse.get_pos()
        rotx = ball.rect.centerx
        roty = ball.rect.centery

        if ball.state=="static":
            if ball.target:
                ball.target.kill()  # make sure if we miss that the target is removed
            angle = 270-math.atan2(pos[1]-roty,pos[0]-rotx)*180/math.pi
            rotimage = pygame.transform.rotate(arrow,angle)
            rect = rotimage.get_rect(center=(rotx,roty-100))
            screen.blit(rotimage,rect)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ball.curveRight(4)

        if keys[pygame.K_LEFT]:
            ball.curveLeft(4)





        mx, my = pygame.mouse.get_pos()

        if goal.rect.collidepoint((mx, my)):
            if click and ball.state=="static":
                mytarget = target(mx-25,my-25)
                target_list.add(mytarget)
                ball.target = mytarget
                ball.shoot((mx+25,my+25))


                scored=False
                click=False

        if ball.state=="moving":
            ball.move()


        if ball.state=="reset":
            click=True
            ball.rect.x = random.randint(200,800)
            ball.rect.y = 800
            shadow.rect.x = ball.rect.x
            shadow.rect.y = ball.rect.y
            ball.state="static"
            click=False


        target_list.draw(screen) # draw target
        # for t in target_list:
        #     t.update()
        ball.update()


        all_sprites_list.draw(screen)

        pygame.display.update()
        mainClock.tick(60)


def help():
    running = True
    while running:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        font = pygame.font.SysFont(None, 50)
        draw_text('How to Play!', font, (255, 204, 102), screen, 20, 20)
        font = pygame.font.SysFont(None, 30)
        draw_text('1. First you use your mouse to aim the cursor where you would like to shoot.', font, (255, 255, 255), screen, 20, 80)
        draw_text('2. Once you have positioned your mouse cursor where you would like to shoot', font, (255, 255, 255), screen, 20, 140)
        draw_text('    simply left click with the mouse and the ball will fly into the corner or area of your', font, (255, 255, 255), screen, 20, 160)
        draw_text('    choice within the goal (If you have aimed correctly).', font, (255, 255, 255), screen, 20, 180)
        draw_text('3. If you do manage to beat the opposition in the way and score then you score, font', font, (255, 255, 255), screen, 20, 240)
        draw_text('    a point and dependant on where the ball lands within the goal the points may vary.', font, (255, 255, 255), screen, 20, 260)
        draw_text('4. Repeat this until you have shot all 5 of your balls', font, (255, 255, 255), screen, 20, 320)
        draw_text('    shown on screen) attempting to earn as high of a score as possible.', font, (255, 255, 255), screen, 20, 340)
        draw_text('5. Once the ball count does hit 0 the game will be over and you will be shown', font, (255, 255, 255), screen, 20, 400)
        draw_text('    your final score along with a game over message, this is then followed by the option to', font, (255, 255, 255), screen, 20, 420)
        draw_text('    the game again or exit if you have finished.', font, (255, 255, 255), screen, 20, 440)
        draw_text('6. Now you are ready to play!', font, (255, 255, 255), screen, 20, 500)


        pygame.display.update()
        mainClock.tick(60)


main_menu()