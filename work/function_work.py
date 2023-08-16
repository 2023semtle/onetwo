import pygame
import time
import sys
import math
from pygame.locals import *
import ctypes

pygame.init()#초기화
#화면 크기
width, height = 1600, 900

#색상
blue = (22, 34, 126)

#속도와 질량 기본 값
VELOCITY = 7
MASS = 2

y_vel = 0
is_ball_wall = False
isCome_outHero = False
stage_num = 0

class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):#버튼
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.fillColors = {
            'normal': '#000000',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font1.render(buttonText, True, (255, 255, 255))

        self.alreadyPressed = False

    def process(self):#버튼 생성

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
    def draw_button(self):
        screen.blit(self.buttonSurface,(self.x,self.y))

class Button1:
    def __init__(self,img_in,x,y,button_width,button_height,img_act,x_act,y_act,action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed
        if x + button_width > mouse[0] > x and y + button_height > mouse[1] > y:
            screen.blit(img_act,(x_act,y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in,(x,y))
            print(1)

class wall:
    def __init__(self):
        self.rect = ""
        self.image = ""
    def load_wall(self,scale_x,scale_y,location_x,location_y,what_is_wall):
        if what_is_wall == 0:
            self.image = pygame.image.load("wall.jpg")
        elif what_is_wall == 1:
            self.image = pygame.image.load("wall.jpg")
        elif what_is_wall == 2:
            self.image = pygame.image.load("wall.jpg")
        self.image = pygame.transform.scale(self.image,(scale_x,scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = location_x
        self.rect.y = location_y
    def draw_wall(self):
        screen.blit(self.image,[self.rect.x,self.rect.y])

class hero(pygame.sprite.Sprite):
    def __init__(self):
        self.image =""
        self.dx = 0
        self.dy = 0
        self.rect = ""
        self.isJump = 0
        self.v = VELOCITY
        self.m = MASS

    def load_car(self,location_x,location_y,scale_x,scale_y):
        # 플레이어 차량
        self.image = pygame.image.load("robot-preview.png")
        # 크기 조정
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.centerx = location_x
        self.rect.bottom = location_y
        self.hero_size = self.image.get_rect().size
        self.hero_width = self.hero_size[0]
        self.hero_height = self.hero_size[1]
    # 자동차를 스크린에 그리기
    def draw_car(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])
    # x 좌표 이동 - 플레이어 자동차의 움직임 제어할 때 필요
    def move_x(self):
        self.rect.x += self.dx
     # 화면 밖으로 못 나가게 방지
    def check_screen(self):
        global stage_num
        if self.rect.left < 0:
            if stage_num != 1:
                self.rect.right = 1600
                stage_num -= 1
            else:
                self.rect.left = 0
        elif self.rect.right > 1600:
            if stage_num != 7:
                self.rect.left = 0
                stage_num += 1
            else:
                self.rect.right = 1600

    def gravity(self):
        global y_vel
        self.rect.bottom += y_vel 
        y_vel += 1
        if self.rect.bottom >= 800:
            y_vel = 0
    def jump(self, j):
        self.isJump = j

    def update(self):
        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:
            # isJump 값이 2일 경우 속도를 리셋
            # 점프 한 상태에서 다시 점프를 위한 값
            # 이 코드를 주석처리하면 이중점프를 못한다.
            if self.isJump == 2:
                self.v = VELOCITY

            # 역학공식 계산 (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (0.5 * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(0.5 * self.m * (self.v * self.v))

            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.rect.y -= round(F)

            # 속도 줄여줌
            self.v -= 1

            # 바닥에 닿았을때, 변수 리셋
            if self.rect.bottom > 800:
                self.rect.bottom = 800
                self.isJump = 0
                self.v = VELOCITY
class ball:
    def __init__(self):
        self.image = ""
        self.angle = 0
        self.rect = ""
        self.ball_speed = 1 * math.pi / 200
        self.ball_hero_distance = 300
        self.ball_direction_of_rotation_right = True
        self.ball_size = ""
        self.ball_width = ""
        self.ball_height = ""
        self.ball_distance_d = 0

    def load_ball(self):
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect() 
        self.ball_size = self.image.get_rect().size
        self.ball_width = self.ball_size[0]
        self.ball_height = self.ball_size[1]

    def draw_ball(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def move_distance(self):
        self.ball_hero_distance += self.ball_distance_d

def Next_Window(): #다음 화면
    global isCome_outHero,stage_num
    isCome_outHero = True
    stage_num = 1

def main():
    global screen,height,width,y_vel,is_ball_wall,font1,Start_Button,isCome_outHero
    pygame.init()#초기화

    #user32 = ctypes.windll.user32 전체화면
    #screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)  # 해상도 구하기

    # pygame 초기화 및 스크린 생성
    pygame.display.set_caption("work")
    screen = pygame.display.set_mode((width,height))#screensize, FULLSCREEN 전체화면 
    font1 = pygame.font.Font('Maplestory_Bold.ttf',20)
    clock = pygame.time.Clock()

    # 플레이어 자동차 생성
    player = hero()
    player.load_car(700,700,50,150)

    stuff = ball()
    stuff.load_ball()

    base_top_wall = wall()
    base_top_wall.load_wall(1600,100,0,0,1)

    base_bottom_wall = wall()
    base_bottom_wall.load_wall(1600,100,0,800,1)

    #1 스테이지
    fisrt_first_wall = wall()
    first_second_wall = wall()
    first_third_wall = wall()
    fisrt_first_wall.load_wall(80,900,600,600,1)
    first_second_wall.load_wall(80,900,900,500,1)
    first_third_wall.load_wall(80,900,1200,500,1)

    #2
    second_first_wall = wall()
    second_first_wall.load_wall(300,900,800,350,1)

    #3
    third_ball_dead_wall = wall()
    third_human_dead_wall = wall()
    third_ball_dead_wall.load_wall(10,1000,600,0,1)
    third_human_dead_wall.load_wall(10,1000,1100,0,1)

    #4
    fourty_first_ball_dead_wall = wall()
    fourty_first_human_dead_wall = wall()
    fourty_second_ball_dead_wall = wall()
    fourty_second_human_dead_wall = wall()
    fourty_first_wall = wall()
    fourty_first_ball_dead_wall.load_wall(10,450,850,0,1)
    fourty_second_ball_dead_wall.load_wall(10,450,1300,450,1)
    fourty_first_human_dead_wall.load_wall(10,450,850,450,1)
    fourty_second_human_dead_wall.load_wall(10,450,1300,0,1)
    fourty_first_wall.load_wall(1300,20,700,450,1)
    
    #5
    fifty_first_wall = wall()
    fifty_first_ball_dead_wall = wall()
    fifty_second_ball_dead_wall = wall()
    fifty_first_wall.load_wall(100,30,700,550,1)
    fifty_first_ball_dead_wall.load_wall(10,550,760,0,1)
    fifty_second_ball_dead_wall.load_wall(2000,10,750,550,1)

    #6
    sixty_first_wall = wall()
    sixty_first_human_dead_wall = wall()
    sixty_second_human_dead_wall = wall()
    sixty_third_human_dead_wall = wall()
    sixty_ball_dead_wall = wall()
    sixty_first_wall.load_wall(100,30,400,500,1)
    sixty_ball_dead_wall.load_wall(10,900,800,0,1)
    sixty_first_human_dead_wall.load_wall(10,500,460,500,1)
    sixty_second_human_dead_wall.load_wall(10,900,1100,0,1)
    sixty_third_human_dead_wall.load_wall(10,900,1400,0,1)

    #7
    seventy_first_wall = wall()
    seventy_second_wall = wall()
    seventy_third_wall = wall()
    seventy_ball_dead_wall = wall()
    seventy_first_human_dead_wall = wall()
    seventy_second_human_dead_wall = wall()
    seventy_third_human_dead_wall = wall()
    seventy_fourty_human_dead_wall = wall()
    seventy_first_wall.load_wall(400,200,0,800,1)
    seventy_second_wall.load_wall(400,200,1200,800,1)
    seventy_third_wall.load_wall(800,50,400,600,1)
    seventy_first_human_dead_wall.load_wall(10,600,450,0,1)
    seventy_second_human_dead_wall.load_wall(10,600,650,0,1)
    seventy_third_human_dead_wall.load_wall(10,600,850,0,1)
    seventy_fourty_human_dead_wall.load_wall(10,600,1050,0,1)
    seventy_ball_dead_wall.load_wall(10,800,1300,0,1)

    Start_Button = Button(520, 300, 500, 200, 'Start', Next_Window)#버튼 생성

    playing = True
    while playing:
        screen.fill(blue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if isCome_outHero == True:
                # 화살표 키를 이용해서 플레이어의 움직임 거리를 조정해준다.
                # 키를 떼면 움직임 거리를 0으로 한다.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                       player.dx = 5
                    elif event.key == pygame.K_a:
                       player.dx = -5
                    elif event.key == pygame.K_LEFT:
                       stuff.ball_distance_d = -1
                    elif event.key == pygame.K_RIGHT:
                        stuff.ball_distance_d = 1
                    # 스페이스키를 눌렀을 때,
                    # 0이면 바닥인 상태 : 1로 변경
                    # 1이면 점프를 한 상태 : 2로 변경, 점프한 위치에서 다시 점프를 하게 된다. 즉, 이중점프
                    if event.key == pygame.K_w:
                       if player.isJump == 0:
                          player.jump(1)
                    if event.key == pygame.K_SPACE:
                       player.rect.x = stuff.rect.x
                       player.rect.y = stuff.rect.y
                       stuff.angle += math.pi 
                if event.type == pygame.KEYUP:
                   if event.key == pygame.K_d:#점프할때 중력 끄기
                      player.dx = 0
                   elif event.key == pygame.K_a:
                       player.dx = 0
                   elif event.key == pygame.K_LEFT:
                       stuff.ball_distance_d = 0
                   elif event.key == pygame.K_RIGHT:
                       stuff.ball_distance_d = 0

        if isCome_outHero == True:
            if is_ball_wall == False:
               if stuff.ball_direction_of_rotation_right == True:
                  stuff.angle += stuff.ball_speed
                  stuff.rect.x =  player.rect.x + int(math.cos(stuff.angle) * stuff.ball_hero_distance)#볼 이동
                  stuff.rect.y =  player.rect.y + int(math.sin(stuff.angle) * stuff.ball_hero_distance)
               else:
                  stuff.angle -= stuff.ball_speed
                  stuff.rect.x =  player.rect.x + int(math.cos(stuff.angle) * stuff.ball_hero_distance)
                  stuff.rect.y =  player.rect.y + int(math.sin(stuff.angle) * stuff.ball_hero_distance)
            #여기에 stage_num마다 벽 check 처리#함수
            print(stuff.angle)
            if stage_num == 1:
                if player.rect.right < fisrt_first_wall.rect.right and player.rect.left > player.rect.left:
                    player.rect.bottom = fisrt_first_wall.rect.y
                fisrt_first_wall.draw_wall()
                first_second_wall.draw_wall()
                first_third_wall.draw_wall()
            elif stage_num == 2:
                second_first_wall.draw_wall()
            elif stage_num == 3:
                third_ball_dead_wall.draw_wall()
                third_human_dead_wall.draw_wall()
            elif stage_num == 4:
                fourty_first_ball_dead_wall.draw_wall()
                fourty_first_human_dead_wall.draw_wall()
                fourty_first_wall.draw_wall()
                fourty_second_ball_dead_wall.draw_wall()
                fourty_second_human_dead_wall.draw_wall()
            elif stage_num == 5:
                fifty_first_ball_dead_wall.draw_wall()
                fifty_first_wall.draw_wall()
                fifty_second_ball_dead_wall.draw_wall()
            elif stage_num == 6:
                sixty_ball_dead_wall.draw_wall()
                sixty_first_human_dead_wall.draw_wall()
                sixty_first_wall.draw_wall()
                sixty_second_human_dead_wall.draw_wall()
                sixty_third_human_dead_wall.draw_wall()
            elif stage_num == 7:
                player.rect.bottom += y_vel 
                y_vel += 1
                if player.rect.left > seventy_first_wall.rect.right and player.rect.right < seventy_second_wall.rect.left:
                    y_vel += 0
                else:
                    if player.rect.bottom > seventy_first_wall.rect.y:
                        y_vel = 0
                seventy_ball_dead_wall.draw_wall()
                seventy_first_wall.draw_wall()
                seventy_second_wall.draw_wall()
                seventy_third_wall.draw_wall()
                seventy_first_human_dead_wall.draw_wall()
                seventy_second_human_dead_wall.draw_wall()
                seventy_third_human_dead_wall.draw_wall()
                seventy_fourty_human_dead_wall.draw_wall()
            if stage_num != 7:
                '''
                #오른쪽,왼쪽 경계 정하기(볼)
                if stuff.rect.x < 0:
                   if stuff.ball_direction_of_rotation_right == True:
                      is_ball_wall = True
                      stuff.rect.x = 0
                      stuff.ball_direction_of_rotation_right = False
                   else:
                      is_ball_wall = True
                      stuff.rect.x = 0
                      stuff.ball_direction_of_rotation_right = True
                elif stuff.rect.right > 1600:
                    if stuff.ball_direction_of_rotation_right == True:
                       is_ball_wall = True
                       stuff.rect.x = width - stuff.ball_width
                       stuff.ball_direction_of_rotation_right = False
                    else:
                        is_ball_wall = True
                        stuff.rect.x = width - stuff.ball_width
                        stuff.ball_direction_of_rotation_right = True
                else:
                    is_ball_wall = False
                #위, 아래쪽 경계 정하기(볼)
                if stuff.rect.y < 100:
                    if stuff.ball_direction_of_rotation_right == True:
                       is_ball_wall = True
                       stuff.rect.y = 100
                       stuff.ball_direction_of_rotation_right = False
                    else:
                       is_ball_wall = True
                       stuff.rect.y = 100
                       stuff.ball_direction_of_rotation_right = True
                elif stuff.rect.y > 700:
                    if stuff.ball_direction_of_rotation_right == True:
                       is_ball_wall = True
                       stuff.rect.y = 700
                       stuff.ball_direction_of_rotation_right = False
                    else:
                       is_ball_wall = True
                       stuff.rect.y = 700
                       stuff.ball_direction_of_rotation_right = True
                else:
                    is_ball_wall = False
                '''
                if player.rect.bottom > base_bottom_wall.rect.y:
                    player.rect.bottom = base_bottom_wall.rect.y
                elif player.rect.top < base_top_wall.rect.top:
                    player.rect.top = base_top_wall.rect.bottom
                    #중력
                    player.rect.bottom += y_vel 
                    y_vel += 1
                    if  player.rect.bottom > base_bottom_wall.rect.y:
                        y_vel = 0
                base_top_wall.draw_wall()
                base_bottom_wall.draw_wall()

            player.draw_car()
            player.move_x()
            player.update()
            player.check_screen()
            player.gravity()
            stuff.draw_ball()
            stuff.move_distance() 

        if isCome_outHero == False:
            Start_Button.process()
            Start_Button.draw_button()#if 문 밖에서 실행하면 실행이 됨

        ''' 게임 코드 끝 '''
        pygame.display.flip()

        # 초당 프레임 설정
        clock.tick(60)
if __name__ == '__main__':
    main()