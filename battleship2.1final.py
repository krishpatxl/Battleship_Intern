import random

def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]

def print_board(board, size, hidden=True):
    for i in range(size):
        for j in range(size):
            if hidden and board[i][j] == 'B':
                print('O', end=' ')
            else:
                print(board[i][j], end=' ')
        print()

def place_ship_manually(board, size, length, ship_name):
    print(f"Placing {ship_name}")
    while True:
        try:
            row = int(input(f"Enter the row index for {ship_name} (1 to {size}): "))
            col = int(input(f"Enter the column index for {ship_name} (1 to {size}): "))
            orientation = input("Choose the orientation (vertical/horizontal): ").lower()
            if orientation not in ['vertical', 'horizontal']:
                print("Invalid orientation. Please choose either 'vertical' or 'horizontal'.")
                continue

            if 1 <= row <= size and 1 <= col <= size:
                row -= 1
                col -= 1

                # Check if the ship can be placed in the chosen position
                if orientation == 'vertical':
                    if row + length <= size and all(board[row + i][col] == 'O' for i in range(length)):
                        break
                else:
                    if col + length <= size and all(board[row][col + i] == 'O' for i in range(length)):
                        break

                print("Invalid ship placement. The ship overlaps with another ship or goes out of the grid.")
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
    return row, col, orientation

def place_ship_randomly(board, size, length, ships):
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        orientation = random.choice(['vertical', 'horizontal'])

        # Check if the ship can be placed in the chosen position and it's far from other ships
        if orientation == 'vertical':
            if row + length <= size and all(board[row + i][col] == 'O' for i in range(length)):
                far_from_other_ships = True
                for ship_row, ship_col, ship_length, ship_orientation in ships:
                    if ship_orientation == 'vertical':
                        if abs(row - ship_row) < 2 * length and abs(col - ship_col) < 2:
                            far_from_other_ships = False
                            break
                    else:
                        if abs(row - ship_row) < 2 and abs(col - ship_col) < 2 * ship_length:
                            far_from_other_ships = False
                            break
                if far_from_other_ships:
                    break

        else:
            if col + length <= size and all(board[row][col + i] == 'O' for i in range(length)):
                far_from_other_ships = True
                for ship_row, ship_col, ship_length, ship_orientation in ships:
                    if ship_orientation == 'vertical':
                        if abs(row - ship_row) < 2 and abs(col - ship_col) < 2 * ship_length:
                            far_from_other_ships = False
                            break
                    else:
                        if abs(row - ship_row) < 2 * length and abs(col - ship_col) < 2:
                            far_from_other_ships = False
                            break
                if far_from_other_ships:
                    break

    return row, col, orientation

def is_valid_guess(guess, size):
    if len(guess) != 2:
        return False
    row, col = guess
    return 1 <= row <= size and 1 <= col <= size

