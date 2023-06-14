# Imports
import sys
import pygame
import time

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
font1 = pygame.font.Font('Maplestory Bold.ttf',20)
running = True
K_is = 0
G_is = 0
L_is = 0
S_is = 0
m_s =0
m_s1 = 0
kg = 0
kg1 = 0
o_is = 0
p = 0
p_is =0

#텍스트1
text1 = '1'
img1 = font1.render(text1,True,(0,0,0))
rect1 = img1.get_rect()
rect1.topleft = (20,250)
cursor1 = pygame.Rect(rect1.topright,(3,rect1.height))
print(cursor1)

#텍스테2
text2 = '1'
img2 = font1.render(text2,True,(0,0,0))
rect2 = img1.get_rect()
rect2.topleft = (1170,250)
cursor2 = pygame.Rect(rect2.topright,(3,rect2.height))
print(cursor2)

#텍스트3
text3 = '1'
img3 = font1.render(text3,True,(0,0,0))
rect3 = img1.get_rect()
rect3.topleft = (230,250)
cursor3 = pygame.Rect(rect3.topright,(3,rect3.height))
print(cursor3)

#텍스트4
text4 = '1'
img4 = font1.render(text2,True,(0,0,0))

rect4 = img1.get_rect()
rect4.topleft = (1370,250)
cursor4 = pygame.Rect(rect4.topright,(3,rect4.height))
print(cursor4)

#버튼1
objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
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

        objects.append(self)

    def process(self):

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
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    global K_is,L_is,S_is,G_is
    K_is = 1
    L_is = 0
    S_is = 0
    G_is = 0
    print(image1_po.x)
def myFunction1():
    global K_is,L_is,S_is,G_is
    K_is = 0
    L_is = 1
    S_is = 0
    G_is = 0
def myFunction2():
    global K_is,L_is,S_is,G_is
    K_is = 0
    L_is = 0
    S_is = 0
    G_is = 1
def myFunction3():
    global K_is,L_is,S_is,G_is
    K_is = 0
    L_is = 0
    S_is = 1
    G_is = 0
def startbutton():
    global o_is
    global isBumped
    o_is = 1
    isBumped = False
def resetbutton():
    global o_is,image1_po,image_po,p_is
    o_is = 0
    p_is = 0
    image1_po = image1.get_rect(centerx=1350, bottom=200)
    image_po = image.get_rect(centerx=150, bottom=200)

customButton = Button(200, 500, 200, 100, '속력1', myFunction)
customButton = Button(500, 500, 200, 100, '질량1', myFunction1)
customButton = Button(800, 500, 200, 100, '속력2', myFunction2)
customButton = Button(1100, 500, 200, 100, '질량2', myFunction3)
customButton = Button(500, 300, 200, 100, '시작', startbutton)
customButton = Button(800, 300, 200, 100, '리셋', resetbutton)
#m/s kg
tex = font1.render('m/s',True,(0,0,0))
tex1 = font1.render('m/s',True,(0,0,0))
tex2 = font1.render('kg',True,(0,0,0))
tex3 = font1.render('kg',True,(0,0,0))

# running status
isBumped = False

#이미지
image1= pygame.image.load('dow.png')
image = pygame.image.load('dw.png')
image1_po = image1.get_rect(centerx=1350, bottom=200)
image_po = image.get_rect(centerx=150, bottom=200)

# Game loop.
while running:
    #생성
    screen.fill((255, 255, 255))
    screen.fill((255, 255, 255)) 
    screen.blit(image1, image1_po)
    screen.blit(image, image_po)
    screen.blit(img1,rect1) 
    screen.blit(img2,rect2) 
    screen.blit(img3,rect3) 
    screen.blit(img4,rect4) 
    screen.blit(tex,(150,250))
    screen.blit(tex1,(1300,250))
    screen.blit(tex2,(360,250))
    screen.blit(tex3,(1500,250))
    if abs(image_po.x+(image_po.width/2) - image1_po.x-(image1_po.width/2)) < image_po.width:
        o_is = 0
        p_is = 1
        isBumped = True
        print(time.time(), "bumped")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       #텍스트1       
        if K_is == 1:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text1)> 0:
                    text1 = text1[:-1]
                    
            else:
                text1 += event.unicode
                print("o")
            img1 = font1.render(text1,True,(0,0,0))
            rect1.size = img1.get_size()
            cursor1.topleft = rect1.topright

        #텍스트2        
        if G_is == 1:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text2)> 0:
                    text2 = text2[:-1]
                    
            else:
                text2 += event.unicode
                print("o")
            img2 = font1.render(text2,True,(0,0,0))
            rect2.size = img2.get_size()
            cursor2.topleft = rect2.topright
        #텍스트3
        if L_is == 1:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text3)> 0:
                    text3 = text3[:-1]
                    
            else:
                text3 += event.unicode
                print("o")
            img3 = font1.render(text3,True,(0,0,0))
            rect3.size = img3.get_size()
            cursor3.topleft = rect3.topright
        #텍스트4
        if S_is == 1:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text4)> 0:
                    text4 = text4[:-1]
                    
            else:
                text4 += event.unicode
                print("o")
            img4 = font1.render(text4,True,(0,0,0))
            rect4.size = img4.get_size()
            cursor4.topleft = rect4.topright 
    #운동
    if o_is == 1 and not isBumped:
        m_s = float(text1)
        kg = float(text3)
        m_s1 = float(text2)
        kg1 = float(text4)
        image1_po.x -= m_s1 * fpsClock.tick(fps)
        image_po.x += m_s * fpsClock.tick(fps)
    # 충돌 체크
    if p_is == 1:
       p = (m_s * kg) + (m_s1 * kg1)
       m_s = (p/2)/kg
       m_s1 = (p/2)/kg1
       image1_po.x +=  m_s1 * fpsClock.tick(fps)
       image_po.x -= m_s * fpsClock.tick(fps)
    #버튼
    for object in objects:
        object.process()

    pygame.display.flip()

    #빨간줄
    if time.time() % 1 > 0.5:
        if K_is == 1:
         pygame.draw.rect(screen, (255,0,0), cursor1)
        if G_is == 1:
         pygame.draw.rect(screen, (255,0,0), cursor2)
        if L_is == 1:
         pygame.draw.rect(screen, (255,0,0), cursor3)
        if S_is == 1:
         pygame.draw.rect(screen, (255,0,0), cursor4)
    fpsClock.tick(fps)
