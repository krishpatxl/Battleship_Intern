 
# ‘X’ indicates the ships hit
# ‘-‘ indicates the hits missed
4
from random import randint

print('Welcome to Battleship, Lets Play !!')
Hidden_Pattern=[[' ']*7 for x in range(7)]
Guess_Pattern=[[' ']*7 for x in range(7)]

let_to_num={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

def print_board(board):
    print('  A B C D E F G')
 
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    #Enter the row number between 1 to 7
    row=input('Please enter a ship row 1-7 ') 
    while row not in '1234567':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-7 ')
    #Enter the Ship column from A TO G
    column=input('Please enter a ship column A-G ').upper() 
    while column not in 'ABCDEFG':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-G ')
    return int(row)-1,let_to_num[column]
