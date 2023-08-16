import pygame as pg
from setting import *
from sprites import *
from os import path


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption(TiTLE)
        self.clock = pg.time.Clock()
        self.running = True
        #self.background_sound = pg.mixer.music.load("main_theme.mp3")
        #pg.mixer.music.play(-1)
        #pg.mixer.music.set_volume(0.3)

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.top_platoforms = pg.sprite.Group()
        self.base_wall = pg.sprite.Group()
        #
        self.first_wall = pg.sprite.Group()
        self.first_platforms = pg.sprite.Group()
        self.firts_base_platforms = pg.sprite.Group()
        #
        self.second_wall = pg.sprite.Group()
        self.second_platforms = pg.sprite.Group()
        self.second_base_platforms = pg.sprite.Group()
        #
        self.third_wall = pg.sprite.Group()
        self.third_platforms = pg.sprite.Group()
        #
        self.fourth_platforms = pg.sprite.Group()
        #
        self.fourth_wall = pg.sprite.Group()
        #
        self.fifth_wall = pg.sprite.Group()
        #
        self.sixth_wall = pg.sprite.Group()
        #
        self.seventh_wall = pg.sprite.Group()
        #
        self.Button = pg.sprite.Group()
        #player,ball
        self.player = Player()
        self.all_sprites.add(self.player)
        self.ball = ball()
        self.all_sprites.add(self.ball)
        #base
        base_bottom_wall = Platform(0,800,1600,100,1)
        self.base_wall.add(base_bottom_wall)
        self.platforms.add(base_bottom_wall)
        #
        base_top_wall = Platform(0,0,1600,100,1)
        self.base_wall.add(base_top_wall)
        self.top_platoforms.add(base_top_wall)
        # first
        first_first_wall = Platform(600,600,80,60,1)
        self.first_wall.add(first_first_wall)
        self.first_platforms.add(first_first_wall)
        first_first_base_wall = Platform(600,660,80,240,1)
        self.first_wall.add(first_first_base_wall)
        self.firts_base_platforms.add(first_first_base_wall)
        #
        first_second_wall = Platform(900,500,80,60,1)
        self.first_wall.add(first_second_wall)
        self.first_platforms.add(first_second_wall)
        first_second_base_wall = Platform(900,560,80,340,1)
        self.first_wall.add(first_second_base_wall)
        self.firts_base_platforms.add(first_second_base_wall)
        #
        first_third_wall = Platform(1200,500,80,60,1)
        self.first_wall.add(first_third_wall)
        self.first_platforms.add(first_third_wall)
        first_third_base_wall = Platform(1200,560,80,340,1)
        self.first_wall.add(first_third_base_wall)
        self.firts_base_platforms.add(first_third_base_wall)
        #second
        second_first_wall = Platform(800,350,300,100,1)
        self.second_wall.add(second_first_wall)
        self.second_platforms.add(second_first_wall)
        second_first_base_wall = Platform(800,450,300,450,1)
        self.second_wall.add(second_first_base_wall)
        self.second_base_platforms.add(second_first_base_wall)
        #third
        third_ball_dead_wall = Platform(600,0,10,1000,1)
        self.third_wall.add(third_ball_dead_wall)
        #self.third_platforms.add(third_ball_dead_wall)
        #
        third_human_dead_wall = Platform(1100,0,10,1000,1)
        self.third_wall.add(third_human_dead_wall)
        #self.third_platforms.add(third_human_dead_wall)
        #four
        fourty_first_ball_dead_wall = Platform(850,0,10,450,1)
        self.fourth_wall.add(fourty_first_ball_dead_wall)
        #self.fourth_platforms.add(fourty_first_ball_dead_wall)
        #
        fourty_second_ball_dead_wall = Platform(1300,450,10,450,1)
        self.fourth_wall.add(fourty_second_ball_dead_wall)
        #self.fourth_platforms.add(fourty_second_ball_dead_wall)
        #
        fourty_first_human_dead_wall = Platform(850,450,10,450,1)
        self.fourth_wall.add(fourty_first_human_dead_wall)
        #self.fourth_platforms.add(fourty_first_human_dead_wall)
        #
        fourty_second_human_dead_wall = Platform(1300,0,10,450,1)
        self.fourth_wall.add(fourty_second_human_dead_wall)
        #self.fourth_platforms.add(fourty_second_human_dead_wall)
        #
        fourty_first_wall = Platform(700,450,1300,20,1)
        self.fourth_wall.add(fourty_first_wall)
        self.fourth_platforms.add(fourty_first_wall)
        #button
        self.Start_button = Button(520, 300, 500, 200, 'Start')
        self.Button.add(self.Start_button)
        self.run()
    
    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updata()
            self.draw()

    def updata(self):
        # Game loop - Updata
        global stage_num, IsCome_player
        if IsCome_player == False:
            self.Button.update()
            self.Start_button.process()
            if self.Start_button.fuc:
                IsCome_player = True
                self.player.stage_number = 1
        if IsCome_player:
            self.all_sprites.update()
            if self.ball.ball_direction_of_rotation_right == True:
                self.ball.angle += self.ball.ball_speed
                self.ball.rect.x = self.player.rect.x + int(math.cos(self.ball.angle) * self.ball.ball_hero_distance)
                self.ball.rect.y = self.player.rect.y + int(math.sin(self.ball.angle) * self.ball.ball_hero_distance)
            else:
                self.ball.angle -= self.ball.ball_speed
                self.ball.rect.x = self.player.rect.x + int(math.cos(self.ball.angle) * self.ball.ball_hero_distance)
                self.ball.rect.y = self.player.rect.y + int(math.sin(self.ball.angle) * self.ball.ball_hero_distance)
            top_hit = pg.sprite.spritecollide(self.player, self.top_platoforms,False)
            if top_hit:
                    self.player.rect.top = top_hit[0].rect.bottom
            if stage_num != 7:
                self.base_wall.update()
                bottom_hit = pg.sprite.spritecollide(self.player, self.platforms, False)
                if bottom_hit:
                   self.player.rect.bottom = bottom_hit[0].rect.top
                   self.player.v = VELOCITY
                   self.player.IsJump = 0
                   self.player.y_vel = 0
            if stage_num == 1:
                self.first_wall.update()
                ball_first_hits = pg.sprite.spritecollide(self.ball,self.firts_base_platforms, False)
                ball_first_hit = pg.sprite.spritecollide(self.ball,self.first_platforms, False)
                hits = pg.sprite.spritecollide(self.player,self.firts_base_platforms, False)
                hit = pg.sprite.spritecollide(self.player,self.first_platforms, False)
                if hits and hit:
                    if self.player.rect.right > hits[0].rect.left and self.player.rect.left < hits[0].rect.right:
                        self.player.rect.left = hits[0].rect.right
                    if self.player.rect.right > hits[0].rect.left:
                        self.player.rect.right = hits[0].rect.left
                    if self.player.rect.left < hits[0].rect.right:
                         self.player.rect.left = hits[0].rect.right
                elif hits:
                    if self.player.rect.right > hits[0].rect.left and self.player.rect.left < hits[0].rect.right:
                        self.player.rect.left = hits[0].rect.right
                    elif self.player.rect.right > hits[0].rect.left:
                        self.player.rect.right = hits[0].rect.left
                    elif self.player.rect.left < hits[0].rect.right:
                         self.player.rect.left = hits[0].rect.right
                elif hit:
                    self.player.rect.bottom = hit[0].rect.top
                    self.player.v = VELOCITY
                    self.player.IsJump = 0
                    self.player.y_vel = 0
                if ball_first_hits or ball_first_hit:
                    if self.ball.ball_direction_of_rotation_right == True:
                        self.ball.ball_direction_of_rotation_right = False
                    else:
                        self.ball.ball_direction_of_rotation_right = True
                                     
            if stage_num == 2:
                self.second_wall.update()
                hits = pg.sprite.spritecollide(self.player, self.second_platforms, False)
                if hits:
                   self.player.rect.bottom = hits[0].rect.top
                   self.player.vy = VELOCITY
            if stage_num == 3:
                self.third_wall.update()
                hits = pg.sprite.spritecollide(self.player, self.third_platforms, False)
                if hits:
                   self.player.rect.bottom = hits[0].rect.top
                   self.player.vy = VELOCITY
            if stage_num == 4:
                self.fourth_wall.update()
                hits = pg.sprite.spritecollide(self.player, self.fourth_platforms, False)
                if hits:
                   self.player.rect.bottom = hits[0].rect.top
                   self.player.vy = VELOCITY
            if stage_num == 5:
                self.fifth_wall.update()
            if stage_num == 6:
                self.sixth_wall.update()
            if stage_num == 7:
                self.seventh_wall.update()
            stage_num = self.player.stage_number
            
    def events(self):
        #Game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
               if self.playing:
                   self.playing = False
               self.running = False
            if IsCome_player:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        if self.player.IsJump == 0:
                            self.player.jump(1)
                    if event.key == pg.K_SPACE:
                       self.player.rect.x = self.ball.rect.x
                       self.player.rect.y = self.ball.rect.y
                       self.ball.angle += math.pi
                        
    def draw(self):
        # Game loop - draw
        self.screen.fill(blue)
        if IsCome_player == False:
            self.Button.draw(self.screen)
        if IsCome_player:
            if stage_num == 1:
                self.first_wall.draw(self.screen)
            if stage_num == 2:
                self.second_wall.draw(self.screen)
            if stage_num == 3:
                self.third_wall.draw(self.screen)
            if stage_num == 4:
                self.fourth_wall.draw(self.screen)
            if stage_num == 5:
                self.fifth_wall.draw(self.screen)
            if stage_num == 6:
                self.sixth_wall.draw(self.screen)
            if stage_num == 7:
                self.seventh_wall.draw(self.screen)
            if stage_num != 7:
                self.base_wall.draw(self.screen)
            self.all_sprites.draw(self.screen)
        # *after* drawing everyting,flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/ continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()