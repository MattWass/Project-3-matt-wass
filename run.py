from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Allows for better organization. Sets the board size,
    the amount of and placing ships, the player name and computer board types
    and updates in regards to hits or misses
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y):
        """Add a ship to the board."""
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add any more ships.")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    Check for valid coordinates for the placing of a battleship or making
    a guess.
    """
    if 0 <= x < board.size and 0 <= y < board.size:
        return True
    print("Invalid coordinates, please try again")
    return False


def populate_board(board):
    """
    Player to place battleships onto the board.
    """
    print(f"{board.name}, place your ships on the board:")
    while len(board.ships) < board.num_ships:
        remaining_ships = board.num_ships - len(board.ships)
        print(f"Ships remaining to place on board: {remaining_ships}")
        x = int(input("Enter x coordinate for your battleship (0-4): "))
        y = int(input("Enter y coordinate for your battleship (0-4): "))

        if valid_coordinates(x, y, board) and (x, y) not in board.ships:
            board.add_ship(x, y)
        else:
            print("This position is already taken or is invalid. Try again.")


def populate_computer_ships(board):
    """
    Computer places its ships randomly on the board.
    """
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)

        if (x, y) not in board.ships:
            board.add_ship(x, y)


def make_guess(board, is_computer_turn=False, x=None, y=None):
    """Allows the player or computer to make a guess, updating the board."""
    if is_computer_turn:
        x = random_point(board.size)
        y = random_point(board.size)
        print(f"Computer guesses {x}, {y}")
    else:
        while True:
            try:
                x = int(input("Enter x coordinate for your guess (0-4): "))
                y = int(input("Enter y coordinate for your guess (0-4): "))
                valid_coord = valid_coordinates(x, y, board)
                not_guessed = (x, y) not in board.guesses
                if valid_coord and not_guessed:
                    return board.guess(x, y)
                else:
                    print("Invalid or already guessed location. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 4.")

    return board.guess(x, y)


def play_game(computer_board, player_board):
    """
    Play game function, allowing alternate turns.
    """
    while True:
        print("\nPlayer's Turn:")
        player_board.print()
        result = make_guess(computer_board)
        print(result)

        if len(computer_board.ships) == 0:
            print("Player wins")
            break

        print("\nComputer's Turn:")
        comp_x = random_point(computer_board.size)
        comp_y = random_point(computer_board.size)
        result = player_board.guess(comp_x, comp_y)
        print(f"Computer guess {comp_x}, {comp_y}: {result}")

        if len(player_board.ships) == 0:
            print("Computer wins")
            break


def new_game():
    """
    Start of a new game. Setting of the board size and the number of ships,
    then resets the score sets the board in motion.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(" Welcome to Battleships!")
    print(f" Board Size: {size}. Number of ships: {num_ships}")
    print("The top left corner of the board is row: 0, col 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)

    populate_computer_ships(computer_board)

    play_game(computer_board, player_board)


new_game()

