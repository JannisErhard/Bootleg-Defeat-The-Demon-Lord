from tkinter import *
import random
# left right is for canvas the second coordinate hile for map its the first, could transpose map but than ascii graphics would be flipped
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
    gamecanvas.create_line(left_up, right_up)
    gamecanvas.create_line(left_down, right_down)
    gamecanvas.create_line(left_up, left_down)
    gamecanvas.create_line(right_down, right_up)
    gamecanvas.create_line(left_half_up, right_half_up)
def draw_roof(x,y, gamecanvas):
    left_up =    [y-0,x-16]
    right_up =   [y+32,x-16]
    left_down =  [y-0,x+16]
    right_down = [y+32,x+16]
    gamecanvas.create_rectangle(left_down, right_up, fill='gray70')
def draw_grass(x,y, gamecanvas):
    left_up =    [y-0,x-16]
    right_up =   [y+32,x-16]
    left_down =  [y-0,x+16]
    right_down = [y+32,x+16]
    gamecanvas.create_rectangle(left_down, right_up, fill='green3',outline='green3')

def draw_on_canvas(current_map, gamecanvas):
    enemy_list = []
    i_x = 2
    i_y = 1
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
        draw_roof(i_x*32, (i_y+1)*32, gamecanvas)
# Draw Sprites
    i_x = 3
    for sublist in current_map:
        i_y = 1
        for tile  in sublist:
            if tile == 'E':
                print("stuff happens")
                enemy = enemy_sprite(i_x*32, i_y*32, gamecanvas)
                enemy_list.append([i_x-3,i_y-1,enemy])
                print(current_map[i_x-3][i_y-1])
            if tile in "^v<>":
                hero = hero_sprite(i_x*32,i_y*32, gamecanvas, i_x-3, i_y-1, tile)
            i_y = i_y + 1
        i_x = i_x+1
    return enemy_list, hero
