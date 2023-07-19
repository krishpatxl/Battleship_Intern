from random import randint
from string import ascii_uppercase as letters

#Creating the board

def create_board():
    try:
        size = eval(input("Please enter a size: "))
    except:
        print("That is not a number, try again")

    Hidden_Pattern=[[' ']*size for x in range(size)]
    Guess_Pattern=[[' ']*size for x in range(size)]

    return Hidden_Pattern, Guess_Pattern, size
#Printing the board together
def print_board(board):
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

abc = ["A","B","C","D","E","F","G","H","I","J"]
def get_ship_location():
    #Enter the row number between 1 to 10
    row = (input('Please enter a ship row: '))
    while row not in '12345678910':
        print("Please enter a valid row ")
        row=input('Please enter a ship row: ')
    #Enter the Ship column from A TO J
    column = input('Please enter a ship column: ').upper()

    while column not in abc:
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-J ').upper()
    return int(row)-1,let_to_num[column]
#starts at line 33
#This function creates the ships
def create_ships(board):
        ship_r, ship_cl = randint(0, size-1), randint(0, size-1)
        board[ship_r][ship_cl] = 'X'
        
def input_validation(row, column, size):

    if row not in range(size):
        print("Please enter a number on the board: ")

    if column not in range (size):
        print("Please enter a number on the board: ")
def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count
while True:
    print('Welcome to Battleship, Lets Play !!') 
    Hidden_Pattern, Guess_Pattern, size = create_board()
    
    a = input("Do you want the ships placed by yourself? ")
    if a == "No" or a == "no":
        

        let_to_num={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
        create_ships(Hidden_Pattern)
        #print_board(Hidden_Pattern)

        turns = 100
        while turns > 0:
            print_board(Guess_Pattern)
            row,column = get_ship_location()
            if Guess_Pattern[row][column] == 'O':
                print(' You already guessed that, try again. ')
            elif Hidden_Pattern[row][column] =='X':
                print (f"You hit ({str(row+1)},{abc[column]})")
                print(' Congrats, you have hit a ship ')
                Guess_Pattern[row][column] = 'O'
                turns -= 1
            else:
                print (f"You hit ({str(row+1)},{abc[column]})")
                print('You missed LOL')
                Guess_Pattern[row][column] = 'x'
                turns -= 1
            if  count_hit_ships(Guess_Pattern) == 7:
                print("You sunk all the ships, congrats!")
                break
            print(' You have ' +str(turns) + ' tries left ')
            if turns == 0:
                print('You lost')
                break 
        a = input("Would you like to play again?")
        if a == " No" or a == " no":
            break
        
    else: 
        a == "Yes" or a =="yes"
        user_input = input("A")
        
        def convert_letter(string_thing):
            num = ord(user_input.upper()) - 65
            return num
        
        print(convert_letter(user_input))
        row=input('Please enter a ship row: ')
        while row not in '12345678910':
            print("Please enter a valid row ")
        column=input("Please enter a ship column: ")
        print_board(Hidden_Pattern)
    
                