def is_grid_full(board, size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'O':
                return False
    return True

def battleship_game():
    print("Welcome to Battleship!")

    while True:
        try:
            size = int(input("Enter the grid size: "))
            if size >= 2:
                break
            else:
                print("The grid size must be at least 2. Please try again.")
        except ValueError:
            print("That's an invalid input. Please enter a valid grid size.")

    user_board = create_grid(size)
    computer_board = create_grid(size)

    place_option = input("Do you want to manually place your ships? (yes/no): ").lower()

    if place_option == 'yes':
        num_ships = int(input("How many ships do you want to place? "))
        user_ships = []
        for i in range(num_ships):
            ship_name = input(f"Enter the name for your Ship {i + 1}: ")
            while not ship_name.strip():
                print("Please enter a ship name.")
                ship_name = input(f"Enter the name for your Ship {i + 1}: ")

            while True:
                try:
                    length = int(input(f"Enter the length for {ship_name} (1 or 2): "))
                    if length in [1, 2]:
                        break
                    else:
                        print("Invalid ship length. Please choose either 1 or 2.")
                except ValueError:
                    print("Invalid input. Please enter a valid ship length.")

            user_row, user_col, orientation = place_ship_manually(user_board, size, length, ship_name)
            user_ships.append((user_row, user_col, length, orientation))  # Store the orientation as well
            if orientation == 'vertical':
                for i in range(length):
                    if i == 0:
                        user_board[user_row][user_col] = ship_name[0]
                    else:
                        if user_row + i < size:
                            user_board[user_row + i][user_col] = ship_name[0]
            else:
                for i in range(length):
                    if i == 0:
                        user_board[user_row][user_col] = ship_name[0]
                    else:
                        if user_col + i < size:
                            user_board[user_row][user_col + i] = ship_name[0]

    else:
        num_ships = random.randint(1, size // 2)
        user_ships = []
        for i in range(num_ships):
            ship_name = f"Ship {i + 1}"
            length = random.randint(1, 2)
            user_row, user_col, orientation = place_ship_randomly(user_board, size, length, user_ships)
            user_ships.append((user_row, user_col, length, orientation))  # Store the orientation as well
            if orientation == 'vertical':
                for i in range(length):
                    if i == 0:
                        user_board[user_row][user_col] = ship_name[0]
                    else:
                        if user_row + i < size:
                            user_board[user_row + i][user_col] = ship_name[0]
            else:
                for i in range(length):
                    if i == 0:
                        user_board[user_row][user_col] = ship_name[0]
                    else:
                        if user_col + i < size:
                            user_board[user_row][user_col + i] = ship_name[0]

    computer_ships = []
    for i in range(num_ships):
        ship_name = f"Opponent's Ship {i}"
        length = 2  # Opponent's ships will always have a length of 2
        computer_row, computer_col, orientation = place_ship_randomly(computer_board, size, length, computer_ships)
        computer_ships.append((computer_row, computer_col, length, orientation))  # Store the orientation as well
        if orientation == 'vertical':
            for i in range(length):
                if i == 0:
                    computer_board[computer_row][computer_col] = ship_name[0]
                else:
                    if computer_row + i < size:
                        computer_board[computer_row + i][computer_col] = ship_name[0]
        else:
            for i in range(length):
                if i == 0:
                    computer_board[computer_row][computer_col] = ship_name[0]
                else:
                    if computer_col + i < size:
                        computer_board[computer_row][computer_col + i] = ship_name[0]

    num_turns = 40  # Maximum number of turns = number of cells on the grid
    for turn in range(num_turns):
        print(f"\nTurn {turn + 1}:")
        if turn % 2 == 0:
            print("Your Board:")
            print_board(user_board, size, hidden=True)
            print("\nOpponent's Board:")
            print_board(computer_board, size, hidden=True)
        else:
            print("Your Board:")
            print_board(user_board, size, hidden=False)
            print("\nOpponent's Board:")
            print_board(computer_board, size, hidden=True)

        while True:
            try:
                row_guess = int(input(f"Enter the row index (1 to {size}): "))
                col_guess = int(input(f"Enter the column index (1 to {size}): "))
                if is_valid_guess((row_guess, col_guess), size):
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid row and column numbers.")

        row_guess -= 1
        col_guess -= 1

        if (row_guess, col_guess) == (computer_row, computer_col) or (row_guess, col_guess) == (computer_row + 1, computer_col) or (row_guess, col_guess) == (computer_row, computer_col + 1):
            ship_name = computer_board[computer_row][computer_col]
            print(f"Congratulations! You hit {ship_name}!")
            computer_board[row_guess][col_guess] = 'X'
        else:
            print("You missed!")
            computer_board[row_guess][col_guess] = '*'

        # Computer's turn
        computer_guess_row, computer_guess_col, computer_guess_orientation = place_ship_randomly(computer_board, size, 1, computer_ships)

        print("\nComputer's Guess:")
        if computer_guess_orientation == 'vertical':
            print(f"Row: {computer_guess_row + 1}, Column: {computer_guess_col + 1}")
        else:
            print(f"Row: {computer_guess_row + 1}, Column: {computer_guess_col + 1}, Orientation: {computer_guess_orientation.capitalize()}")

        if (computer_guess_row, computer_guess_col) == (user_row, user_col) or (computer_guess_row, computer_guess_col) == (user_row + 1, user_col) or (computer_guess_row, computer_guess_col) == (user_row, user_col + 1):
            ship_name = user_board[user_row][user_col]
            print(f"The opponent hit your {ship_name}!")
            user_board[computer_guess_row][computer_guess_col] = 'X'
        else:
            print("The opponent missed!")
            user_board[computer_guess_row][computer_guess_col] = '*'

        # Check if the grid is full
        if is_grid_full(user_board, size) or is_grid_full(computer_board, size):
            print("Game over! The grid is full.")
            break

    else:
        print("Game over! You've used all your turns.")

    print("\nFinal Board:")
    print("Your Board:")
    print_board(user_board, size, hidden=False)
    print("\nOpponent's Board:")
    print_board(computer_board, size, hidden=True)

    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input == 'yes':
        battleship_game()
    else:
        print("Thanks for playing Battleship!")

battleship_game()
