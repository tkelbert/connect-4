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
    print(cool)
    return cool


def itg(tt):
     for row in range(6):
        print('\n')
        for col in range(7):
            index2 = row*7 + col + 1
            print(tt[index2], end = '||')




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
    try:
        values = {
        "tr": grid[x-1][y+1],
        "tl": grid[x-1][y-1],
        "ml": grid[x][y-1],
        "mr": grid[x][y+1],
        "bl": grid[x+1][y-1],
        "bm": grid[x+1][y],
        "br": grid[x+1][y+1]
        }
    except IndexError:
        print('endie')

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
    posSur = [x for x in surroundings if x > 0 and x < 43]
    print(posSur)
    for items in posSur:
        
        islam[items] = bb[items]
        if bb[items] == letter:
            bud[items] = bb[items]
    
    
    detector = dict_comp1(islam,letter)
    print('ddddd',detector)
    print("bud",bud)
    print(index2,"i")

    result = []
    result2 = []
    result3 = []
    result4 = []
    for key, value in bud.items():
        # key is the key of the dictionary (a string)
        # value is the value of the dictionary (a number)
        z = index2 - key
        result.append(z)
    firstIter = []
    for item in bud.keys():
        firstIter.append(item)
    rate = []
    for item in firstIter:
        w = index2 - item
        rate.append(w)
        print(rate)
    for i in range(len(rate)):
        try:
            nextLayer = index2 - (2*(rate[i]))
            print(f"nextLayer{nextLayer} = index2({index2}) + (2*rate:{rate[i]}[i{i}])" )
            result2.append(nextLayer)
        except NameError:
            print('i')
    for i in range(len(rate)):
        try:
            nextLayer2 = index2 - (3*(rate[i]))
            print(f"nextLayer{nextLayer2} = index2({index2}) + (2*rate:{rate[i]}[i{i}])" )
            result3.append(nextLayer2)
        except NameError:
            print('i')
    for i in range(len(rate)):
        try:
            nextLayer3 = index2 - (4*(rate[i]))
            print(f"nextLayer{nextLayer3} = index2({index2}) + (2*rate:{rate[i]}[i{i}])" )
            result4.append(nextLayer3)
        except NameError:
            print('i')            
    itg(bb)
    pp = {}
    for items in result3:
        if items == letter:
            pp[items] = bb[items]

    # dict_comp1(result2,letter)
    # dict_comp1(result3,letter)
    # dict_comp1(result4,letter)
    print(bb)
    o = index2
    print('r',rate)
    try:
        for items in rate:
        
            print(items)
            if bb[o] == bb[o-items] and bb[o] == bb[o-(items*2)] and bb[o] == bb[o-(items*3)] and bb[o] != '#':
                print(items)
                print('a')
                return True
            if bb[o] == bb[o-items] and bb[o] == bb[o-(items*2)] and bb[o] == bb[o+(items)] and bb[o] != '#':
                print(items)
                print('this b boy won')
                return True
            if bb[o] == bb[o-items] and bb[o] == bb[o+(items*2)] and bb[o] == bb[o+(items*3)] and bb[o] != '#':
                print(items)
                print('this c boy won')
                return True
            if bb[o] == bb[o-items] and bb[o] == bb[o-(items*2)] and bb[o] == bb[o-(items*3)] and bb[o] != '#':
                print(items)
                print('this d boy won')
            
                return True
            if bb[o] == bb[o-items] and bb[o] == bb[o-(items*2)] and bb[o] == bb[o+(items)] and bb[o] != '#':
                print('this d boy won')
            
                return True
            if bb[o] == bb[o+items] and bb[o] == bb[+(items*2)] and bb[o] == bb[o+(items*3)] and bb[o] != '#':
                print('this e boy won')
              
                return True
    except KeyError:
        pass
    print(result2)
    print(result3)
    for item in result3:
        if item > 0 and item < 43:
            if bb[item] == letter:
                print(item)
                print('yo',bb[item])
                for items in result2:
                    if bb[items] == letter and bb[index2] == letter:
                        print('2',bb[items])
                        if bb[index2] == letter:
                            print('this nigga won!!')
                            print(item)
                            print(bb[items])
                    
                            return True
   
(SearchL1(3,3,'X'))
SearchL1(3,3,'O')