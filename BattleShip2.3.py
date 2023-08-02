import random

GRID_SIZE = 10

class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length

def create_grid():
    return [['O' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def print_board(board, hidden=True):
    # Print column labels (numbers)
    print('', end=' ')
    for col in range(1, GRID_SIZE + 1):
        print(f'{col:2}', end='')
    print()

    # Print rows with labels (letters) and board content
    for row in range(GRID_SIZE):
        print(chr(65 + row) + ' ', end='')  # Convert row index to letter label
        for col in range(GRID_SIZE):
            if hidden and board[row][col] == 'X':  # Hide the user's ships on the opponent's board
                print('O', end=' ')
            else:
                print(board[row][col], end=' ')
        print()

def place_ship_manually(board, ship):
    print(f"Placing {ship.name}")
    while True:
        try:
            col_guess = int(input(f"Enter the row index (1 to {GRID_SIZE}): "))
            row_guess = input(f"Enter the column index (A to {chr(64 + GRID_SIZE)}): ").upper()
            orientation = input("Choose the orientation (vertical/horizontal): ").lower()
            if orientation not in ['vertical', 'horizontal']:
                print("Invalid orientation. Please choose either 'vertical' or 'horizontal'.")
                continue

            if 1 <= col_guess <= GRID_SIZE and 'A' <= row_guess <= chr(64 + GRID_SIZE):
                row = ord(row_guess) - 65  # Convert the row letter to the corresponding index
                col = col_guess - 1

                # Check if the ship can be placed in the chosen position
                if orientation == 'vertical':
                    if row + ship.length <= GRID_SIZE and all(board[row + i][col] == 'O' for i in range(ship.length)):
                        break
                else:
                    if col + ship.length <= GRID_SIZE and all(board[row][col + i] == 'O' for i in range(ship.length)):
                        break

                print("Invalid ship placement. The ship overlaps with another ship or goes out of the grid.")
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
    return row, col, orientation

def place_ship_randomly(board, ship, ships):
    while True:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        orientation = random.choice(['vertical', 'horizontal'])

        # Check if the ship can be placed in the chosen position and it's far from other ships
        if orientation == 'vertical':
            if row + ship.length <= GRID_SIZE and all(board[row + i][col] == 'O' for i in range(ship.length)):
                far_from_other_ships = True
                for ship_row, ship_col, _, ship_orientation in ships:
                    if ship_orientation == 'vertical':
                        if abs(row - ship_row) < 2 * ship.length and abs(col - ship_col) < 2:
                            far_from_other_ships = False
                            break
                    else:
                        if abs(row - ship_row) < 2 and abs(col - ship_col) < 2 * ship.length:
                            far_from_other_ships = False
                            break
                if far_from_other_ships:
                    break
        else:
            if col + ship.length <= GRID_SIZE and all(board[row][col + i] == 'O' for i in range(ship.length)):
                far_from_other_ships = True
                for ship_row, ship_col, _, ship_orientation in ships:
                    if ship_orientation == 'vertical':
                        if abs(row - ship_row) < 2 and abs(col - ship_col) < 2 * ship.length:
                            far_from_other_ships = False
                            break
                    else:
                        if abs(row - ship_row) < 2 * ship.length and abs(col - ship_col) < 2:
                            far_from_other_ships = False
                            break
                if far_from_other_ships:
                    break

    return row, col, orientation

def is_valid_guess(guess):
    if len(guess) != 2:
        return False
    row_guess, col_guess = guess
    if 1 <= col_guess <= GRID_SIZE and 'A' <= row_guess <= chr(64 + GRID_SIZE):
        row = ord(row_guess) - 65
        col = col_guess - 1
        return True, (row, col)
    return False, None
def is_grid_full(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 'O':
                return False
    return True

def battleship_game():
    print("Welcome to Battleship!")

    user_board = create_grid()
    computer_board = create_grid()

    while True:
        place_option = input("Do you want to manually place your ships? (yes/no): ").lower()
        if place_option == 'yes':
            ships = [
                Ship("Carrier", 5),
                Ship("Battleship", 4),
                Ship("Destroyer", 3),
                Ship("Submarine", 3),
                Ship("Patrol Boat", 2)
            ]

            user_ships = []
            for ship in ships:
                print(f"\n{ship.name} ({ship.length} long)")
                user_row, user_col, orientation = place_ship_manually(user_board, ship)
                user_ships.append((user_row, user_col, ship.length, orientation))  # Store the orientation as well
                if orientation == 'vertical':
                    for i in range(ship.length):
                        if i == 0:
                            user_board[user_row][user_col] = ship.name[0]
                        else:
                            if user_row + i < GRID_SIZE:
                                user_board[user_row + i][user_col] = ship.name[0]
                else:
                    for i in range(ship.length):
                        if i == 0:
                            user_board[user_row][user_col] = ship.name[0]
                        else:
                            if user_col + i < GRID_SIZE:
                                user_board[user_row][user_col + i] = ship.name[0]
            break
        elif place_option == 'no':
            ships = [
                Ship("Carrier", 5),
                Ship("Battleship", 4),
                Ship("Destroyer", 3),
                Ship("Submarine", 3),
                Ship("Patrol Boat", 2)
            ]

            user_ships = []
            for ship in ships:
                user_row, user_col, orientation = place_ship_randomly(user_board, ship, user_ships)
                user_ships.append((user_row, user_col, ship.length, orientation))  # Store the orientation as well
                if orientation == 'vertical':
                    for i in range(ship.length):
                        if i == 0:
                            user_board[user_row][user_col] = ship.name[0]
                        else:
                            if user_row + i < GRID_SIZE:
                                user_board[user_row + i][user_col] = ship.name[0]
                else:
                    for i in range(ship.length):
                        if i == 0:
                            user_board[user_row][user_col] = ship.name[0]
                        else:
                            if user_col + i < GRID_SIZE:
                                user_board[user_row][user_col + i] = ship.name[0]
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Place opponent's ships randomly on the computer board
    computer_ships = []
    for ship in ships:
        computer_row, computer_col, orientation = place_ship_randomly(computer_board, ship, computer_ships)
        computer_ships.append((computer_row, computer_col, ship.length, orientation))  # Store the orientation as well
        if orientation == 'vertical':
            for i in range(ship.length):
                if i == 0:
                    computer_board[computer_row][computer_col] = 'O'
                else:
                    if computer_row + i < GRID_SIZE:
                        computer_board[computer_row + i][computer_col] = 'O'
        else:
            for i in range(ship.length):
                if i == 0:
                    computer_board[computer_row][computer_col] = 'O'
                else:
                    if computer_col + i < GRID_SIZE:
                        computer_board[computer_row][computer_col + i] = 'O'

    num_turns = 100  # Maximum number of turns = number of cells on the grid
    for turn in range(num_turns):
        print(f"\nTurn {turn + 1}:")
        if turn % 2 == 0:
            print("Your Board:")
            print_board(user_board, hidden=True)
            print("\nOpponent's Board:")
            print_board(computer_board, hidden=True)
        else:
            print("Your Board:")
            print_board(user_board, hidden=False)
            print("\nOpponent's Board:")
            print_board(computer_board, hidden=True)

        while True:
            try:
                col_guess = int(input(f"Enter the row index (1 to {GRID_SIZE}): "))
                row_guess = input(f"Enter the column index (A to {chr(64 + GRID_SIZE)}): ").upper()
                is_valid, (row_guess, col_guess) = is_valid_guess((row_guess, col_guess))
                if is_valid:
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid row and column numbers.")

        if (row_guess, col_guess) in computer_ships:
            for ship in ships:
                if computer_board[row_guess][col_guess] == 'O':  # Check if the opponent's shot hit a ship on user's grid
                    ship_name = ship.name
                    break
            print(f"Congratulations! The opponent hit your {ship_name}!")
            computer_board[row_guess][col_guess] = 'X'
        else:
            print("The opponent missed!")
            computer_board[row_guess][col_guess] = '*'

        # Computer's turn
        computer_guess_row, computer_guess_col, _ = place_ship_randomly(computer_board, ships[-1], computer_ships)

        print("\nComputer's Guess:")
        print(f"Row: {chr(65 + computer_guess_row)}, Column: {computer_guess_col + 1}")

        if (computer_guess_row, computer_guess_col) in user_ships:
            for ship in ships:
                if user_board[computer_guess_row][computer_guess_col] == ship.name[0]:
                    ship_name = ship.name
                    break
            print(f"The opponent hit the {ship_name}!")
            user_board[computer_guess_row][computer_guess_col] = 'X'
        else:
            print("The opponent missed!")
            user_board[computer_guess_row][computer_guess_col] = '*'

        # Check if the grid is full
        if is_grid_full(user_board) or is_grid_full(computer_board):
            print("Game over! The grid is full.")
            break

    else:
        print("Game over! You've used all your turns.")

    print("\nFinal Board:")
    print("Your Board:")
    print_board(user_board, hidden=False)
    print("\nOpponent's Board:")
    print_board(computer_board, hidden=True)

    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input == 'yes':
        battleship_game()
    else:
        print("Thanks for playing Battleship!")

battleship_game()
