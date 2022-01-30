#!/usr/bin/env python3
campaign = {}
campaign[4] = [
            list('SX#  EDE '),
            list('CC# EEEEE'),
            list('#-#     X'),
            list('         '),
            list('^       K'),
        ]
campaign[1] = [['K', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 'X', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', 'S', '#', ' ', ' ', 'D', ' ', ' '],
[' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', 'E', ' ', 'E', ' '],
['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '-', '#', '#'],
[' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' '],
[' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', 'E', '#', '#', 'E', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'S', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', 'K', '#', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '#', '#', 'E', '#', '#', 'E', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ']]
campaign[2] = [
['S',' ',' ',' ',' ',' ',' ','#',' '],
[' ',' ','#','#','#','#',' ','|','D'],
[' ',' ','E',' ',' ','#',' ','#',' '],
['#','#','#','#','E','#',' ','#','#'],
[' ',' ',' ',' ',' ','#',' ','E',' '],
['^',' ','E',' ',' ','E','K','E','X']]
campaign[3] = [
[' ',' ',' ','#','H','#','E','E','K'],
[' ','#','E','#',' ','#',' ','E','E'],
[' ','#',' ',' ',' ','|',' ',' ','E'],
[' ','#','#','#',' ','#','#','#','-'],
[' ','K','S','#',' ','#','D','E',' '],
['E','E','E','#','^','#','E',' ',' ']]
campaign[5] = [
['E',' ', 'E', ' ', 'E', 'E', 'E', ' ', 'E', ' ', ' ', 'E', ' ', '^', ' ', 'E', 'E', 'E'],
['E',' ', 'E', ' ', 'E', ' ', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', ' ', 'E'],
['E','E', 'E', ' ', 'E', 'E', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', 'D', 'E'],
['E',' ', 'E', ' ', 'E', ' ', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', ' ', 'E'],
['E',' ', 'E', ' ', 'E', 'E', 'E', ' ', 'E', 'E', ' ', 'E', 'E', ' ', ' ', 'E', 'E', 'E']]
campaign['empty'] = [
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
['^',' ',' ',' ',' ',' ',' ',' ',' ']]
campaign['win'] = [
list('You Win'+' '*(len('Thanks for playing!')-7)),
list('Game Over'+' '*(len('Thanks for playing!')-9)),
list(' '*len('Thanks for playing!')),
list('Thanks for playing!')
        ]
