from typing import Any
from setting import *
import pygame as pg
import math

class Player(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load("robot-preview.png"),(50,150))
        self.rect = self.image.get_rect()
        self.rect.center = (200,650)
        self.vx = 0
        self.y_vel = 0
        self.stage_number = 0
        self.IsJump = 0
        self.v = VELOCITY
        self.m = MASS

    def jump(self,j):
        self.IsJump = j
    
    def update(self):
        global stage_num
        self.vx = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = -5
        if keys[pg.K_d]:
            self.vx = 5
        # wrap around the sides of the screen
        if self.rect.left < 0:
            if self.stage_number != 1:
                self.rect.right = 1600
                self.stage_number -= 1
            else:
                self.rect.left = 0
        elif self.rect.right > 1600:
            if self.stage_number != 7:
                self.rect.left = 0
                self.stage_number += 1
            else:
                self.rect.right = 1600
        #gravity
        self.rect.bottom += self.y_vel
        self.y_vel += 1
        #jump
        if self.IsJump > 0:
            if self.v > 0:
                F = (0.5 * self.m * (self.v *self.v))
            else:
                F = -(0.5 * self.m * (self.v *self.v))
            self.rect.y -= round(F)
            self.v -= 1

        self.rect.x += self.vx
        self.rect.y += self.v

class ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load("ball.png"),(100,100))
        self.rect = self.image.get_rect()
        self.ball_speed = 1 * math.pi / 200
        self.angle = 0
        self.ball_distance_d = 0
        self.ball_hero_distance = 300
        self.ball_direction_of_rotation_right = True
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
           self.ball_distance_d = -1
        elif keys[pg.K_RIGHT]:
            self.ball_distance_d = 1
        else:
            self.ball_distance_d = 0
        self.ball_hero_distance += self.ball_distance_d

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,weight,height,what_is_wall):
        pg.sprite.Sprite.__init__(self)
        if what_is_wall == 0:
            self.image = pg.transform.scale(pg.image.load("wall.jpg"),(weight,height))
        elif what_is_wall == 1:
            self.image = pg.transform.scale(pg.image.load("wall.jpg"),(weight,height))
        elif what_is_wall == 2:
            self.image = pg.transform.scale(pg.image.load("wall.jpg"),(weight,height))
        #self.image = pg.Surface((weight,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, buttonText='Button', onePress = True):#버튼
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onclickFunction = self.Next_Window
        self.onePress = onePress
        self.fuc = False
        self.buttonRect = pg.Rect(self.rect.x, self.rect.y, width, height)

        self.buttonSurf = font1.render(buttonText, True, (255, 255, 255))

        self.alreadyPressed = False

    def process(self):#버튼 생성

        mousePos = pg.mouse.get_pos()
        
        self.image.fill(black)
        if self.buttonRect.collidepoint(mousePos):
            self.image.fill(gray)

            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.image.fill(gray1)

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.image.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
    def Next_Window(self):
        self.fuc = True
