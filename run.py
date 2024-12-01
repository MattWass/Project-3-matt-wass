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
        