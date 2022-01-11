#!/usr/bin/env python3
from Graphics_Department.graphics import draw_on_canvas
from Graphics_Department.graphics import go_screen
from World.maps import *
from Statemachine.statemachine import rpg

def unbind_all():
    root.unbind('<Up>')
    root.unbind('<Left>')
    root.unbind('<Down>')
    root.unbind('<Right>')
    root.unbind('<space>')
    root.unbind('k')
    root.unbind('h')
    root.unbind('c')
    root.unbind('a')

import tkinter as tk
global first_map, HP, attk, defn, bag, HP_Demon_Lord, debug, msg, stage, max_level
global map_width, extended_map_height
global legacy
map_width , extended_map_height = int(), int()
attk, defn, HP, exp, HP_Demon_Lord   = 1, 1, 3, 0, 10
msg = "Game Start"

bag = []
receipts_and_deleted_tweets = []
stage = 1
max_level = 4



first_map = campaign[1]

for sublist in first_map:
    y_len = len(sublist)
    receipts_and_deleted_tweets.append(y_len*[0])

def map_to_screen(map):
    global bag, HP, attk, defn, exp, msg, HP_Demon_Lord, debug
    UIText = []
    style = 'style_2'
    global map_width, extended_map_height
    if debug: print("style is updated:", style == 'style_2')
    
    if HP <= 0:
        translator = []
        translator.append("♥:"+str(HP)+" †:"+str(attk)+' ♦:'+str(defn)+' EX:'+str(exp))
        translator.append("Bag: "+str(bag))
        translator.append("              ")
        UIText[:] = translator[:]
        for i in map:
            substring = str()
            for j in i:
                substring += '▓'
            translator.append(substring)
        translator.append("Game Over")
        unbind_all()
    else:
        if debug: print("♥:",HP," †:", attk, ' ♦:', defn, 'EX:', exp)
        len_y = 0
        len_x = 0
        substring = str()
        translator = []
        translator.append("♥:"+str(HP)+" †:"+str(attk)+' ♦:'+str(defn)+' EX:'+str(exp))
        translator.append("Bag: "+str(bag))
        translator.append("              ")
        UIText[:] = translator[:]
        len_y = len(map[0])
        if style == 'style_1':
            substring=(len_y+2)*'#'
        if style == 'style_2':
            substring = ''
            substring += '╔'
            substring += '═'*len_y
            substring += '╗'
        translator.append(substring)
        for i in map:
            len_x += 1
            substring = str()
            if style == 'style_1':
                substring += '#'
            if style == 'style_2':
                substring += '║'
            for j in i:
                substring += j
            if style == 'style_2':
                substring = substring.replace('#','╬')
                substring = substring.replace('E','☺')
                substring = substring.replace('D','☻')
            if style == 'style_1':
                substring += '#'
            if style == 'style_2':
                substring += '║'
            translator.append(substring)
        if style == 'style_1':
            substring=(len_y+2)*'#'
        if style == 'style_2':
            substring = ''
            substring += '╚'
            substring += '═'*len_y
            substring += '╝'
        translator.append(substring)
        translator.append(msg)

        map_width = (len_y+2)*32
        extended_map_height = (len_x+4)*32
    Frame = "\n".join(translator)
    return Frame, "\n".join(UIText)
def check_stage_progression():
    global HP_Demon_Lord, debug, stage, first_map, attk , HP, defn, max_level, msg
    global  hero, enemy_list, disposable_objects_list
    if HP_Demon_Lord <= 0:
        HP_Demon_Lord = 10
        stage += 1
        if stage > max_level: 
            unbind_all()
            msg = ''
            first_map = campaign['win']
        else: 
            msg = 'Level '+str(stage)
            first_map = campaign[stage]
            gamecanvas.delete("all")
            gamecanvas.configure(width=32*(len(first_map[0])+2))
            gamecanvas.configure(height=32*(len(first_map)+4))
            del hero
            enemy_list = []
            disposable_objects_list = []
            enemy_list, hero, disposable_objects_list = draw_on_canvas(first_map, gamecanvas)
            attk = 1
            defn = 1
            HP = 3

def show_game_over_screen():
    gamecanvas.delete("all")
    go_screen(gamecanvas)

def update_all_objects(enemy_list, current_map):
    global hero, disposable_objects
    for sublist in enemy_list:
        if current_map[sublist[0]][sublist[1]] != 'E':
            print(sublist[0], sublist[1], "is dead and",current_map[sublist[0]][sublist[1]])
            sublist[2].die(gamecanvas)
            enemy_list.remove(sublist)


    for sublist in disposable_objects_list:
        if current_map[sublist[0]][sublist[1]] != sublist[2]:
            sublist[3].vanish(gamecanvas)
            disposable_objects_list.remove(sublist)

    i_x = 3
    for sublist in current_map:
        i_y = 1
        for tile in sublist:
            if tile in "^v<>":
                hero.update(i_x*32,i_y*32,gamecanvas,tile)
            i_y += 1
        i_x += 1


def game_action(command):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list 
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, command ,attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    if HP > 0:
        update_all_objects(enemy_list, first_map)
    else:
        show_game_over_screen()
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)

def turn_up_input(self):
    game_action('^')
def turn_left_input(self):
    game_action('<')
def turn_right_input(self):
    game_action('>')
def turn_down_input(self):
    game_action('v')
def Move(self):
    game_action('F')
def Use_Key(self):
    game_action('K')
def Attack(self):
    game_action('A')
def Use_Potion(self):
    game_action('H')
def Use_Coin(self):
    game_action('C')

debug = False
legacy = False
Frame, UIText = map_to_screen(first_map)
root = tk.Tk()
root.wm_title("Bootleg Defeat The Demon Lord")
if legacy: gamewindow = tk.Label(root, text=Frame, font = ('Courier new', 26))
UI_of_Canvas = tk.Label(root, text=UIText, font = ('Courier new', 26))
gamecanvas = tk.Canvas(root, width=map_width, height=extended_map_height, bg='black')
global hero, disposable_objects_list
enemy_list, hero, disposable_objects_list = draw_on_canvas(first_map, gamecanvas)
root.bind('<Up>',turn_up_input)
root.bind('<Left>',turn_left_input)
root.bind('<Down>',turn_down_input)
root.bind('<Right>',turn_right_input)
root.bind('<space>',Move)
root.bind('k',Use_Key)
root.bind('h',Use_Potion)
root.bind('c',Use_Coin)
root.bind('a',Attack)
if legacy: 
    gamewindow.grid(row=0, column=0)
else:
    UI_of_Canvas.grid(row=0, column=1)
    gamecanvas.grid(row=1, column=1)
tk.mainloop()


