import random

# Function to create an empty grid of given size
def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Function to print the user's board
def print_user_board(grid, size):
    for row in grid:
        print(' '.join('X' if col == 'U' else col for col in row))

# Function to place a ship on the grid
def place_ship(grid, name, length, size):
    while True:
        try:
            row = int(input(f"Enter the row index for the {name} (1 to {size}): "))
            col = int(input(f"Enter the column index for the {name} (1 to {size}): "))
            if 1 <= row <= size and 1 <= col <= size:
                row -= 1
                col -= 1
                break
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")

    # Check if the ship fits on the grid
    if col + length > size:
        print("Invalid ship placement. Ship does not fit on the grid.")
        return False

    for i in range(length):
        if grid[row][col + i] != 'O':
            print("Invalid ship placement. Overlapping with another ship.")
            return False

    for i in range(length):
        grid[row][col + i] = name[0] + str(i + 1)

    return True

# Function to check if the guess is valid
def is_valid_guess(guess, size):
    if len(guess) != 2:
        return False
    row, col = guess
    return 0 <= row < size and 0 <= col < size

# Function to check if the guess hit a ship and if it was sunk
def check_hit_and_sunk(guess, ships):
    hit_ship = None
    hit_ship_index = None

    for i, ship in enumerate(ships):
        if guess in ship:
            hit_ship = ship
            hit_ship_index = i
            break

    if hit_ship:
        hit_ship.remove(guess)
        if not hit_ship:
            del ships[hit_ship_index]
            return "sunk", hit_ship_index
        else:
            return "hit", None
    else:
        return "miss", None

# Main function to run the game
def battleship_game():
    print("Welcome to Battleship!")

    while True:
        try:
            size = int(input("Enter the grid size (e.g., 5 for a 5x5 grid): "))
            if size >= 2:
                break
            else:
                print("Grid size must be at least 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid grid size.")

    user_grid = create_grid(size)
    opponent_grid = create_grid(size)

    print("Your board:")
    print_user_board(user_grid, size)

    num_ships = int(input("Enter the number of ships you want to place: "))
    user_ships = []

    for i in range(num_ships):
        name = input(f"Enter the name for Ship {i + 1}: ")
        while True:
            length = 2  # 2x1 ships
            if place_ship(user_grid, name, length, size):
                user_ships.append([(row, col + i) for i in range(length)])
                break

    opponent_ships = []
    num_opponent_ships = num_ships

    for i in range(num_opponent_ships):
        name = f"Ship{i + 1}"
        while True:
            length = 2  # 2x1 ships
            if place_ship(opponent_grid, name, length, size):
                opponent_ships.append([(row, col + i) for i in range(length)])
                break

    user_guesses = []
    opponent_guesses = []
    max_attempts = 8

    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1}: Your Turn")
        guess_str = input("Enter your guess (format: row col): ")
        guess_list = guess_str.strip().split()

        if len(guess_list) != 2:
            print("Invalid input. Please enter both row and column numbers.")
            continue

        try:
            guess_row = int(guess_list[0]) - 1
            guess_col = int(guess_list[1]) - 1
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
            continue

        guess = (guess_row, guess_col)

        if not is_valid_guess(guess, size):
            print(f"Invalid guess. Please enter numbers between 1 and {size}.")
            continue

        user_guesses.append(guess)

        result, sunk_index = check_hit_and_sunk(guess, opponent_ships)

        if result == "sunk":
            print(f"Congratulations! You sunk the opponent's {opponent_ships[sunk_index][0][0]}!")
        elif result == "hit":
            print("Congratulations! You hit an opponent's ship!")
        else:
            print("You missed! Try again.")
            user_grid[guess_row][guess_col] = '*'

        print("\nYour Board:")
        print_user_board(user_grid, size)

        print("\nOpponent's Board:")
        for row, col in opponent_guesses:
            opponent_grid[row][col] = 'X' if (row, col) in user_ships[sunk_index] else '*'
        print_user_board(opponent_grid, size)

        if not opponent_ships:
            print("Congratulations! You've sunk all the opponent's ships!")
            break

        print(f"\nAttempt {attempt + 1}: Opponent's Turn")
        opponent_guess_row = random.randint(0, size - 1)
        opponent_guess_col = random.randint(0, size - 1)
        opponent_guess = (opponent_guess_row, opponent_guess_col)

        opponent_guesses.append(opponent_guess)

        result, _ = check_hit_and_sunk(opponent_guess, user_ships)

        if result == "sunk":
            print("The opponent hit and sunk your ship!")
        elif result == "hit":
            print("The opponent hit your ship!")
        else:
            print("The opponent missed!")

    else:
        print("Game over! You've used all your attempts.")
        print("The remaining opponent's ships:")
        for ship in opponent_ships:
            print(f"{ship[0][0]}")

    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input == 'yes':
        battleship_game()
    else:
        print("Thanks for playing Battleship!")

# Run the game
battleship_game()
