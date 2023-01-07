from random import random, choice
import random

import playMoveClass
from playMoveClass import CFB

game = CFB()  # Create a new CFB object


grid = []
bb = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ',
8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ',
15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ',
22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ',
29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ',
36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' '}

def dict_comp1(bb,letter):
    cool = {key: value for key, value in bb.items() if value == letter}
    return cool





def SearchL1(x,y,letter): ##use a bool where true is 'X' and false is 'O"
    #get the information in the form of a grid that can use the dict values below. need to add things so that it doesn't 
    #search beyond the grid, so that would be [0-5][0-6] allowed and anything else not

    for key in bb:
        bb[key] = random.choice(['X','O'])
    print(bb)
    for row in range(6):
        grid.append([])
        for col in range(7):
                index = row*7 + col + 1
                value = bb.get(index)
                cc = {index : game.get_value(row, col)}
                grid[row].append(bb[index])  
    mo7 = {i: i for i in range(1, 43) if i % 7== 0}
    index2 = x*7 + y + 1
    print(index2)
    values = {
        "tr": grid[x-1][y+1],
        "tl": grid[x-1][y-1],
        "ml": grid[x][y-1],
        "mr": grid[x][y+1],
        "bl": grid[x+1][y-1],
        "bm": grid[x+1][y],
        "br": grid[x+1][y+1]
    }

    tr = (7*(x-1)) + (y + 1) + 1
    tl = (7*(x-1)) + (y-1) + 1
    ml = (7*x) + (y-1) + 1
    mr = (7*x) + (y+1) + 1
    bl = (7*(x+1)) + (y-1) + 1
    bm = (7*(x+1)) + y + 1
    br = (7*(x+1)) + (y+1) + 1
    
    islam = {}
    bud = {}
    surroundings = [tr,tl,ml,mr,bl,bm,br]
    posSur = [x for x in surroundings if x > 0]
    print(posSur)
    for items in posSur:
        
        islam[items] = bb[items]
        if bb[items] == letter:
            bud[items] = bb[items]
    
    
    detector = dict_comp1(islam,letter)
    print('ddddd',detector)
    print("bud",bud)
    return bud

    

SearchL1(0,0,'O')