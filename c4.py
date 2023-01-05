import colorama
from colorama import Back, Fore, init
import random

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




#def play_game():
# #board = CFB()
    #board.play_move(0, 0)
    #board.print_board()```

#play_game()


board = {
    'columns': 7,
    'rows': 6,
    'board': [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
}
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
    36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' x', 42: ' '}

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

pluto = board
def whoFirst():
    who = int(input("Write the number 1 to go first and the number 2 if you want to go second\n"))
    if who != 1 and who != 2:
        who = int(input("That wasn't one of the options asshole"))
        if who != 1 and who != 2:
                whoFirst()
    return who

def add_7(numbers,i):
    try:
        h = numbers + 7
    except TypeError:
        whoFirst()
    return h




def printBoard():
    for i,element in enumerate(pluto):
        print(pluto[i])
def getRow():
    print('Pick the column that you would like to drop your piece into')
    a = int(input('Options (1-7) Enter here: '))
    try:
        assert a in range(1,8)
    except AssertionError:
        getRow(a)
    return a
def gravity():
    #interate through each column, adding to a number that represents the level of the pieces
    f = 7
    a  = (getRow() - 1)
    count = 0
    l = 0
    #iterate through the column, checking for how many spots are filled. get a number representing this
    for i in range(6):
        b = game.get_value(i,a)
        if b != '0':
            count =+ 1

        print("count:",count)
        if count > 0:
            if i == 5:
                sum = (5 - count)
                game.play_move(sum,a,'x')
    game.print_board()








                # do something with the column


    #subject will later pick move by simply specifying which row they want to play in
    #


# Fore changes the text's foreground color
#print(Fore.BLUE + "Blue Letters")

#Back changes the text's background color
#print(Back.WHITE + "White Background")

def mark_space(num):
    bb[num] = "X"


 #return a value that represents the position the new piece will be added.
def insertTokenFirstMove():
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
        insertTokenFirstMove()
    #numbers = [i for i in range(1,43)]
    # for colu in range(0,6):
    #     for ro in range(0,7):
    #         print(game.play_move(colu,ro))
    game.play_move(5, (t-1),'X')



    #print("yo" + andrea)
    #amanda = bb[andrea].append("X |")
  #  print(f"{t}:] ==" + amanda)
    if t in seven:
        game.print_board()
        #my_dict["Name"].append("Guru")
        #my_dict["Address"].append("Mumbai")
        #my_dict["Age"].append(bb30)
        #print(my_dict)

insertTokenFirstMove()
gravity()


def compMove():
    openSq = 0
    empty_list = []
    empty_list = list()
    for i in range(5):
        pass
    pass

def minimax():
    pass

def insertToken():
    print("")
