
import random

def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]

def print_board(grid, size):
    for row in grid:
        print(' '.join('X' if col == 'U' else col for col in row))

def place_ship(grid, name, length, size, row, col, orientation):
    if orientation == 'horizontal':
        if 1 <= row <= size and 1 <= col + length <= size:
            row -= 1
            col -= 1
        else:
            print("That's an invalid ship placement. The ship does not fit on the grid.")
            return False

        for i in range(length):
            if grid[row][col + i] != 'O':
                print("That's an invalid ship placement. It's overlapping with another ship.")
                return False

        for i in range(length):
            grid[row][col + i] = name[0] + str(i + 1)

    elif orientation == 'vertical':
        if 1 <= row + length <= size and 1 <= col <= size:
            row -= 1
            col -= 1
        else:
            print("That's an invalid ship placement. The ship does not fit on the grid.")
            return False

        for i in range(length):
            if grid[row + i][col] != 'O':
                print("That's an invalid ship placement. It's overlapping with another ship.")
                return False

        for i in range(length):
            grid[row + i][col] = name[0] + str(i + 1)

    else:
        print("Invalid orientation. Please choose 'horizontal' or 'vertical'.")
        return False

    return True

def randomly_place_ships(grid, num_ships, size):
    for i in range(num_ships):
        name = f"Ship{i + 1}"
        while True:
            length = 2  # 2x1 ships
            row = random.randint(1, size)
            col = random.randint(1, size)
            orientation = random.choice(['horizontal', 'vertical'])
            if place_ship(grid, name, length, size, row, col, orientation):
                break

def computer_guess(user_ships, size):
    while True:
        guess_row = random.randint(0, size - 1)
        guess_col = random.randint(0, size - 1)
        guess = (guess_row, guess_col)

        if guess not in user_ships:
            return guess

def is_valid_guess(guess_str, size):
    guess_list = guess_str.strip().split()
    if len(guess_list) != 2:
        return False
    try:
        guess_row, guess_col = int(guess_list[0]), int(guess_list[1])
        return 1 <= guess_row <= size and 1 <= guess_col <= size
    except ValueError:
        return False

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

def battleship_game():
    print("Welcome to Battleship! Let's Play !!")

    while True:
        try:
            size = int(input("Please enter the grid size: "))
            if size >= 2:
                break
            else:
                print("Your grid size must be at least 2. Please try again.")
        except ValueError:
            print("That's an invalid input. Please enter a valid grid size.")

    user_grid = create_grid(size)
    opponent_grid = create_grid(size)

    print("Your board:")
    print_board(user_grid, size)

    place_option = input("Do you want to manually enter your ships? (yes/no): ").lower()

    num_ships = int(input("Please enter the number of ships you want to place: "))

    if place_option == 'yes':
        for i in range(num_ships):
            name = input(f"Please enter the name for ship {i + 1}: ")
            while True:
                while True:
                    try:
                        length = int(input(f"Please enter the length for the {name} (1 or 2): "))
                        if length in [1, 2]:
                            break
                        else:
                            print("Invalid ship length. Please choose either 1 or 2.")
                    except ValueError:
                        print("Invalid input. Please enter a valid ship length.")

                while True:
                    orientation = input(f"Please enter the orientation for the {name} (horizontal/vertical): ").lower()
                    if orientation in ['horizontal', 'vertical']:
                        break
                    else:
                        print("Invalid orientation. Please choose 'horizontal' or 'vertical'.")

                row = int(input(f"Please enter the row index for the {name} (1 to {size}): "))
                col = int(input(f"Please enter the column index for the {name} (1 to {size}): "))
                if place_ship(user_grid, name, length, size, row, col, orientation):
                    break
    else:
        randomly_place_ships(user_grid, num_ships, size)

    randomly_place_ships(opponent_grid, num_ships, size)
    user_ships = {(i, j) for i in range(size) for j in range(size) if user_grid[i][j] != 'O'}

    user_guesses = []
    opponent_guesses = []
    max_attempts = 6

    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1}: Your Turn")
        guess_str = input("Please enter your guess (format: row col): ")

        if not is_valid_guess(guess_str, size):
            print("That's an invalid input. Please enter both row and column numbers between 1 and {size}.")
            continue

        guess_list = guess_str.strip().split()
        guess_row, guess_col = int(guess_list[0]) - 1, int(guess_list[1]) - 1
        guess = (guess_row, guess_col)

        user_guesses.append(guess)

        result, sunk_index = check_hit_and_sunk(guess, opponent_grid)

        if result == "sunk":
            print(f"Congratulations! You sunk the opponent's {opponent_grid[sunk_index[0]][sunk_index[1]]}!")
        elif result == "hit":
            print("Congratulations! You hit an opponent's ship!")
        else:
            print("You missed! Please try again.")
            opponent_grid[guess_row][guess_col] = '*'

        print("\nYour Board:")
        print_board(user_grid, size)

        print("\nOpponent's Board:")
        print_board(opponent_grid, size)

        if not any('O' in row for row in opponent_grid):
            print("Congratulations! You've sunk all the opponent's ships!")
            break

        print(f"\nAttempt {attempt + 1}: Opponent's Turn")
        computer_guess_location = computer_guess(user_ships, size)
        computer_guess_result, _ = check_hit_and_sunk(computer_guess_location, user_grid)

        if computer_guess_result == "sunk":
            print(f"The opponent hit and sunk your ship at {computer_guess_location}!")
        elif computer_guess_result == "hit":
            print(f"The opponent hit your ship at {computer_guess_location}!")
        else:
            print(f"The opponent missed at {computer_guess_location}!")

        opponent_guesses.append(computer_guess_location)

    else:
        print("Game over! You've used all your attempts.")
        print("The remaining opponent's ships:")
        for i, row in enumerate(opponent_grid):
            for j, col in enumerate(row):
                if col != 'O':
                    print(f"{col} at ({i+1}, {j+1})")

    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input == 'yes':
        battleship_game()
    else:
        print("Thanks for playing Battleship!")

# Run the game
battleship_game()
battleship_game()
