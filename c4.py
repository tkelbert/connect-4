import colorama
from colorama import Back, Fore, init
from random import randint, random

def pct(text, color):
    # Use colorama to set the foreground color of the text
    print(color + text)

# Initialize colorama
colorama.init()

# Call the function and pass it the Fore class and a color constant
pct("Blue text", colorama.Fore.BLUE)

# Reset the colors to the default
colorama.deinit()


print(Back.BLUE + 'working?')
import sys


import playMoveClass
from playMoveClass import CFB

game = CFB()  # Create a new CFB object

game.print_board()  # Print the board

board1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

bb = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ',
    8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ',
    15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ',
    22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ',
    29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ',
    36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' '}
for key in bb:
    if bb[key] == ' ':
        bb[key] = '#'
print(bb)
#bb_n = {key: '#' if value == ' ' else value for key, value in bb.items()}

#column list section
columnDict = {
    "col1": [{1, 8, 15, 22, 29, 36}],
    "col2": [{2, 9, 16, 23, 30, 37}],
    "col3": [{3, 10, 17, 24, 31, 38}],
    "col4": [{4, 11, 18, 25, 32, 39}],
    "col5": [{5, 12, 19, 26, 33, 40}],
    "col6": [{6, 13, 20, 27, 34, 41}],
    "col7": [{7, 14, 21, 27, 35, 42}]
}
seven = [1,2,3,4,5,6,7]

row1 = [36,37,38,39,40,41,42]

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
def convertToBB(grid):
    for row in range(6):
        for col in range(7):
            index = row*7 + col + 1
            bb[index] = game.get_value(row,col)
    return bb
def create_number_list(start, end): 
    number_list = []
    for number in range(start, end+1):
        number_list.append(number)
    return number_list
def printVictory(list):
    for row in range(6):
        print('\n')
        for col in range(7):
            # Calculate the index of the current position in the dictionary
            index = row*7 + col + 1
            if index in list:
                print(Back.GREEN + bb[index], end ='||')
            else:
                print(bb[index], end = '||')
                print(Fore.WHITE,end = '')
                colorama.deinit()
    print(Back.BLACK)
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
            print(Back.CYAN)
            print("here are the index numbers for the winning 4 tokens. No wrap around detected", list1)
            printVictory(list1)
            return True
#this search function pinwheels around the played piece and checks if all 4 pieces are the same token
#
def searchL1(x, y, letter):
    # Generate random 'X' and 'O' values for the positions on the game board
    index2 = x*7 + y + 1
    
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
    # print('ddddd',detector)
    # print("bud",bud)
    # print(index2,"i")
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
    
    thirdToken  = dict_comp1(pp,letter)
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
    except NameError:
        pass
    
  
def searchL2(x,y,letter):
    index = x*7 + y + 1
    itg(bb,index)
    tr = (7*(x-1)) + (y + 1) + 1
    tl = (7*(x-1)) + (y-1) + 1
    ml = (7*x) + (y-1) + 1
    mr = (7*x) + (y+1) + 1
    bl = (7*(x+1)) + (y-1) + 1
    bm = (7*(x+1)) + y + 1
    br = (7*(x+1)) + (y+1) + 1
    dings = {}
    index = x*7 + y + 1
    islam = {}
    bud = {}
    clock = {}
    surroundings = [tr,mr,br,bm,bl,ml,tl]
    for i, value in enumerate(surroundings):
        if value > 0 and value < 43:
            dings[i+1] = bb[value]
            clock[i+1] = value
    bible = dict_comp1(dings,letter)
    posSur = [x for x in surroundings if x > 0 and x < 43]
    print('p',posSur)
    for items in posSur:
        islam[items] = bb[items]
        if bb[items] == letter:
            bud[items] = bb[items]
    print(index)
    print(letter)
    print("dings",dings)
    print("bible",bible)
    if len(bible) <= 1:
        print('not possible to it to satisfy the second pinwheel')
    try:
        if dings[1] == dings[5] and dings[1] == letter:
            print('up and to the right')
            uright = [clock[1], index, clock[5]]
            print(uright)
            rate = clock[1] - index
            new1 = clock[1] + rate
            new2 = clock[5] - rate
            print(f"new1{new1}, bb[new1]: {bb[new1]} and new2{new2}, bb[new2]{bb[new2]}")
            if bb[new1] == letter: 
                try:
                    assert bb[new1]
                    print(new1)
                    uright.append(new1)
                    print('uright',uright)
                except AssertionError:
                    print('not in index')
                
            if bb[new2] == letter:
                try:
                    assert bb[new2]
                    print('new2',new2)
                    uright.append(new2)
                    print('uright',uright)
                except AssertionError:
                    print('not in index')
            if bb[new1] != letter and bb[new2] != letter and dings[1] == dings[5]:
                pass
            else:
                if (wrap_around_checker(uright)):
                    return True
    except KeyError:
        pass
    try:            
        if dings[2] == dings[6] and dings[2] == letter:
            print('horizontal trio')
            horizontal = [clock[2],index,clock[6]]
            print(horizontal)
            rate = 1
            new1 = clock[2] + rate
            new2 = clock[6] - rate
            print(f"new1:{new1}, bb[new1]: {bb[new1]} and new2{new2}, bb[new2]{bb[new2]}")
            if bb[new1] == letter: 
                try:
                    assert bb[new1]
                    print(new1)
                    horizontal.append(new1)
                    print('horizontal',horizontal)
                except AssertionError:
                    print('not in index')
                
            if bb[new2] == letter:
                try:
                    assert bb[new2]
                    print('new2',new2)
                    horizontal.append(new2)
                    print('horizontal',horizontal)
                except AssertionError:
                    print('not in index')
            if bb[new1] != letter and bb[new2] != letter and dings[2] == dings[6]:
                pass
            else:
                if (wrap_around_checker(horizontal)):
                    return True

    except KeyError:
        pass
    try:
        if dings[3] == dings[7] and dings[3] == letter:
            print('x = - y')
            uleft = [clock[3],index, clock[7]]
            print(uleft)
            rate = index - clock[2]
            new1 = clock[3] - rate
            new2 = clock[7] + rate
            print(f"new1{new1}, bb[new1]: {bb[new1]} and new2{new2}, bb[new2]{bb[new2]}")
            if bb[new1] == letter: 
                try:
                    assert bb[new1]
                    print(new1)
                    uleft.append(new1)
                    print('uleft',uleft)
                except AssertionError:
                    print('not in index')
                
            if bb[new2] == letter:
                try:
                    assert bb[new2]
                    print('new2',new2)
                    uleft.append(new2)
                    print('uleft',uleft)
                except AssertionError:
                    print('not in index')
            if bb[new1] != letter and bb[new2] != letter and index == letter and dings[3] == dings[7]:
                pass
            else:
                if (wrap_around_checker(uleft)):
                    return True
    except KeyError:
        pass
    
