import pyglet
import random as rm
settings_m = False
sett_m = False
m_v = 0.01
g_v = 0.01
G_v = 1
s_v = 1
# window game
class GameScreen(pyglet.window.Window):
    def __init__(self):
        super().__init__(1200, 1000) # caption='Game Screen'
        global G_player
        self.b_pause = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_play_M.png'), x = 25, y = 940)
        self.b_bg_bt = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/bg_f_bt.png'), x = 600, y = 600)
        self.b_ct = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_continue.png'), x = 610, y = 735)
        self.b_play_M = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_pause.png'), x = 25, y = 940)
        self.b_exit = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_exit.png'), x = 610, y = 615)
        self.b_settings = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_Settings.png'), x = 610, y = 675)
        self.character = pyglet.sprite.Sprite(pyglet.resource.image('img/game/charecter.png'), x = 550, y = 0)
        self.hitbox_cr = pyglet.shapes.Rectangle(x=self.character.x, y=self.character.y, width=self.character.width, height=10, color=(0,0,0,0))
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.jump_count = 1
        self.platform1 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x = 30, y = 30)
        self.hitbox_pf1 = pyglet.shapes.Rectangle(x = self.platform1.x, y = self.platform1.y, width=self.platform1.width, height=self.platform1.height, color=(0,0,0,0))
        self.bg = pyglet.sprite.Sprite(pyglet.resource.image('img/game/bg.png'), x= 0, y = 0)
        self.platform2 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x = 180, y = 70)
        self.hitbox_pf2 = pyglet.shapes.Rectangle(x = self.platform2.x, y = self.platform2.y, width=self.platform2.width, height=self.platform2.height, color=(0,0,0,0))
        self.platform3 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x = 360, y = 125)
        self.hitbox_pf3 = pyglet.shapes.Rectangle(x =self.platform3.x, y = self.platform3.y, width=self.platform3.width, height=self.platform3.height, color=(0,0,0,0))
        self.platform4 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 230, y= 160)
        self.hitbox_pf4 = pyglet.shapes.Rectangle(x= self.platform4.x, y= self.platform4.y, width=self.platform4.width, height=self.platform4.height)
        self.platform5 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 380, y= 220)
        self.hitbox_pf5 = pyglet.shapes.Rectangle(x= self.platform5.x, y= self.platform5.y, width=self.platform5.width, height=self.platform5.height)
        self.platform6 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 550, y= 250)
        self.hitbox_pf6 = pyglet.shapes.Rectangle(x= self.platform6.x, y= self.platform6.y, width=self.platform6.width, height=self.platform6.height)
        self.platform7 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 680, y= 290)
        self.hitbox_pf7 = pyglet.shapes.Rectangle(x= self.platform7.x, y= self.platform7.y, width=self.platform7.width, height=self.platform7.height)
        self.platform8 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 760, y= 360)
        self.hitbox_pf8 = pyglet.shapes.Rectangle(x= self.platform8.x, y= self.platform8.y, width=self.platform8.width, height=self.platform8.height)
        self.platform9 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 838, y= 400)
        self.hitbox_pf9 = pyglet.shapes.Rectangle(x= self.platform9.x, y= self.platform9.y, width=self.platform9.width, height=self.platform9.height)
        self.platform10 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 960, y= 441)
        self.hitbox_pf10 = pyglet.shapes.Rectangle(x= self.platform10.x, y= self.platform10.y, width=self.platform10.width, height=self.platform10.height)
        self.platform11 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 1100, y= 500)
        self.hitbox_pf11 = pyglet.shapes.Rectangle(x= self.platform11.x, y= self.platform11.y, width=self.platform11.width, height=self.platform11.height)
        self.platform12 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= 1000, y= 560)
        self.hitbox_pf12 = pyglet.shapes.Rectangle(x= self.platform12.x, y= self.platform12.y, width=self.platform12.width, height=self.platform12.height)
        self.p_n_l = pyglet.sprite.Sprite(pyglet.resource.image('img/game/p_n_l.png'), x =self.platform12.x, y = self.platform12.y + 18)
        self.hitbox_p_n_l = pyglet.shapes.Rectangle(x = self.p_n_l.x, y = self.p_n_l.y, width=self.p_n_l.width, height=self.p_n_l.height)
        self.cannon = pyglet.sprite.Sprite(pyglet.resource.image('img/game/cannon.png'), x = 0, y = self.character.y)
        self.shell = pyglet.sprite.Sprite(pyglet.resource.image('img/game/shell.png'), x = self.cannon.x, y = self.cannon.y + 35)
        self.hitbox_s = pyglet.shapes.Rectangle(x = self.shell.x, y = self.shell.y, width=self.shell.width, height=self.shell.height)
        self.hitbox_cr2 = pyglet.shapes.Rectangle(x= self.character.x, y = self.character.y, width=self.character.width, height=self.character.height)
        self.shell_2 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/shell.png'), x = -50, y = self.cannon.y + 35)
        self.hitbox_s_2 = pyglet.shapes.Rectangle(x=self.shell_2.x, y=self.shell_2.y, width=self.shell_2.width, height=self.shell_2.height)
        self.P_R = pyglet.sprite.Sprite(pyglet.resource.image('img/game/P_R.png'), x = 550, y = 450)
        self.p_n_l_2 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/p_n_l_2.png'), x=-100, y=-100)
        self.hitbox_p_n_l_2 = pyglet.shapes.Rectangle(x=self.p_n_l_2.x, y=self.p_n_l_2.y, width=self.p_n_l_2.width, height=self.p_n_l_2.height)
        self.cannon_2 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/cannon.png'), x=0, y =self.character.y)
        self.cannon_3 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/cannon.png'), x=1200, y =self.character.y) 
        self.cannon_4 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/cannon.png'), x=1200, y =self.character.y)
        self.shell3 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/shell.png'), x = self.cannon_2.x, y = self.cannon_2.y + 35)
        self.hitbox_s_3 = pyglet.shapes.Rectangle(x = self.shell3.x, y = self.shell3.y, width=self.shell3.width, height=self.shell3.height)
        self.shell_4 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/shell.png'), x = self.cannon_3.x, y = self.cannon_3.y + 35)
        self.hitbox_s_4 = pyglet.shapes.Rectangle(x = self.shell_4.x, y = self.shell_4.y, width=self.shell_4.width, height=self.shell_4.height)
        self.platform13 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= -200, y= -200)
        self.hitbox_pf13 = pyglet.shapes.Rectangle(x= self.platform13.x, y= self.platform13.y, width=self.platform13.width, height=self.platform13.height)
        self.platform14 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= -200, y= -200)
        self.hitbox_pf14 = pyglet.shapes.Rectangle(x= self.platform14.x, y= self.platform14.y, width=self.platform14.width, height=self.platform14.height)
        self.platform15 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= -200, y= -200)
        self.hitbox_pf15 = pyglet.shapes.Rectangle(x= self.platform15.x, y= self.platform15.y, width=self.platform15.width, height=self.platform15.height)
        self.platform16 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= -200, y= -200)
        self.hitbox_pf16 = pyglet.shapes.Rectangle(x= self.platform16.x, y= self.platform16.y, width=self.platform16.width, height=self.platform16.height)
        self.platform17 = pyglet.sprite.Sprite(pyglet.resource.image('img/game/platform.png'), x= -200, y= -200)
        self.hitbox_pf17 = pyglet.shapes.Rectangle(x= self.platform17.x, y= self.platform17.y, width=self.platform17.width, height=self.platform17.height)
        self.p_t_e = pyglet.sprite.Sprite(pyglet.resource.image('img/game/p_t_e.png'), x = -200, y = -200)
        self.hitbox_p_t_e = pyglet.shapes.Rectangle(x=self.p_t_e.x, y= self.p_t_e.y, width=self.p_t_e.width, height=self.p_t_e.height)
        self.t_p = pyglet.sprite.Sprite(pyglet.resource.image('img/game/T_P.png'), x = 0, y= 0)

        music = pyglet.media.load('music/game/2.mp3')
        G_player = pyglet.media.Player()
        G_player.queue(music)
        G_player.volume = g_v
        G_player.loop = True
        G_player.pause()

        self.b_press = False
        self.b_cont = True
        # variables second lvl
        self.colission1 = False
        self.lvl_1_c = False
        self.lvl_1_c2  = False
        self.shoot = True
        self.shoot_shell_2 = False
        self.shoot_scine_cannon = True
        self.death = False
        self.restart = False
        # variables third lvl
        self.st_lvl_3 = False
        self.shoot_shell_0 = False
        self.shoot_shell_1 = False
        self.shoot_shell_2 = False
        self.shoot_shell_3 = False
        self.st_shoot = False
        self.time_shoot = 0
        self.on_off = False
        self.last_y_shell_1 = 0
        self.last_y_shell_3 = 0
        self.last_y_shell_4 = 0
        self.last_y_shell_5 = 0
        self.shoot_scine_cannon_1 = True
        self.shoot_scine_cannon_2 = True
        self.shoot_scine_cannon_3 = True
        self.shoot_scine_cannon_4 = True
        self.t_e = False
        self.v_t_e = 0

        self.r_value = rm.randrange(300, 310)
        self.l_y_shell = 0
        self.l_y_shell2 = 0
        pyglet.clock.schedule_interval(self.update, 1/60)

    def chek_collishon(self, f_hitbox, t_hitbox):
        x1 = f_hitbox.x
        y1 = f_hitbox.y
        x2 = f_hitbox.x + f_hitbox.width
        y2 = f_hitbox.y + f_hitbox.height

        x3 = t_hitbox.x
        y3 = t_hitbox.y
        x4 = t_hitbox.x + t_hitbox.width
        y4 = t_hitbox.y + t_hitbox.height
        if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
            return True
        else:
            return False

    def on_draw(self):
        self.clear()

        if self.b_press:
            self.clear()
            self.bg.draw()
            self.platform1.draw()
            self.platform2.draw()
            self.platform3.draw()
            self.platform4.draw()
            self.platform5.draw()
            self.platform6.draw()
            self.platform7.draw()
            self.platform8.draw()
            self.platform9.draw()
            self.platform10.draw()
            self.platform11.draw()
            self.platform12.draw()
            self.p_n_l.draw()
            if self.lvl_1_c2:
                self.cannon.draw()
                self.shell.draw()
                self.shell_2.draw()
                self.p_n_l_2.draw()
            if self.st_lvl_3:
                self.cannon.draw()
                self.cannon_2.draw()
                self.cannon_3.draw()
                self.cannon_4.draw()
                self.shell.draw()
                self.shell_2.draw()
                self.shell3.draw()
                self.shell_4.draw()
                self.platform13.draw()
                self.platform14.draw()
                self.platform15.draw()
                self.platform16.draw()
                self.platform17.draw()
                self.p_t_e.draw()
            self.character.draw()
            self.b_play_M.draw()
            self.b_bg_bt.draw()
            self.b_ct.draw()
            self.b_exit.draw()
            self.b_settings.draw()
        if self.b_cont:
            self.clear()
            self.bg.draw()
            self.b_pause.draw()
            self.platform1.draw()
            self.platform2.draw()
            self.platform3.draw()
            self.platform4.draw()
            self.platform5.draw()
            self.platform6.draw()
            self.platform7.draw()
            self.platform8.draw()
            self.platform9.draw()
            self.platform10.draw()
            self.platform11.draw()
            self.platform12.draw()
            self.p_n_l.draw()
            self.character.draw()
            if self.lvl_1_c2:
                self.cannon.draw()
                self.shell.draw()
                self.shell_2.draw()
                self.p_n_l_2.draw()
            if self.st_lvl_3:
                self.cannon.draw()
                self.cannon_2.draw()
                self.cannon_3.draw()
                self.cannon_4.draw()
                self.shell.draw()
                self.shell_2.draw()
                self.shell3.draw()
                self.shell_4.draw()
                self.platform13.draw()
                self.platform14.draw()
                self.platform15.draw()
                self.platform16.draw()
                self.platform17.draw()
                self.p_t_e.draw()
            if self.death:
                self.P_R.draw()
            if self.t_e:
                self.t_p.draw()
        
    def update(self, dt):
        self.hitbox_s.x = self.shell.x
        self.hitbox_s.y = self.shell.y
        self.hitbox_cr.x = self.character.x
        self.hitbox_cr.y = self.character.y
        if self.shoot:
            self.shell.y = self.cannon.y + 35
        if self.shoot_scine_cannon:
            self.shell_2.y = self.cannon.y + 35
        self.hitbox_s_2.x = self.shell_2.x
        self.hitbox_s_2.y = self.shell_2.y
        self.cannon.y = self.character.y
        self.hitbox_cr2.x = self.character.x
        self.hitbox_cr2.y = self.character.y
        if self.lvl_1_c:
            self.character.x = 550
            self.character.y = 0
            self.hitbox_cr.x = self.character.x
            self.hitbox_cr.y = self.character.y
            self.hitbox_cr2.x = self.character.x
            self.hitbox_cr2.y = self.character.y
            self.platform1.x = 30 + self.r_value
            self.platform1.y = 30
            self.platform2.x = 180 + self.r_value
            self.platform2.y = 70
            self.platform3.x = 360 + self.r_value
            self.platform3.y = 125
            self.platform4.x = 230 + self.r_value
            self.platform4.y = 160
            self.platform5.x = 380 + self.r_value
            self.platform5.y = 220
            self.platform6.x = 550 + self.r_value
            self.platform6.y = 250
            self.platform7.x = 680 + self.r_value
            self.platform7.y = 290
            self.platform8.x = 760 + self.r_value
            self.platform8.y = 360
            self.platform9.x = 838 + self.r_value
            self.platform9.y = 400
            self.platform10.x = 960 + 100
            self.platform10.y = 441
            self.platform11.x = 1100 
            self.platform11.y = 500
            self.platform12.x = 1000 
            self.platform12.y = 560

            self.hitbox_pf1.x = self.platform1.x
            self.hitbox_pf1.y = self.platform1.y
            self.hitbox_pf2.x = self.platform2.x
            self.hitbox_pf2.y = self.platform2.y
            self.hitbox_pf3.x = self.platform3.x
            self.hitbox_pf3.y = self.platform3.y
            self.hitbox_pf4.x = self.platform4.x
            self.hitbox_pf4.y = self.platform4.y
            self.hitbox_pf5.x = self.platform5.x
            self.hitbox_pf5.y = self.platform5.y
            self.hitbox_pf6.x = self.platform6.x
            self.hitbox_pf6.y = self.platform6.y
            self.hitbox_pf7.x = self.platform7.x
            self.hitbox_pf7.y = self.platform7.y
            self.hitbox_pf8.x = self.platform8.x
            self.hitbox_pf8.y = self.platform8.y
            self.hitbox_pf9.x = self.platform9.x
            self.hitbox_pf9.y = self.platform9.y
            self.hitbox_pf10.x = self.platform10.x
            self.hitbox_pf10.y = self.platform10.y
            self.hitbox_pf11.x = self.platform11.x
            self.hitbox_pf11.y = self.platform11.y
            self.hitbox_pf12.x = self.platform12.x
            self.hitbox_pf12.y = self.platform12.y
            self.lvl_1_c2 = True
            self.p_n_l.x = -100
            self.p_n_l.y = -100
            self.hitbox_p_n_l.x = self.p_n_l.x
            self.hitbox_p_n_l.y = self.p_n_l.y
            self.p_n_l_2.x = self.platform12.x
            self.p_n_l_2.y = self.platform12.y + 18
            self.hitbox_p_n_l_2.x = self.p_n_l_2.x
            self.hitbox_p_n_l_2.y = self.p_n_l_2.y
            self.lvl_1_c = False
        if self.keys[pyglet.window.key.D] and not self.character.x == 1145:
            self.character.x += 5
        elif self.keys[pyglet.window.key.A] and not self.character.x == 0:
            self.character.x -= 5
        if self.jump_count == 0:
            self.character.y -= 1
            if self.character.y == 0:
                self.jump_count = 1
        if not self.character.x < self.platform1.width:
            self.jump_count = 0
            if self.character.y == 0:
                self.jump_count = 1
        # start lvl 3 
        if self.st_lvl_3:
            self.cannon_3.rotation = 180
            self.cannon_4.rotation = 180
            self.cannon_2.y = self.character.y + 166
            self.cannon_3.y = self.character.y + 100
            self.cannon_4.y = self.character.y + 299
            self.hitbox_s.x = self.shell.x
            self.hitbox_s.y = self.shell.y
            self.hitbox_s_2.x = self.shell_2.x
            self.hitbox_s_2.y = self.shell_2.y
            self.hitbox_s_3.x = self.shell3.x
            self.hitbox_s_3.y = self.shell3.y
            self.hitbox_s_4.x = self.shell_4.x
            self.hitbox_s_4.y = self.shell_4.y
            if self.shoot_scine_cannon_1:
                self.shell.y = self.cannon.y + 35
            if self.shoot_scine_cannon_2:
                self.shell_2.y = self.cannon_2.y + 35
            if self.shoot_scine_cannon_3:
                self.shell3.y = self.cannon_3.y - 65
            if self.shoot_scine_cannon_4:
                self.shell_4.y = self.cannon_4.y - 65
            if self.time_shoot == 120 and not self.shoot_shell_0:
                self.shoot_shell_0 = True
                self.shoot_shell_2 = True
            else:
                self.time_shoot += 1
            if self.chek_collishon(self.hitbox_cr2, self.shell):
                self.death = True
                pyglet.clock.unschedule(self.update)
            if self.chek_collishon(self.hitbox_cr2, self.shell_2):
                self.death = True
                pyglet.clock.unschedule(self.update)
            if self.chek_collishon(self.hitbox_cr2, self.shell3):
                self.death = True
                pyglet.clock.unschedule(self.update)
            if self.chek_collishon(self.hitbox_cr2, self.shell_4):
                self.death = True
                pyglet.clock.unschedule(self.update)
            if self.chek_collishon(self.hitbox_cr, self.hitbox_p_t_e):
                self.t_e = True
            
        if self.on_off:
            self.jump_count = 1
            self.character.x = 550
            self.character.y = 3
            self.shell.x = -50
            self.shell_2.x = -50
            self.shell3.x = 1200
            self.shell_4.x = 1200
            self.hitbox_p_n_l_2.x = self.p_n_l_2.x
            self.hitbox_p_n_l_2.y = self.p_n_l_2.y
            # move coordinates platform
            self.platform1.x = 300
            self.platform1.y = 30
            self.platform2.x = 408
            self.platform2.y = 70
            self.platform3.x = 516
            self.platform3.y = 125
            self.platform4.x = 624
            self.platform4.y = 160
            self.platform5.x = 732
            self.platform5.y = 220
            self.platform6.x = 840
            self.platform6.y = 250
            self.platform7.x = 948
            self.platform7.y = 290
            self.platform8.x = 840
            self.platform8.y = 360
            self.platform9.x = 732
            self.platform9.y = 400
            self.platform10.x = 624
            self.platform10.y = 441
            self.platform11.x = 516
            self.platform11.y = 500
            self.platform12.x = 408
            self.platform12.y = 560
            self.platform13.x = 300
            self.platform13.y = 608
            self.platform14.x = 408
            self.platform14.y = 656
            self.platform15.x = 516
            self.platform15.y = 704
            self.platform16.x = 624
            self.platform16.y = 752
            self.platform17.x = 732
            self.platform17.y = 800

            self.p_t_e.x = self.platform17.x
            self.p_t_e.y = self.platform17.y + 19

            self.hitbox_p_t_e.x = self.p_t_e.x
            self.hitbox_p_t_e.y = self.p_t_e.y

            self.hitbox_pf1.x = self.platform1.x
            self.hitbox_pf1.y = self.platform1.y
            self.hitbox_pf2.x = self.platform2.x
            self.hitbox_pf2.y = self.platform2.y
            self.hitbox_pf3.x = self.platform3.x
            self.hitbox_pf3.y = self.platform3.y
            self.hitbox_pf4.x = self.platform4.x
            self.hitbox_pf4.y = self.platform4.y
            self.hitbox_pf5.x = self.platform5.x
            self.hitbox_pf5.y = self.platform5.y
            self.hitbox_pf6.x = self.platform6.x
            self.hitbox_pf6.y = self.platform6.y
            self.hitbox_pf7.x = self.platform7.x
            self.hitbox_pf7.y = self.platform7.y
            self.hitbox_pf8.x = self.platform8.x
            self.hitbox_pf8.y = self.platform8.y
            self.hitbox_pf9.x = self.platform9.x
            self.hitbox_pf9.y = self.platform9.y
            self.hitbox_pf10.x = self.platform10.x
            self.hitbox_pf10.y = self.platform10.y
            self.hitbox_pf11.x = self.platform11.x
            self.hitbox_pf11.y = self.platform11.y
            self.hitbox_pf12.x = self.platform12.x
            self.hitbox_pf12.y = self.platform12.y
            self.hitbox_pf13.x = self.platform13.x
            self.hitbox_pf13.y = self.platform13.y
            self.hitbox_pf14.x = self.platform14.x
            self.hitbox_pf14.y = self.platform14.y
            self.hitbox_pf15.x = self.platform15.x
            self.hitbox_pf15.y = self.platform15.y
            self.hitbox_pf16.x = self.platform16.x
            self.hitbox_pf16.y = self.platform16.y
            self.hitbox_pf17.x = self.platform17.x
            self.hitbox_pf17.y = self.platform17.y

            self.on_off = False
            
        # shoot cannon in 3 lvl
        if self.shoot_shell_0:
            if self.shell.x == 1207:
                self.shell.x = -50
                self.shoot_scine_cannon_1 = True
            else:
                self.shell.x += 3
            if self.shell.x == 130:
                self.shoot_scine_cannon_1 = False
                self.shoot_shell_1 = True
        if self.shoot_shell_1:
            if self.shell_2.x == 1207:
                self.shell_2.x = -50
                self.shoot_scine_cannon_2 = True
            else:
                self.shell_2.x +=3
            if self.shell_2.x == 130:
                self.shoot_scine_cannon_2 = False
        if self.shoot_shell_2:
            if self.shell3.x == -52:
                self.shell3.x = 1200
                self.shoot_scine_cannon_3 = True
            else:
                self.shell3.x -= 4
            if self.shell3.x == 1052:
                self.shoot_scine_cannon_3 = False   
                self.shoot_shell_3 = True
        if self.shoot_shell_3:
            if self.shell_4.x == -52:
                self.shell_4.x = 1200
                self.shoot_scine_cannon_4 = True
            else:
                self.shell_4.x -= 4
            if self.shell_4.x == 1052:
                self.shoot_scine_cannon_4 = False

        if self.t_e:
            if self.v_t_e == 150:
                pyglet.app.exit()
            else:
                self.v_t_e += 1
                print(self.v_t_e)

        # shell move
        if self.lvl_1_c2:
            if self.shell.x == 1200:
                self.shell.x = 0
                self.shoot = True
                self.shell.y = self.cannon.y
            else:
                self.shell.x += 3
            if self.shell.x == 105:
                self.l_y_shell = self.shell.y
                self.shell.y = self.l_y_shell
                self.shoot = False
            if self.shell.x == 450:
                self.shoot_shell_2 = True
                self.shell_2.x = -50
                self.shoot_scine_cannon = True
            if self.shoot_shell_2:
                if self.shell_2.x == 1200:
                    self.shell_2.x = -10
                    self.shoot_shell_2 = False
                else:
                    self.shell_2.x += 4
                if self.shell_2.x == 122:
                    self.l_y_shell2 = self.shell_2.y
                    self.shell_2.y = self.l_y_shell2
                    self.shoot_scine_cannon = False
            if self.chek_collishon(self.hitbox_s, self.hitbox_cr2):
                pyglet.clock.unschedule(self.update)
                self.death = True
            if self.chek_collishon(self.hitbox_cr2, self.hitbox_s_2):
                pyglet.clock.unschedule(self.update)
                self.death = True
        if self.chek_collishon(self.hitbox_cr2, self.hitbox_p_n_l_2):
            self.on_off = True
            self.colission1 = False
            self.lvl_1_c = False
            self.lvl_1_c2  = False
            self.shoot = False
            self.shoot_shell_2 = False
            self.shoot_scine_cannon = False
            self.st_lvl_3 = True
        # reaction when death
        if self.restart:
            self.character.x = 550
            self.character.y = 0
            self.jump_count = 1
            self.shell.x = self.cannon.x
            self.shell.y = self.cannon.y + 35
            self.shell_2.x = -50
            self.shell_2.y = self.cannon.y + 35
            self.restart = False

        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf1):
            self.character.y = self.platform1.y + 16
            self.jump_count = 1
            self.colission1 = True
        else:
            self.colission1 = False
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf2):
            self.character.y = self.platform2.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf3):
            self.character.y = self.platform3.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf4):
            self.character.y = self.platform4.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf5):
            self.character.y = self.platform5.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf6):
            self.character.y = self.platform6.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf7):
            self.character.y = self.platform7.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf8):
            self.character.y = self.platform8.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf9):
            self.character.y = self.platform9.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf10):
            self.character.y = self.platform10.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf11):
            self.character.y = self.platform11.y + 16
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf12):
            self.character.y = self.platform12.y + 17
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf13):
            self.character.y = self.platform13.y + 17
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf14):
            self.character.y = self.platform14.y + 17
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf15):
            self.character.y = self.platform15.y + 17
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf16):
            self.character.y = self.platform16.y + 17
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_pf17):
            self.character.y = self.platform17.y + 17
            self.jump_count = 1
        if self.chek_collishon(self.hitbox_cr, self.hitbox_p_n_l):
            self.lvl_1_c = True
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        global settings_m
        if button == pyglet.window.mouse.LEFT and self.b_pause.x <= x <= self.b_pause.x + self.b_pause.width \
        and self.b_pause.y <= y <= self.b_pause.y + self.b_pause.height:
            self.b_press = True
            self.b_cont = False
            pyglet.clock.unschedule(self.update)
        elif button == pyglet.window.mouse.LEFT and self.b_ct.x <= x <= self.b_ct.x + self.b_ct.width \
        and self.b_ct.y <= y <= self.b_ct.y + self.b_ct.height:
            self.b_cont = True
            self.b_press = False
            pyglet.clock.schedule_interval(self.update, 1/60)
        elif button == pyglet.window.mouse.LEFT and self.b_exit.x <= x <= self.b_exit.x + self.b_exit.width \
        and self.b_exit.y <= y <= self.b_exit.y + self.b_exit.height:
            M_s.set_visible(True)
            G_s.set_visible(False)
            self.b_press = False
            self.b_cont = True
            player.play()
            G_player.pause()
        elif button == pyglet.window.mouse.LEFT and self.b_settings.x <= x <= self.b_settings.x + self.b_settings.width \
        and self.b_settings.y <= y <= self.b_settings.y + self.b_settings.height:
            G_s.set_visible(False)
            S_s.set_visible(True)
            settings_m = True
            player_s.play()
            G_player.pause()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.b_press = True
            self.b_cont = False
            pyglet.clock.unschedule(self.update)
        if symbol == pyglet.window.key.SPACE and self.jump_count == 1:
            self.character.y += (10**2)/2
            self.jump_count -= 1
        if symbol == pyglet.window.key.R and self.death:
            pyglet.clock.schedule_interval(self.update, 1/60)
            self.restart = True
            self.death = False
    def on_close(self):
        pyglet.app.exit()
