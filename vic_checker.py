import colorama
from colorama import Back, Fore, init

def pct(text, color):
    # Use colorama to set the foreground color of the text
    print(color + text)

# Initialize colorama
colorama.init()


print(Back.BLACK + 'working?')
import sys

import random

import playMoveClass
from playMoveClass import CFB

# Create a new CFB object
game = CFB()

# Initialize an empty dictionary representing the state of the game board
bb = {i: ' ' for i in range(1, 43)}

# Define a function that returns a dictionary with only the key-value pairs from a given dictionary where the value is equal to a given letter
def dict_comp1(dictionary, letter):
    return {key: value for key, value in dictionary.items() if value == letter}

# Define a function that prints the values in a dictionary in a grid format
def itg(dictionary,index2):
    for row in range(6):
        print('\n')
        for col in range(7):
            # Calculate the index of the current position in the dictionary
            index = row*7 + col + 1
            if index == index2:
                print(Fore.CYAN, end ='')
            # Print the value at the current position
            print(dictionary[index], end = '||')
            print(Fore.WHITE,end = '')

def create_number_list(start, end): 
    number_list = []
    for number in range(start, end+1):
        number_list.append(number)
    return number_list

def wrap_around_checker(list1):
    print(list1)
    leftEdge = [1, 8, 15, 22, 29, 36]
    rightEdge = [7, 14, 21, 27, 35, 42]
    is_wrap_around = False
    if not all(x in leftEdge for x in list1) and not all(x in rightEdge for x in list1):
        for num in list1[1:3]:
            if num in leftEdge or num in rightEdge:
                is_wrap_around = True
                break
        if is_wrap_around:
            print('wrap around detected!!!!')

            return False
        else:
            print("here are the index numbers for the winning 4 tokens. No wrap around detected", list1)
            return True

    # print(f"list0:{list1[0]}list1:{list1[1]}list2:{list1[2]},list3:{list1[3]}")
    # if not all(x in leftEdge for x in list1) and not all(x in rightEdge for x in list1):
    #     if list1[0] not in leftEdge and list1[0] not in rightEdge:
    #         if list1[1] in leftEdge or list1[2] in leftEdge:
    #             print('wrap around detected')
    #         elif list1[1] in rightEdge or list1[2] in rightEdge:
    #             print('wrap around detected')
    #     else:
    #         print("here are the index numbers for the winning 4 tokens. No wrap around detected",list1)
# Define a function that searches for a given letter in the positions surrounding a given position on the game board
def SearchL1(x, y, letter):
    # Generate random 'X' and 'O' values for the positions on the game board
    index2 = x*7 + y + 1
    for key in bb:
        if key != index2:
            bb[key] = random.choice(['X','O'])
        else:
            bb[key] = letter
    # Convert the dictionary into a 2D list representing the game board as a grid
    grid = []
    for row in range(6):
        grid.append([])
        for col in range(7):
                index = row*7 + col + 1
                value = bb.get(index)
                # Store the value at the current position in the grid
                grid[row].append(bb[index])  
    # Create a dictionary of the indices that are multiples of 7
    mo7 = {i: i for i in range(1, 43) if i % 7== 0}
    # Calculate the index of the given position in the dictionary

    

    # Initialize a dictionary containing the values of the positions surrounding the given position
    values = {}
    try:
        # Populate the dictionary with the values of the surrounding positions
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
    # Calculate the indices of the surrounding positions
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
    print('p',posSur)
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
            # print(f"nextLayer{nextLayer} = index2({index2}) + (2*rate:{rate[i]}[i{i}])" )
            result2.append(nextLayer)
        except NameError:
            print('i')
    for i in range(len(rate)):
        try:
            nextLayer2 = index2 - (3*(rate[i]))
            # print(f"nextLayer{nextLayer2} = index2({index2}) + (2*rate:{rate[i]}[i{i}])" )
            result3.append(nextLayer2)
        except NameError:
            print('i')
    for i in range(len(rate)):
        try:
            nextLayer3 = index2 - (4*(rate[i]))
            # print(f"nextLayer{nextLayer3} = index2({index2}) + (2*rate:{rate[i]}[i{i}])" )
            result4.append(nextLayer3)
        except NameError:
            print('i')            
    itg(bb,index2)
    print(f"result2:{result2} and result3:{result3} and result:{result}")
    pp = {}
    ppp = {}
    for items in result3:
        if items == letter:
            pp[items] = bb[items]
    try:
        for i, val  in enumerate(result2):
            if bb[val] == letter:
                pp[val] = bb[val]
    except KeyError:
        print('keyer')
        pass
    try:
        for i, val  in enumerate(result3):
            if bb[val] == letter:
                ppp[val] = bb[val]
    except KeyError:
        print('keyerror')
        pass
    
    print('pp',pp)
    print('ppp',ppp)
    thirdToken  = dict_comp1(pp,letter)
    print(thirdToken)
    ct = 0
    winlist = []
    try:
        for itm in ppp.keys():
            if index2 < itm:
                indexer = itm - index2
                rater = indexer/3
                if rater % 1 == 0:
                    if bb[itm - rater] == letter:
                        if len(winlist) > 0:
                            winList2 = []
                            winlist2.append(itm)
                            winlist2.append(int(itm + rater))
                            winlist2.append(int(itm + (2 * rater)))
                            winlist2.append(index2)
                            print("winList2:",winList2)
                        winlist.append(itm)
                        winlist.append(int(itm - rater))
                        winlist.append(int(itm - (2 * rater)))
                        winlist.append(index2)
                        if wrap_around_checker(winlist):
                            return True
                        print("you won to the right motherfucker, this one subtracts the played tile from the final one that was found to be the same")
                        print(f"itm:{itm}, indexer:{indexer}, played tile: {index2}, rater {rater}, winList{winlist}") 
            else:
                indexer = index2 - itm
                rater = indexer/3
                if rater % 1 == 0:
                    if bb[itm + rater] == letter:
                        if len(winlist) > 0:
                            winList2 = []
                            winlist2.append(itm)
                            winlist2.append(int(itm + rater))
                            winlist2.append(int(itm + (2 * rater)))
                            winlist2.append(index2)
                            print("winList2:",winList2)
                        winlist.append(itm)
                        winlist.append(int(itm + rater))
                        winlist.append(int(itm + (2 * rater)))
                        winlist.append(index2)
                        if wrap_around_checker(winlist):
                            return True
                        print("you won to the left motherfucker, going down in index number")
                        print(rater) 
                        print(f"itm:{itm}, indexer:{indexer}, played tile: {index2}, rater {rater}, winList{winlist}") 
      
           
        return winlist
    except KeyError:
        print('key')
        pass
    except NameError:
        pass
    
xx = random.randint(0,5)
yy = random.randint(0,6)

SearchL1(xx,yy,'O')
