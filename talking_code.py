from random import randint


def create_board():
    try:
        size = eval(input("please enter a size"))
    except:
        print("that is not a number")

    Hidden_Pattern=[['0']*size for x in range(size)]
    Guess_Pattern=[['0']*size for x in range(size)]

    return Hidden_Pattern, Guess_Pattern, size

def print_board(board):
    print('  A B C D E F G')
 
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

abc = ["A","B","C","D","E","F","G"]
def get_ship_location():
    #Enter the row number between 1 to 7

    row = input('Please enter a ship row 1-7 ')
    while row not in '1234567':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-7 ')
    #Enter the Ship column from A TO G
    column = input('Please enter a ship column A-G ').upper()
    
    while column not in abc:
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-G ')
    return int(row)-1,let_to_num[column]
# starts at line 33
# This function creates the ships
def create_ships(board):
    for ship in range(7):
        ship_r, ship_cl=randint(0,6), randint(0,6)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 6), randint(0, 6)
        board[ship_r][ship_cl] = 'X'

def input_validation(row, column, size):
    
    if row not in range(size):
        print("please enter a number on the board")
    
    if column not in range (size):
        print("please enter a number on the board")
        

def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count
while True:
    a = input("How do you want the ships placed?")
    if a == " Myself" or a == " by myself" or a == " By Myself" or a == " By myself":
        break
    else:
        print('Welcome to Battleship, Lets Play !!') 
        Hidden_Pattern, Guess_Pattern, size = create_board()

        let_to_num={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
        create_ships(Hidden_Pattern)
        #print_board(Hidden_Pattern)
        turns = 10
        while turns > 0:
            print_board(Guess_Pattern)
            row,column =get_ship_location()
            if Guess_Pattern[row][column] == 'O':
                print(' You already guessed that, try again. ')
            elif Hidden_Pattern[row][column] =='X':
                print (f"You hit ({str(row+1)},{abc[column]})")
                print(' Congrats, you have hit a ship ')
                Guess_Pattern[row][column] = 'O'
                turns -= 1
            else:
                print ("You hit " + str(row+1) +' ' + abc[column])
                print('You missed LOL')
                Guess_Pattern[row][column] = 'x'
                turns -= 1
            if  count_hit_ships(Guess_Pattern) == 7:
                print("You hit all the ships")
                break
            print(' You have ' +str(turns) + ' tries left ')
            if turns == 0:
                print('You lost')
                break 
        a = input("Would you like to play again?")
        if a == " No" or a == " no":
            break
    
    