# window settings
class Settings(pyglet.window.Window):
    def __init__(self):
        super().__init__(1200, 1000)
        global s_v, player_s, m_v, seek
        self.bg_menu = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/bg.png'), x = 0, y = 0)
        self.b_resume = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_continue.png'), x = 1050, y = 900)
        self.b_back = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/b_back.png'), x = 1050, y = 75)
        self.v_plus_b = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/b_plus_m.png'), x = 650, y = 650)
        self.v_minus_b = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/b_minus_m.png'), x = 525, y = 650)
        self.g_plus_b = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/b_plus_m.png'), x = 650, y = 400)
        self.g_minus_b = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/b_minus_m.png'), x = 525, y = 400)


        music = pyglet.media.load('music/menu/1.mp3')
        player_s = pyglet.media.Player()
        player_s.queue(music)
        player_s.volume = m_v
        
        player_s.pause()

        self.v_t = pyglet.text.Label(f'{s_v}', font_size=23,
                         x=self.width // 2, y=self.height - 310,
                         anchor_x='center', anchor_y='top')
        self.txt_m = pyglet.text.Label('menu music', font_size=25,
                         x=self.width // 2, y=self.height - 250,
                         anchor_x='center', anchor_y='top')
        
        self.G_t = pyglet.text.Label(f'{G_v}', font_size=23,
                         x=self.width // 2, y=self.height - 560,
                         anchor_x='center', anchor_y='top')

        self.txt_G = pyglet.text.Label('game music', font_size=25,
                         x=self.width // 2, y=self.height - 510,
                         anchor_x='center', anchor_y='top')

        pyglet.clock.schedule_interval(self.update, 1/60)
    def on_draw(self):
        self.bg_menu.draw()
        self.v_plus_b.draw()
        self.v_minus_b.draw()
        if settings_m:
            self.b_resume.draw()
        elif sett_m:
            self.b_back.draw()
        self.v_t.draw()
        self.txt_m.draw()
        self.txt_G.draw()
        self.G_t.draw()
        self.g_plus_b.draw()
        self.g_minus_b.draw()
    def update(self, dt):
        if self.bg_menu.x == -1500:
            self.bg_menu.x = 0
        else:
            self.bg_menu.x -= 1
    def on_mouse_press(self, x, y, button, modifiers):
        global settings_m, sett_m, s_v, m_v, player_s, player, g_v, G_v
        if button == pyglet.window.mouse.LEFT and self.b_resume.x <= x <= self.b_resume.x + self.b_resume.width \
        and self.b_resume.y <= y <= self.b_resume.y + self.b_resume.height:
            G_s.set_visible(True)
            S_s.set_visible(False)
            settings_m = False
            player_s.pause()
            G_player.play()
        elif button == pyglet.window.mouse.LEFT and self.b_back.x <= x <= self.b_back.x + self.b_back.width \
        and self.b_back.y <= y <= self.b_back.y + self.b_back.height:
            sett_m = False
            S_s.set_visible(False)
            M_s.set_visible(True)
            player_s.pause()
            player.play()
        elif button == pyglet.window.mouse.LEFT and self.v_plus_b.x <= x <= self.v_plus_b.x + self.v_plus_b.width \
        and self.v_plus_b.y <= y <= self.v_plus_b.y + self.v_plus_b.height:
            if not s_v == 100 and not m_v == 1:
                s_v += 1
                self.v_t.text = f'{s_v}'
                m_v += 0.01
                player_s.volume = m_v
                player.volume = m_v
        elif button == pyglet.window.mouse.LEFT and self.v_minus_b.x <= x <= self.v_minus_b.x + self.v_minus_b.width \
        and self.v_minus_b.y <= y <= self.v_minus_b.y + self.v_minus_b.height:
            if not s_v == 1 and not m_v == 0.01:
                s_v -= 1
                self.v_t.text = f'{s_v}'
                m_v -= 0.01
                player_s.volume = m_v
                player.volume = m_v
        elif button == pyglet.window.mouse.LEFT and self.g_plus_b.x <= x <= self.g_plus_b.x + self.g_plus_b.width \
        and self.g_plus_b.y <= y <= self.g_plus_b.y + self.g_plus_b.height:
            if not g_v == 1 and not G_v == 100:
                g_v += 0.01
                G_v += 1
                G_player.volume = g_v
                self.G_t.text = f'{G_v}'
        elif button == pyglet.window.mouse.LEFT and self.g_minus_b.x <= x <= self.g_minus_b.x + self.g_minus_b.width \
        and self.g_minus_b.y <= y <= self.g_minus_b.y + self.g_minus_b.height:
            if not g_v == 0.01 and not G_v == 1:
                g_v -= 0.01
                G_player.volume = g_v
                G_v -= 1
                self.G_t.text = f'{G_v}'
    def on_close(self):
        pyglet.app.exit()
