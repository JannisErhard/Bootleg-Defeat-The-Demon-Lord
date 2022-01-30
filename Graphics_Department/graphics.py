from tkinter import *
import random
from Graphics_Department.colors import grey
# left right is for canvas the second coordinate hile for map its the first, could transpose map but than ascii graphics would be flipped

greens = {}
greens = {
1: 'yellowgreen'\
,2: 'green4'\
,3: 'darkolivegreen3'\
,4: 'green4'\
,5: 'yellowgreen'\
}

def go_screen(gamecanvas):
    height = gamecanvas.winfo_height()
    width = gamecanvas.winfo_width()
    gamecanvas.create_line(0,width//4,width, height,fill='red', width=10)
    gamecanvas.create_line(0,height,width,width//4,fill='red', width=10)
    gamecanvas.create_oval(width//8*3, height//8*3+height//8, 5*width//8, 5*height//8+height//8,fill='red', outline='red')
    gamecanvas.create_oval(width//4, height//4-height//8, 3*width//4, 3*height//4-height//8,fill='red', outline='red')
    gamecanvas.create_oval(width//8*3, height//8*4-height//8, 4*width//8, 5*height//8-height//8,fill='black', outline='red')
    gamecanvas.create_oval(width//8*4, height//8*4-height//8, 5*width//8, 5*height//8-height//8,fill='black', outline='red')
class enemy_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        # body
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='grey60',outline='black')
        # head
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='lightsalmon',outline='black')
        #eye left
        self.lefteyeid = gamecanvas.create_line(center[0]-6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        #eye right
        self.righteyeid = gamecanvas.create_line(center[0]+6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        # nose
        self.noseid = gamecanvas.create_oval(center[0]-4, center[1]-8, center[0]+4, center[1], fill='salmon',outline='black')
    def die(self, gamecanvas):
        gamecanvas.delete(self.bodyid)
        gamecanvas.delete(self.headid)
        gamecanvas.delete(self.lefteyeid)
        gamecanvas.delete(self.righteyeid)
        gamecanvas.delete(self.noseid)

class Merchant_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='yellow',outline='orange')
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='tan',outline='black')
        self.lefteyeid = gamecanvas.create_line(center[0]-6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        self.righteyeid = gamecanvas.create_line(center[0]+6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        self.noseid = gamecanvas.create_oval(center[0]-4, center[1]-8, center[0]+4, center[1], fill='tan1',outline='black')
    def vanish(self, gamecanvas):
        gamecanvas.delete(self.bodyid)
        gamecanvas.delete(self.headid)
        gamecanvas.delete(self.lefteyeid)
        gamecanvas.delete(self.righteyeid)
        gamecanvas.delete(self.noseid)

class Sword_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        self.spriteid = {}
        # body arguments are left_border, up_border, right_border, down_border
        self.spriteid[1] = gamecanvas.create_line(center[0]+1, center[1]+11, center[0]+1, center[1]-12, fill='grey40', width = 2)
        self.spriteid[2] = gamecanvas.create_line(center[0]-1, center[1]+11, center[0]-1, center[1]-12, fill='grey40', width = 2)
        self.spriteid[3] = gamecanvas.create_line(center[0], center[1]+15, center[0], center[1]-15, fill='grey50', width = 2)
        self.spriteid[4] = gamecanvas.create_line(center[0]-3, center[1]+9, center[0]+3, center[1]+9, fill='brown', width = 2)
    def vanish(self, gamecanvas):
        for i in range(1,5):
            gamecanvas.delete(self.spriteid[i])

class Coin_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        self.frameid2 = gamecanvas.create_oval(center[0]-6, center[1]-4, center[0]+6, center[1]+8, fill='lightgoldenrod',outline='black')
        self.frameid = gamecanvas.create_oval(center[0]-6, center[1]-6, center[0]+6, center[1]+6, fill='gold',outline='black')
    def vanish(self, gamecanvas):
        gamecanvas.delete(self.frameid)
        gamecanvas.delete(self.frameid2)

class Potion_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        self.frameid1 = gamecanvas.create_oval(center[0]-8, center[1]+2, center[0]+8, center[1]+14, fill='mediumseagreen',outline='black')
        self.frameid2= gamecanvas.create_rectangle(center[0]-8, center[1]-6, center[0]+8, center[1]+6, fill='mediumseagreen',outline='lightskyblue')
        self.frameid3 = gamecanvas.create_oval(center[0]-8, center[1]-6, center[0]+8, center[1]+6, fill='lightblue',outline='black')
        self.frameid4 = gamecanvas.create_oval(center[0]-5, center[1]-7, center[0]+5, center[1]+3, fill='grey90',outline='black')
        self.frameid5 = gamecanvas.create_oval(center[0]-5, center[1]-9, center[0]+5, center[1]+1, fill='grey70',outline='black')
    def vanish(self, gamecanvas):
        gamecanvas.delete(self.frameid1)
        gamecanvas.delete(self.frameid2)
        gamecanvas.delete(self.frameid3)
        gamecanvas.delete(self.frameid4)
        gamecanvas.delete(self.frameid5)

class vertical_door_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        # body arguments are left_border, up_border, right_border, down_border
        self.frameid = gamecanvas.create_rectangle(center[0]-2, center[1]-32, center[0]+2, center[1]+16, fill='Orangered3',outline='black')
    def vanish(self, gamecanvas):
        gamecanvas.delete(self.frameid)

class horizontal_door_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        # body arguments are left_border, up_border, right_border, down_border
        self.topid = gamecanvas.create_rectangle(center[0]-16, center[1]-14, center[0]+16, center[1]-8, fill='Orangered3',outline='black')
        self.frameid = gamecanvas.create_rectangle(center[0]-16, center[1]-8, center[0]+16, center[1]+12, fill='Orangered4',outline='black')
    def vanish(self, gamecanvas):
        gamecanvas.delete(self.frameid)
        gamecanvas.delete(self.topid)

class Key_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        # body arguments are left_border, up_border, right_border, down_border
        self.frameid =  gamecanvas.create_oval(center[0]+8, center[1]-8, center[0]+14, center[1]-14, fill='yellow',outline='darkorange')

        self.stielid6 = gamecanvas.create_line(center[0]-6, center[1]+6-2, center[0]+8, center[1]-8 -2,  fill='orange', width = 2)
        self.stielid7 = gamecanvas.create_line(center[0]-6, center[1]+6-2, center[0]+3, center[1]+12-2,  fill='orange', width = 2)
        self.stielid8 = gamecanvas.create_line(center[0]-4, center[1]+4-2, center[0]+5, center[1]+10-2,  fill='orange', width = 2)
        self.stielid9 = gamecanvas.create_line(center[0]-2, center[1]+2-2, center[0]+7, center[1]+8 -2,  fill='orange', width = 2)

        self.stielid2 = gamecanvas.create_line(center[0]-6, center[1]+6, center[0]+8, center[1]-8,  fill='yellow', width = 2)
        self.stielid3 = gamecanvas.create_line(center[0]-6, center[1]+6, center[0]+3, center[1]+12, fill='yellow', width = 2)
        self.stielid4 = gamecanvas.create_line(center[0]-4, center[1]+4, center[0]+5, center[1]+10, fill='yellow', width = 2)
        self.stielid5 = gamecanvas.create_line(center[0]-2, center[1]+2, center[0]+7, center[1]+8,  fill='yellow', width = 2)

    def vanish(self, gamecanvas):
        gamecanvas.delete(self.frameid)
        gamecanvas.delete(self.stielid2)
        gamecanvas.delete(self.stielid3)
        gamecanvas.delete(self.stielid4)
        gamecanvas.delete(self.stielid5)
        gamecanvas.delete(self.stielid6)
        gamecanvas.delete(self.stielid7)
        gamecanvas.delete(self.stielid8)
        gamecanvas.delete(self.stielid9)



class Shield_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        # body arguments are left_border, up_border, right_border, down_border
        self.frameid = {}
        colors = {14 : 'grey10', 13 : 'grey20', 12 : 'grey30', 11 : 'grey40'}
        for var in range(14,10,-1):
            self.frameid[var] = gamecanvas.create_oval(center[0]-var, center[1]-var, center[0]+var, center[1]+var, fill=colors[var],outline=colors[var])
        var = 5
        self.frameid[10] = gamecanvas.create_oval(center[0]-var, center[1]-var, center[0]+var, center[1]+var, fill='grey30',outline='grey10')
    def vanish(self, gamecanvas):
        for var in range(14,9,-1):
            gamecanvas.delete(self.frameid[var])

class Boss_sprite:
    def __init__(self,x,y, gamecanvas):
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        # body
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='blue',outline='black')
        # head
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='red',outline='black')
        #eye left
        self.lefteyeid = gamecanvas.create_line(center[0]-6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        #eye right
        self.righteyeid = gamecanvas.create_line(center[0]+6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        # nose
        self.noseid = gamecanvas.create_oval(center[0]-4, center[1]-8, center[0]+4, center[1], fill='salmon',outline='black')
    def vanish(self, gamecanvas):
        gamecanvas.delete(self.bodyid)
        gamecanvas.delete(self.headid)
        gamecanvas.delete(self.lefteyeid)
        gamecanvas.delete(self.righteyeid)
        gamecanvas.delete(self.noseid)

class hero_sprite:
    def __init__(self,x,y, gamecanvas, board_x, board_y, orientation):
        self.board_x = board_x
        self.board_y = board_y
        self.canvas_coord = [x,y]
        self.orientation = orientation
        left_up =    [y-0,x-16]
        right_up =   [y+32,x-16]
        left_down =  [y-0,x+16]
        right_down = [y+32,x+16]
        center = [y+16, x]
        print(x,y,orientation)
        if orientation == '^':
            self.face_up(center, gamecanvas)
        if orientation == 'v':
            self.face_down(center, gamecanvas)
        if orientation == '<':
            self.face_left(center, gamecanvas)
        if orientation == '>':
            self.face_right(center, gamecanvas)
    def update(self, x, y , gamecanvas, orientation):
        center = [y+16, x]
        gamecanvas.delete(self.bodyid, self.headid)
        if hasattr(self, 'lefteyeid'):
            gamecanvas.delete(self.lefteyeid)
        if hasattr(self, 'righteyeid'):
            gamecanvas.delete(self.righteyeid)
        if hasattr(self, 'noseid'):
            gamecanvas.delete(self.noseid)
        if orientation == '^':
            self.face_up(center, gamecanvas)
        if orientation == 'v':
            self.face_down(center, gamecanvas)
        if orientation == '<':
            self.face_left(center, gamecanvas)
        if orientation == '>':
            self.face_right(center, gamecanvas)

    #def move():
    #def turn():
    def face_left(self, center, gamecanvas):
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='grey60',outline='black')
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='tan',outline='black')
        self.righteyeid = gamecanvas.create_line(center[0]-6, center[1]-5, center[0], center[1]-11, fill = 'black', width = 2)
        self.noseid = gamecanvas.create_rectangle(center[0]-5, center[1]-4, center[0]-8, center[1], fill='tan3',outline='black')
    def face_right(self, center, gamecanvas):
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='grey60',outline='black')
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='tan',outline='black')
        self.lefteyeid = gamecanvas.create_line(center[0], center[1]-11, center[0]+6, center[1]-5, fill = 'black', width = 2)
        self.noseid = gamecanvas.create_rectangle(center[0]+5, center[1]-4, center[0]+8, center[1], fill='tan3',outline='black')
    def face_up(self, center, gamecanvas):
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='grey60',outline='black')
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='tan',outline='black')
    def face_down(self, center, gamecanvas):
        self.bodyid = gamecanvas.create_rectangle(center[0]-7, center[1]-8, center[0]+7, center[1]+8, fill='grey60',outline='black')
        self.headid = gamecanvas.create_oval(center[0]-8, center[1]-14, center[0]+8, center[1]+2, fill='tan',outline='black')
        self.lefteyeid = gamecanvas.create_line(center[0]-6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        self.righteyeid = gamecanvas.create_line(center[0]+6, center[1]-11, center[0], center[1]-5, fill = 'black', width = 2)
        self.noseid = gamecanvas.create_rectangle(center[0]-2, center[1]-4, center[0]+2, center[1], fill='tan1',outline='black')
    def face_down_experimental(self, center, gamecanvas):  # top coordinate in gimp is first coordinate in here
        top_corner = [0]*2
        top_corner[0], top_corner[1] = center[0]-16, center[1]-16
        self.headid = gamecanvas.create_rectangle(top_corner[0], top_corner[1],top_corner[0]+32, top_corner[1]+32, fill = 'white')
        self.bodyid = gamecanvas.create_rectangle(top_corner[0]+8, top_corner[1]+8,top_corner[0]+24, top_corner[1]+21, fill = 'white')
        self.bodyid = gamecanvas.create_rectangle(top_corner[0]+12, top_corner[1]+1,top_corner[0]+20, top_corner[1]+9, fill = 'white')
        self.legsid = gamecanvas.create_rectangle(top_corner[0]+12, top_corner[1]+21,top_corner[0]+20, top_corner[1]+30, fill = 'white')

def draw_wall(x,y, gamecanvas):
    left_up =    [y-0,x-16]
    right_up =   [y+32,x-16]
    left_half_up =    [y-0,x-2]
    right_half_up =   [y+32,x-2]
    left_down =  [y-0,x+16]
    right_down = [y+32,x+16]
    left_center =  [y-0,x]
    left_inter_sec_2 =  [y-0,x+6]
    left_inter_sec_3 =  [y-0,x+9]
    right_center =  [y+32,x]
    right_inter_sec_2 =   [y+32,x+6]
    right_inter_sec_3 =   [y+32,x+9]

    gamecanvas.create_rectangle(left_half_up, right_up, fill='gray70', outline='gray70')
    gamecanvas.create_rectangle(left_down, right_inter_sec_3, fill='gray40', outline='gray40')
    gamecanvas.create_rectangle(left_inter_sec_3, right_center, fill='gray50', outline='gray50')
    gamecanvas.create_rectangle(left_center, right_half_up, fill='gray60', outline='gray60')
    # row 1 
    gamecanvas.create_line(y+0,x+15,y+32,x+15,fill=grey[20-18])
    gamecanvas.create_line(y+0,x+14,y+32,x+14,fill=grey[50-17])
    gamecanvas.create_line(y+0,x+13,y+32,x+13,fill=grey[60-16])
    gamecanvas.create_line(y+0,x+12,y+32,x+12,fill=grey[60-15])
    gamecanvas.create_line(y+0,x+11,y+32,x+11,fill=grey[60-14])
    gamecanvas.create_line(y+0,x+10,y+32,x+10,fill=grey[80-13])
    # row 2
    gamecanvas.create_line(y+0,x+9, y+32, x+9,fill=grey[20-12])
    gamecanvas.create_line(y+0,x+8, y+32, x+8,fill=grey[50-11])
    gamecanvas.create_line(y+0,x+7, y+32 ,x+7,fill=grey[60-10])
    gamecanvas.create_line(y+0,x+6, y+32 ,x+6,fill=grey[60-9])
    gamecanvas.create_line(y+0,x+5, y+32 ,x+5,fill=grey[60-8])
    gamecanvas.create_line(y+0,x+4, y+32 ,x+4,fill=grey[80-7])
    # row 3
    gamecanvas.create_line(y+0,x+3, y+32, x+3,fill=grey[20+20-6])
    gamecanvas.create_line(y+0,x+2, y+32, x+2,fill=grey[50+20-5])
    gamecanvas.create_line(y+0,x+1, y+32 ,x+1,fill=grey[60+20-4])
    gamecanvas.create_line(y+0,x+0, y+32 ,x+0,fill=grey[60+20-3])
    gamecanvas.create_line(y+0,x-1, y+32 ,x-1,fill=grey[60+20-2])
    gamecanvas.create_line(y+0,x-2, y+32 ,x-2,fill=grey[80+20-1])
    #middle column
    gamecanvas.create_line(y+16,x+2,y+16 ,x-2,fill=grey[20])
    gamecanvas.create_line(y+17,x+2,y+17 ,x-2,fill=grey[50])
    gamecanvas.create_line(y+18,x+2,y+18 ,x-2,fill=grey[70])
    #left column
    gamecanvas.create_line(y+5,x+4,y+5 ,x+9,fill=grey[20])
    gamecanvas.create_line(y+6,x+4,y+6 ,x+9,fill=grey[50])
    gamecanvas.create_line(y+7,x+4,y+7 ,x+9,fill=grey[70])
    #right column
    gamecanvas.create_line(y+20,x+4,y+20 ,x+9,fill=grey[20])
    gamecanvas.create_line(y+21,x+4,y+21 ,x+9,fill=grey[50])
    gamecanvas.create_line(y+22,x+4,y+22 ,x+9,fill=grey[70])
    #middle column
    gamecanvas.create_line(y+16,x+10,y+16 ,x+15,fill=grey[20])
    gamecanvas.create_line(y+17,x+10,y+17 ,x+15,fill=grey[50])
    gamecanvas.create_line(y+18,x+10,y+18 ,x+15,fill=grey[70])
    #middle column
    gamecanvas.create_line(y+8,x+10,y+8 ,x+15,fill=grey[20])
    gamecanvas.create_line(y+9,x+10,y+9 ,x+15,fill=grey[50])
    gamecanvas.create_line(y+10,x+10,y+10 ,x+15,fill=grey[70])

def draw_roof(x,y, gamecanvas):
    left_up =    [y-0,x-16]
    right_up =   [y+32,x-16]
    left_down =  [y-0,x+16]
    right_down = [y+32,x+16]
    gamecanvas.create_rectangle(left_down, right_up, fill='gray70', outline='gray70')
    #gamecanvas.create_line(left_up, right_up, fill='black')
def draw_head_roof(x,y, gamecanvas):
    left_up =    [y-0,x-16]
    right_up =   [y+32,x-16]
    left_down =  [y-0,x+16]
    right_down = [y+32,x+16]
    gamecanvas.create_rectangle(left_down, right_up, fill='gray70', outline='gray70')
    gamecanvas.create_line(left_up, right_up, fill='grey80')
    gamecanvas.create_line(left_up[0],left_up[1]+0, right_up[0], right_up[1]+0, fill=grey[20])
    gamecanvas.create_line(left_up[0],left_up[1]+1, right_up[0], right_up[1]+1, fill=grey[30])
    gamecanvas.create_line(left_up[0],left_up[1]+2, right_up[0], right_up[1]+2, fill=grey[40])
    gamecanvas.create_line(left_up[0],left_up[1]+3, right_up[0], right_up[1]+3, fill=grey[50])
    gamecanvas.create_line(left_up[0],left_up[1]+4, right_up[0], right_up[1]+4, fill=grey[60])
    gamecanvas.create_line(left_up[0],left_up[1]+5, right_up[0], right_up[1]+5, fill=grey[65])
def draw_grass(x,y, gamecanvas):
    left_up =    [y-0,x-16]
    right_up =   [y+32,x-16]
    left_down =  [y-0,x+16]
    right_down = [y+32,x+16]
    for i in range(-16,16):
        for j in range(0,32):
            gamecanvas.create_line(y+j, x+i, y+j+2, x+i, fill=greens[random.randint(1,5)])
    #gamecanvas.create_rectangle(left_down, right_up, fill='green3',outline='green3')

def draw_on_canvas(current_map, gamecanvas):
    enemy_list = []
    disposable_objects_list = []
    i_x = 2
    draw_roof(i_x*32, 0, gamecanvas)
    draw_roof(i_x*32, (len(current_map[0])+1)*32, gamecanvas)
    for i_y in range(len(current_map[0])):
        if current_map[0][i_y] != '#':
            draw_wall(i_x*32, (i_y+1)*32, gamecanvas)
        else:
            draw_roof(i_x*32, (i_y+1)*32, gamecanvas)
    i_x = 3
    for sublist in current_map:
        i_y = 1
        for tile  in sublist:
            if not i_x-3+1 < len(current_map):
                if tile == '#':
                    draw_roof(i_x*32, i_y*32, gamecanvas)
                else:
                    draw_grass(i_x*32, i_y*32, gamecanvas)
            else:
                if tile == '#' and not current_map[i_x-3+1][i_y-1] == '#':
                    draw_wall(i_x*32, i_y*32, gamecanvas)
                elif tile == '#' and current_map[i_x-3+1][i_y-1] == '#':
                    draw_roof(i_x*32, i_y*32, gamecanvas)
                else: 
                    draw_grass(i_x*32, i_y*32, gamecanvas)
            i_y = i_y + 1
        draw_roof(i_x*32, 0, gamecanvas)
        draw_roof(i_x*32, (len(sublist)+1)*32, gamecanvas)
        i_x = i_x+1
    for i_y in range(len(current_map[0])):
        if not current_map[-1][i_y] == '#':
            draw_head_roof(i_x*32, (i_y+1)*32, gamecanvas)
        else:
            draw_roof(i_x*32, (i_y+1)*32, gamecanvas)
    draw_roof(i_x*32, 0, gamecanvas)
    draw_roof(i_x*32, (len(current_map[0])+1)*32, gamecanvas)
# Draw Sprites
    i_x = 3
    for sublist in current_map:
        i_y = 1
        for tile  in sublist:
            if tile == 'E':
                enemy = enemy_sprite(i_x*32, i_y*32, gamecanvas)
                enemy_list.append([i_x-3,i_y-1,enemy])
            if tile in "^v<>":
                hero = hero_sprite(i_x*32,i_y*32, gamecanvas, i_x-3, i_y-1, tile)
            if tile == "|":
                door = vertical_door_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, '|', door])
            if tile == "-":
                door = horizontal_door_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, '-', door])
            if tile == "D":
                Boss = Boss_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'D', Boss])
            if tile == "M":
                Merchant = Merchant_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'M', Merchant])
            if tile == "S":
                Shield = Shield_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'S', Shield])
            if tile == "C":
                Coin = Coin_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'C', Coin])
            if tile == "H":
                Potion = Potion_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'H', Potion])
            if tile == "K":
                Key = Key_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'K', Key])
            if tile == "X":
                Sword = Sword_sprite(i_x*32, i_y*32, gamecanvas)
                disposable_objects_list.append([i_x-3, i_y-1, 'X', Sword])
            i_y = i_y + 1
        i_x = i_x+1
    return enemy_list, hero, disposable_objects_list
