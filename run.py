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

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships")
            else:
                self.ships.append((x, y))
                if self.type == "player":
                    self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size -1)


def valid_coordinates(x, y, board):

def populate_board(board):

def make_guess(board):

def play_game(computer_board, player_board):

def new_game():