# window menu
class menuscreen(pyglet.window.Window):
    def __init__(self):
        super().__init__(1200, 1000)
        self.bg_menu = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/bg.png'), x = 0, y = 0)
        global player, seek
        music = pyglet.media.load('music/menu/1.mp3')
        player = pyglet.media.Player()
        seek = 0.0
        player.queue(music)
        player.volume = m_v
        player.loop = True
        player.play()
        pyglet.clock.schedule_interval(self.update, 1/60)
    def on_draw(self):
        global b_play, b_settings, b_exit, bg_menu, seek
        self.bg_menu.draw()
        b_play = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_play.png'), x=550, y = 800)
        b_play.draw()
        b_settings = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_Settings.png'), x = 550, y = 725)
        b_settings.draw()
        b_exit = pyglet.sprite.Sprite(pyglet.resource.image('img/menu/B_exit.png'), x = 550, y = 650)
        b_exit.draw()
    def update(self, dt):
        global seek
        if self.bg_menu.x == -1500:
            self.bg_menu.x = 0
        else:
            self.bg_menu.x -= 1
        seek = player.time
    def on_mouse_press(self, x, y, button, modifiers):
        global sett_m, seek, player, G_player
        if button == pyglet.window.mouse.LEFT and b_play.x <= x <= b_play.x + b_play.width \
        and b_play.y <= y <= b_play.y + b_play.height:
            M_s.set_visible(False)
            G_s.set_visible(True)
            player.pause()
            G_player.play()
        elif button == pyglet.window.mouse.LEFT and b_settings.x <= x <= b_settings.x + b_settings.width \
        and b_settings.y <= y <= b_settings.y + b_settings.height:
            sett_m = True
            M_s.set_visible(False)
            S_s.set_visible(True)
            player_s.play()
            player.pause()
            player_s.seek(seek)
            
        elif button == pyglet.window.mouse.LEFT and b_exit.x <= x <= b_exit.x + b_exit.width \
        and b_exit.y <= y <= b_exit.y + b_exit.height:
            pyglet.app.exit()
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
    def on_close(self):
        pyglet.app.exit()
M_s = menuscreen()
S_s = Settings()
G_s = GameScreen()
S_s.set_visible(False)
G_s.set_visible(False)
pyglet.app.run()