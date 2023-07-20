import random

# Function to create an empty grid of given size
def create_grid(size):
    return [['0' for _ in range(size)] for _ in range(size)]

# Function to print the user's board
def print_user_board(grid, size):
    for row in grid:
        print(' '.join('X' if col == 'X' else col for col in row))

# Function to place the user's battleship
def place_user_battleship(grid, size):
    while True:
        try:
            row = int(input(f"Please enter the row index for your battleship (0 to {size-1}): "))
            col = int(input(f"Please enter the column index for your battleship (0 to {size-1}): "))
            if 0 <= row < size and 0 <= col < size:
                break
            else:
                print("That's an invalid input. Please try again.")
        except ValueError:
            print("That's an invalid input. Please enter valid row and column numbers.")
    grid[row][col] = '*'
    return row, col

# Function to place the opponent's battleship randomly
def place_opponent_battleship(grid, size):
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    grid[row][col] = '-'
    return row, col

# Function to check if the guess is valid
def is_valid_guess(guess, size):
    if len(guess) != 2:
        return False
    row, col = guess
    return 0 <= row < size and 0 <= col < size

# Function to check if the guess hits the battleship
def is_hit(guess, battleship_row, battleship_col):
    return guess == (battleship_row, battleship_col)

# Main function to run the game
def battleship_game():
    print("Welcome to Battleship! Let's Play !!")

    while True:
        try:
            size = int(input("Please enter the grid size: "))
            if size >= 2:
                break
            else:
                print("The grid size must be at least 2. Try again.")
        except ValueError:
            print("That's an invalid input. Please enter a valid grid size.")

    play_again = True

    while play_again:
        user_grid = create_grid(size)
        opponent_grid = create_grid(size)

        print("Your board:")
        print_user_board(user_grid, size)

        user_place_battleship = input("Do you want to place your battleship manually? (yes/no): ").lower()

        if user_place_battleship == 'yes':
            user_battleship_row, user_battleship_col = place_user_battleship(user_grid, size)
        else:
            user_battleship_row, user_battleship_col = place_opponent_battleship(user_grid, size)

        opponent_battleship_row, opponent_battleship_col = place_opponent_battleship(opponent_grid, size)

        user_guesses = []
        opponent_guesses = []
        max_attempts = 8

        for attempt in range(max_attempts):
            print(f"\nAttempt {attempt + 1}: Your Turn")
            guess_str = input("Enter your guess (format: row col): ")
            guess_list = guess_str.strip().split()

            if len(guess_list) != 2:
                print("That's an invalid input. Please enter both row and column numbers.")
                continue

            try:
                guess_row = int(guess_list[0]) - 1
                guess_col = int(guess_list[1]) - 1
            except ValueError:
                print("That's an invalid input. Please enter valid row and column numbers.")
                continue

            guess = (guess_row, guess_col)

            if not is_valid_guess(guess, size):
                print(f"That's an invalid guess. Please enter numbers between 1 and {size}.")
                continue

            user_guesses.append(guess)

            if is_hit(guess, opponent_battleship_row, opponent_battleship_col):
                print("You sunk the opponent's battleship! Congrats!")
                user_grid[guess_row][guess_col] = '+'
                break
            else:
                print("You missed! Please try again.")
                user_grid[guess_row][guess_col] = '+'

            print("\nYour Board:")
            print_user_board(user_grid, size)

            if attempt == max_attempts - 1:
                print("Game over! You've used all your attempts.")
                print(f"The opponent's battleship was located at: ({opponent_battleship_row}, {opponent_battleship_col}).")
                break

            print(f"\nAttempt {attempt + 1}: Opponent's Turn")
            opponent_guess_row = random.randint(0, size - 1)
            opponent_guess_col = random.randint(0, size - 1)
            opponent_guess = (opponent_guess_row, opponent_guess_col)

            opponent_guesses.append(opponent_guess)

            if is_hit(opponent_guess, user_battleship_row, user_battleship_col):
                print("Oh No! The opponent hit your battleship!")
                opponent_grid[opponent_guess_row][opponent_guess_col] = '-'
            else:
                print("Phew! The opponent missed!")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

    print("Thank you for playing Battleship!")

# Run the game
battleship_game()
