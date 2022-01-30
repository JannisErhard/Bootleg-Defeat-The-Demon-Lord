#!/usr/bin/env python3
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
                if i == 'F' and np_field[player_x, player_y] in '<^':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] in '<^':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
        to_check_x, to_check_y = player_x-1, player_y-1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] in '>v':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] in '>v':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
        to_check_x, to_check_y = player_x+1, player_y-1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] in '>^':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] in '>^':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
        to_check_y, to_check_x = player_y+1, player_x-1 
        if 0 <= to_check_y < y_len and 0 <= to_check_x < x_len: #AOO from right and down
            if np_field[to_check_x, to_check_y] == 'E':
                if i == 'F' and np_field[player_x, player_y] in '<v':
                    if debug: print(Flavor_Text_2, max(0,(2-vert)))
                    HP -= max(0,(2-vert))
            if np_field[to_check_x,to_check_y] == 'D':
                if i == 'F' and np_field[player_x, player_y] in '<v':
                    if debug: print(Flavor_Text_1, max(0,(3-vert)))
                    HP -= max(0,(3-vert))
    for i in range(0,x_len):
        sublist =[np_field[:][i]]
        map_back.append(list(np_field[:][i]))
    bag.sort()
    return map_back, attk, vert, HP, exp, bag, receipts_and_deleted_tweets, HP_Demon_Lord
