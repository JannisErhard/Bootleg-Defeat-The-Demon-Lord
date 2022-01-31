#!/usr/bin/env python3
import numpy as np
monster = {'E' : 2, 'D' : 3}

def boundscheck(x,y,field):
    return -1 < x < field.shape[0] and -1 < y < field.shape[1] 


def try_use_key(position, field, bag):
    a, b = [1,0,-1,0], [0,1,0,-1]
    success = False
    for inc_x, inc_y in zip(a,b):
        x,y = position[0]+inc_x, position[1]+inc_y
        if boundscheck(x,y,field):
            if field[x,y] in "-|":
                bag.remove('K')
                field[x, y]  = ' '
                success = True
                break
    return success, field, bag

def try_use_coin(position, field, bag, receipts):
    a, b = [1,0,-1,0], [0,1,0,-1]
    success = False
    for inc_x, inc_y in zip(a,b):
        x,y = position[0]+inc_x, position[1]+inc_y
        if boundscheck(x,y,field):
            if field[x,y] in "M":
                bag.remove('C')
                if receipts[x][y] == 3:
                    field[player_x, player_y-1]  = ' '
                success = True
                break
    return success, field, bag, receipts

def encounter_check(position, field, vert):
    a, b = [1,0,-1,0], [0,1,0,-1]
    damage = 0
    for inc_x, inc_y in zip(a,b):
        x,y = position[0]+inc_x, position[1]+inc_y
        if boundscheck(x,y,field):
            if field[x,y] in "ED":
                print(f'Attack of {field[x,y]} from {x,y} while hero was at {position[0],position[1]}')
                damage += max(0,(monster[field[x,y]]-vert)) 
    return damage 

def rpg(field,  actions, attk, vert, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord, debug): 
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
                pass # orginally resulted in death
            else:
                if i == 'H': # resulted in death when HP was full
                   HP = 3
                   bag.remove('H')
                if i == 'K':
                    if debug: print("I use Key!")
                    key_success, np_field, bag = try_use_key([player_x, player_y], np_field, bag)
                    if not key_success:
                        pass # originally resulted in death 
                if i == 'C':
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
                        pass
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
                    #return None
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
                    #return None
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
                    if debug: print("I hit nothing ...")
                    break
                    #return None
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
                    if debug: print("I hit nothing ...")
                    break
                    #return None
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
            HP -= encounter_check([player_x, player_y], np_field, vert)
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
# check wether enemies may attack
        if i != 'F':
            HP -= encounter_check([player_x, player_y], np_field, vert)
    for i in range(0,x_len):
        sublist =[np_field[:][i]]
        map_back.append(list(np_field[:][i]))
    bag.sort()
    return map_back, attk, vert, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord
