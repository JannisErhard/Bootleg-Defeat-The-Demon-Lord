#!/usr/bin/env python3
from Graphics_Department.graphics import draw_on_canvas
import numpy as np
def rpg(field,  actions, attk, vert, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug): 
    HIT_BOX='^v<>HAKC'
    Flavor_Text_1="The Demon Lord bends you over and gives you a good spanking for:"
    Flavor_Text_2="One of the Demon Lord lackys scratches you for:"
    if debug: print(field)
    
    np_field  = np.asarray(field)
    if np.isin('^', np_field):
        player_x, player_y = map(int, np.where(np_field == '^'))
        if debug: print("initial position is:", player_x, player_y, '^')
    elif np.isin('v', np_field):
        player_x, player_y = map(int, np.where(np_field == 'v'))
        if debug: print("initial position is:", player_x, player_y, 'v')
    elif np.isin('<', np_field):
        player_x, player_y = map(int, np.where(np_field == '<'))
        if debug: print("initial position is:", player_x, player_y, '<')
    elif np.isin('>', np_field):
        player_x, player_y = map(int, np.where(np_field == '>'))
        if debug: print("initial position is:", player_x, player_y, '>')
    else:
        if debug: print("No player no cry")
        return None
    if debug: print(actions)
    map_back = []
    x_len = 0
    y_len = 0 
    for sublist in field:
        y_len = len(sublist)
        x_len += 1
    for i in actions:
        if HP <= 0:
            break
        if i in 'KCH':
            if i not in bag:
                pass
            else:
                if i == 'H':
                   HP = 3
                   bag.remove('H')
                if i == 'K':
                    if debug: print("I use Key!")
                    key_success = False
                    if player_x-1 >= 0:
                        if np_field[player_x-1, player_y] == '-':
                            bag.remove('K')
                            np_field[player_x-1, player_y]  = ' '
                            key_success = True
                    if player_x+1 < x_len:
                        if np_field[player_x+1, player_y] == '-':
                            bag.remove('K')
                            np_field[player_x+1, player_y]  = ' '
                            key_success = True
                    if player_y+1 < y_len:
                        if np_field[player_x, player_y+1] == '|':
                            bag.remove('K')
                            np_field[player_x, player_y+1]  = ' '
                            key_success = True
                    if player_y-1 >= 0:
                        if np_field[player_x, player_y-1] == '|':
                            bag.remove('K')
                            np_field[player_x, player_y-1]  = ' '
                            key_success = True
                    if not key_success:
                        pass 
                if i == 'C':#TODO: unlock doors left right down, unclear: nec. 2 face door ?
                    if debug: print("I use Coin!")
                    commerce_success = False
                    if player_y-1 >= 0:
                        if np_field[player_x, player_y-1] == 'M':
                            bag.remove('C')
                            receipts_and_deleted_tweets[player_x][player_y-1] += 1
                            if receipts_and_deleted_tweets[player_x][player_y-1] == 3:
                                np_field[player_x, player_y-1]  = ' '
                            commerce_success = True
                    if player_y+1 < y_len:
                        if np_field[player_x, player_y+1] == 'M':
                            bag.remove('C')
                            receipts_and_deleted_tweets[player_x][player_y+1] += 1
                            if receipts_and_deleted_tweets[player_x][player_y+1] == 3:
                                np_field[player_x, player_y+1]  = ' '
                            commerce_success = True
                    if player_x+1 < x_len:
                        if np_field[player_x+1, player_y] == 'M':
                            bag.remove('C')
                            receipts_and_deleted_tweets[player_x+1][player_y] += 1
                            if receipts_and_deleted_tweets[player_x+1][player_y] == 3:
                                np_field[player_x+1, player_y]  = ' '
                            commerce_success = True
                    if player_x-1 >= 0:
                        if np_field[player_x-1, player_y] == 'M':
                            bag.remove('C')
                            receipts_and_deleted_tweets[player_x-1][player_y] += 1
                            if receipts_and_deleted_tweets[player_x-1][player_y] == 3:
                                np_field[player_x-1, player_y]  = ' '
                            commerce_success = True
                    if not commerce_success:
                        #if debug: print("I dropped coin, that  incident kiled me...") 
                        #return None
                        break
        if i == 'A':
            if debug: print("I attack")
            if np_field[player_x,player_y] == '>':
                if debug: print("I strike to the right")
                if  np_field[player_x,player_y+1] == 'E':
                    if debug: print("Target is hit")
                    exp += 1
                    np_field[player_x, player_y+1] = ' '
                elif  np_field[player_x,player_y+1] == 'D':
                    if debug: print("Demon Lord is hit")
                    HP_Demon_Lord -= attk
                    if HP_Demon_Lord <= 0:
                        np_field[player_x, player_y+1] = ' '
                else:
                    if debug: print("I hit nothing ...")
                    break
            if np_field[player_x,player_y] == '^':
                if debug: print("I strike up")
                if  np_field[player_x-1,player_y] == 'E':
                    if debug: print("Target is hit")
                    exp += 1
                    np_field[player_x-1, player_y] = ' '
                elif  np_field[player_x-1,player_y] == 'D':
                    if debug: print("Demon Lord is hit")
                    HP_Demon_Lord -= attk
                    if HP_Demon_Lord <= 0:
                        np_field[player_x-1, player_y] = ' '
                else:
                    if debug: print("I hit nothing ...")
                    break
                    return None
            if np_field[player_x,player_y] == 'v':
                if debug: print("I strike down")
                if  np_field[player_x+1,player_y] == 'E':
                    if debug: print("Target is hit")
                    exp += 1
                    np_field[player_x+1, player_y] = ' '
                elif  np_field[player_x+1,player_y] == 'D':
                    if debug: print("Demon Lord is hit")
                    HP_Demon_Lord -= attk
                    if HP_Demon_Lord <= 0:
                        np_field[player_x+1, player_y] = ' '
                else:
                    #return None
                    if debug: print("I hit nothing ...")
                    break
            if np_field[player_x,player_y] == '<':
                if debug: print("I strike to the left")
                if  np_field[player_x,player_y-1] == 'E':
                    if debug: print("Target is hit")
                    exp += 1
                    np_field[player_x, player_y-1] = ' '
                elif  np_field[player_x,player_y-1] == 'D':
                    if debug: print("Demon Lord is hit")
                    HP_Demon_Lord -= attk
                    if HP_Demon_Lord <= 0:
                        np_field[player_x, player_y-1] = ' '
                else:
                    #return None
                    if debug: print("I hit nothing ...")
                    break
            if exp == 3:
                attk += 1
                exp = 0
        if i in '<>^v':
            if debug: print("I turnet to:", i)
            np_field[np.where(np_field == "^")]=str(i)
            np_field[np.where(np_field == "<")]=str(i)
            np_field[np.where(np_field == ">")]=str(i)
            np_field[np.where(np_field == "v")]=str(i)
        if i == 'F':
            if debug: print("I move facing ", np_field[player_x,player_y])
            if np.isin('^', np_field):
                player_x, player_y = map(int, np.where(np_field == '^'))
                player_x -= 1
                if not player_x < 0 and not str(np_field[player_x,player_y]) in '#ED-M':
                    if str(np_field[player_x,player_y]) in 'KCH':
                        if debug: print("I find", np_field[player_x,player_y])
                        bag.append(str(np_field[player_x,player_y]))
                    if str(np_field[player_x,player_y]) in 'S':
                        if debug: print("I find shield!")
                        vert += 1
                    if str(np_field[player_x,player_y]) in 'X':
                        if debug: print("I find STEROIDS!")
                        attk += 1
                    np_field[player_x+1, player_y] = ' '
                    np_field[player_x, player_y] = '^'
                else:
                    player_x += 1
            if np.isin('v', np_field):
                player_x, player_y = map(int, np.where(np_field == 'v'))
                player_x += 1
                if not player_x == x_len and not  str(np_field[player_x,player_y]) in '#ED-M':
                    if str(np_field[player_x,player_y]) in 'KCH':
                        if debug: print("I find", np_field[player_x,player_y])
                        bag.append(str(np_field[player_x,player_y]))
                    if str(np_field[player_x,player_y]) in 'S':
                        if debug: print("I find shield!")
                        vert += 1
                    if str(np_field[player_x,player_y]) in 'X':
                        if debug: print("I find STEROIDS!")
                        attk += 1
                    np_field[player_x-1, player_y] = ' '
                    np_field[player_x, player_y] = 'v'
                else:
                    player_x -= 1
            if np.isin('<', np_field):
                player_x, player_y = map(int, np.where(np_field == '<'))
                player_y -= 1
                if not player_y < 0 and not str(np_field[player_x,player_y]) in '#ED|M':
                    if str(np_field[player_x,player_y]) in 'KCH':
                        if debug: print("I find", np_field[player_x,player_y])
                        bag.append(str(np_field[player_x,player_y]))
                    if str(np_field[player_x,player_y]) in 'S':
                        if debug: print("I find shield!")
                        vert += 1
                    if str(np_field[player_x,player_y]) in 'X':
                        if debug: print("I find STEROIDS!")
                        attk += 1
                    np_field[player_x, player_y+1] = ' '
                    np_field[player_x, player_y] = '<'
                else:
                    player_y += 1
            if np.isin('>', np_field):
                player_x, player_y = map(int, np.where(np_field == '>'))
                player_y += 1
                if not player_y >= y_len: 
                    if not str(np_field[player_x,player_y]) in '#ED|M':
                        if str(np_field[player_x,player_y]) in 'KCH':
                            if debug: print("I find", np_field[player_x,player_y])
                            bag.append(str(np_field[player_x,player_y]))
                        if str(np_field[player_x,player_y]) in 'S':
                            if debug: print("I find shield!")
                            vert += 1
                        if str(np_field[player_x,player_y]) in 'X':
                            if debug: print("I find STEROIDS!")
                            attk += 1
                        np_field[player_x, player_y-1] = ' '
                        np_field[player_x, player_y] = '>'
                    else :
                        player_y -= 1
                else: 
                    player_y -= 1
        if player_x-1 >= 0: 
            if np_field[player_x-1,player_y] == 'D':
                if i in HIT_BOX:
                    if debug: print("The Demon Lord bends you over and gives you a good spanking for", max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
            if np_field[player_x-1,player_y] == 'E':
                if i in HIT_BOX:
                    if debug: print("One of the Demon Lord lackys scratches you for", max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                else:
                    if debug: print("Player avoids the attack.")
        if player_x-2 >= 0: 
            if np_field[player_x-2,player_y] == 'D':
                if i == "F" and np_field[player_x,player_y] == 'v':
                    if debug: print("The Demon Lord bends you over and gives you a good spanking for", max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
            if np_field[player_x-2,player_y] == 'E':
                if i == "F" and np_field[player_x,player_y] == 'v':
                    if debug: print("One of the Demon Lord lackys scratches you for", max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                else:
                    if debug: print("Player avoids the attack.")
        if player_x+1 < x_len:
            if np_field[player_x+1,player_y] == 'D':
                if i in HIT_BOX:
                    if debug: print("The Demon Lord bends you over and gives you a good spanking for", max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
            if np_field[player_x+1,player_y] == 'E':
                if i in HIT_BOX:
                    if debug: print("One of the Demon Lord lackys scratches you for", max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                else:
                    if debug: print("Player avoids the attack.")
        if player_x+2 < x_len:
            if np_field[player_x+2,player_y] == 'D':
                if i == "F" and np_field[player_x,player_y] == '^':
                    if debug: print("The Demon Lord bends you over and gives you a good spanking for", max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
            if np_field[player_x+2,player_y] == 'E':
                if i == "F" and np_field[player_x,player_y] == '^':
                    if debug: print("One of the Demon Lord lackys scratches you for", max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                else:
                    if debug: print("Player avoids the attack.")
        if player_y-1 >= 0:
            if np_field[player_x,player_y-1] == 'D':
                if i in HIT_BOX:
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
            if np_field[player_x,player_y-1] == 'E':
                if i in HIT_BOX:
                    if debug: print("One of the Demon Lord lackys scratches you for", max(0,(2-vert)))
                    HP -= max(0,(2-vert))
        if player_y-2 >= 0:
            if np_field[player_x,player_y-2] == 'D':
                if i == "F" and np_field[player_x,player_y] == '>':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
            if np_field[player_x,player_y-2] == 'E':
                if i == "F" and np_field[player_x,player_y] == '>':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                else:
                    if debug: print("Player avoids the attack.")
        if player_y+1 < y_len:
            if np_field[player_x,player_y+1] == 'D':
                if i in HIT_BOX:
                    if debug: print("The Demon Lord bends you over and gives you a good spanking for", max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
            if np_field[player_x,player_y+1] == 'E':
                if i in HIT_BOX:
                    if debug: print("One of the Demon Lord lackys scratches you for", max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                else:
                    if debug: print("Player avoids the attack.")
        if player_y+2 < y_len:
            if np_field[player_x,player_y+2] == 'E':
                if i == 'F' and np_field[player_x, player_y] == '<':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[player_x,player_y+2] == 'D':
                if i == 'F' and np_field[player_x, player_y] == '<':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                else:
                    if debug: print("Player avoids the attack.")
        to_check_y, to_check_x = player_y+1, player_x+1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] == '<':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                elif i == 'F' and np_field[player_x, player_y] == '^':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] == '<':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                elif i == 'F' and np_field[player_x, player_y] == '^':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
        to_check_x, to_check_y = player_x-1, player_y-1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] == '>':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                elif i == 'F' and np_field[player_x, player_y] == 'v':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] == '>':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                elif i == 'F' and np_field[player_x, player_y] == 'v':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
        to_check_x, to_check_y = player_x+1, player_y-1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] == '>':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                elif i == 'F' and np_field[player_x, player_y] == '^':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] == '>':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                if i == 'F' and np_field[player_x, player_y] == '^':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
        to_check_y, to_check_x = player_y+1, player_x-1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] == '<':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
                elif i == 'F' and np_field[player_x, player_y] == 'v':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] == '<':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
                if i == 'F' and np_field[player_x, player_y] == 'v':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
    for i in range(0,x_len):
        sublist =[np_field[:][i]]
        map_back.append(list(np_field[:][i]))
    bag.sort()
    return map_back, attk, vert, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord

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

campaign = {}

campaign[3] = [
            list('SX#  EDE '),
            list('  # EEEEE'),
            list('#-#     X'),
            list('         '),
            list('^       K'),
        ]
campaign[1] = [['K', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 'X', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', 'S', '#', ' ', ' ', 'D', ' ', ' '], [' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', 'E', ' ', 'E', ' '], ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '-', '#', '#'], [' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', 'E', '#', '#', 'E', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', 'K', '#', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '#', '#', 'E', '#', '#', 'E', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ']]
campaign[2] = [
['S',' ',' ',' ',' ',' ',' ','#',' '],
[' ',' ','#','#','#','#',' ','|','D'],
[' ',' ','E',' ',' ','#',' ','#',' '],
['#','#','#','#','E','#',' ','#','#'],
[' ',' ',' ',' ',' ','#',' ','E',' '],
['^',' ','E',' ',' ','E','K','E','X']]
campaign[4] = [
['E',' ', 'E', ' ', 'E', 'E', 'E', ' ', 'E', ' ', ' ', 'E', ' ', '^', ' ', 'E', 'E', 'E'],
['E',' ', 'E', ' ', 'E', ' ', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', ' ', 'E'],
['E','E', 'E', ' ', 'E', 'E', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', 'D', 'E'],
['E',' ', 'E', ' ', 'E', ' ', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', ' ', 'E'],
['E',' ', 'E', ' ', 'E', 'E', 'E', ' ', 'E', 'E', ' ', 'E', 'E', ' ', ' ', 'E', 'E', 'E']]
campaign['win'] = [
list('You Win'+' '*(len('Thanks for playing!')-7)),
list('Game Over'+' '*(len('Thanks for playing!')-9)),
list(' '*len('Thanks for playing!')),
list('Thanks for playing!')
        ]


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
        extended_map_height = (len_x+2+3)*32
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



def turn_up_input(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list 
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, '^',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)
def turn_left_input(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, '<',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if debug: print(Frame)
    if legacy: gamewindow.configure(text=Frame)
def turn_right_input(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, '>',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if debug: print(Frame)
    if legacy: gamewindow.configure(text=Frame)
def turn_down_input(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, 'v',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)
def Move(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, 'F',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)
def Use_Key(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, 'K',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)
def Attack(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, 'A',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)
def Use_Potion(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets  , HP_Demon_Lord= rpg(first_map, 'H',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)
def Use_Coin(self):
    global first_map, HP, attk, defn, bag, exp, receipts_and_deleted_tweets, HP_Demon_Lord, debug, enemy_list
    global legacy
    first_map, attk, defn, HP, exp, bag, receipts_and_deleted_tweets , HP_Demon_Lord = rpg(first_map, 'C',attk, defn, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug)
    update_all_objects(enemy_list, first_map)
    check_stage_progression()
    Frame, UIText = map_to_screen(first_map)
    UI_of_Canvas.configure(text=UIText)
    if legacy: gamewindow.configure(text=Frame)

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
if legacy: gamewindow.grid(row=0, column=0)
UI_of_Canvas.grid(row=0, column=1)
gamecanvas.grid(row=1, column=1)
tk.mainloop()


