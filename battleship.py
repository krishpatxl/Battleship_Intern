# starts at line 33
# This function creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,4), randint(0,4)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        board[ship_r][ship_cl] = 'X'



def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

create_ships(Hidden_Pattern)
#print_board(Hidden_Pattern)
turns = 8
while turns > 0:
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == 'O':
        print(' You already guessed that, try again. ')
    elif Hidden_Pattern[row][column] =='X':
        print(' Congrats, you have hit a ship ')
        Guess_Pattern[row][column] = 'O'
        turns -= 1
    else:
        print('You missed LOL')
        Guess_Pattern[row][column] = 'x'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("You ")
        break
    print(' You have ' +str(turns) + ' tries left ')
    if turns == 0:
        print('You lost')
        break