pluto = board1
def whoFirst():
    who = int(input("Write the number 1 to go first and the number 2 if you want to go second\n"))
    if who != 1 and who != 2:
        who = int(input("That wasn't one of the options asshole"))
        if who != 1 and who != 2:
                whoFirst()
    return who
def whichLetter():
    who = str(input("pick 'X' or 'O'"))
    who.capitalize()
    print(who)
    if who != 'O' and who != 'X':
        who = str(input("That wasn't one of the options asshole"))
        if who != 'O' and who != 'X':
            whoFirst()
    return who
def printBoard():
    for i,element in enumerate(pluto):
        print(pluto[i])

def getRow():
    print('Pick the column that you would like to drop your piece into')
    a = int(input('Options (1-7) Enter here: '))
    try:
        assert a in range(1,8)
    except AssertionError:
        getRow()
    return a
def gravity(col,letter):
    unfilled = 0
    #interate through each column, adding to a number that represents the level of the pieces
    for i in range(6):
        if game.get_value(i,col) == '#':
            unfilled += 1
    row3 = unfilled - 1
    convertToBB(game)
    game.play_move(row3,col,letter)
    if (searchL1(row3,col,letter)):
        print('you won!!!!! fucker')
        exit()
    if (searchL2(row3,col,letter)):
        print('second inner pinwheel')
        exit()
    else:
        print('you did not win.... fucker')

 #return a value that represents the position the new piece will be added.
def insertTokenFirstMove(letter):
    print("column number is the top number of  board in blue text.")
    pct("1   2   3   4   5   6   7", colorama.Fore.BLUE)

    print(bb)
    print("Welcome to connect 4! This game will test humanity against machine, and you are up to the plate")
    print("Which column do you want to put your piece in? It will fall to the bottom of that column ")
    t = int(input("Column number: "))
    e = t + 35
    print(t)
    e = int(e)

    try:
        print(bb[e])
    except KeyError:
        print("that choice does not correspond to a location on the board")
        insertTokenFirstMove(letter)
    game.play_move(5, (t-1),letter)
    if t in seven:
        game.print_board()
        #my_dict["Name"].append("Guru")
        #my_dict["Address"].append("Mumbai")
        #my_dict["Age"].append(bb30)
        #print(my_dict)
def fcompMove(letter):
    compcol = 0
    x = (randint(1,7) - 1)
    y = (randint(1,6) - 1)
    gravity(x,letter)

def compMove(letter):
    bestScore = -10000




def main():
    player = whichLetter()
    if player == 'X' or player == 'x':
        computer = 'O'
    else:
        computer = 'X'
    insertTokenFirstMove(player)
    win = 0 
    while '#' in bb.values():
        
        fcompMove(computer)
        game.print_board()
        gravity(getRow()-1,player)
        
main()

def minimax():
    pass
