from enums import Player
from exceptions import InvalidMoveError, CellOccupiedError

class Cell:
    def __init__(self):
        self.owner = None

    def mark(self, player):
        if self.owner is not None:
            raise CellOccupiedError("Cell is already occupied.")
        self.owner = player

    def __str__(self):
        return self.owner.value if self.owner else " "

class Board:
    def __init__(self, size=3):
        if size < 3 or size > 8:
            raise InvalidMoveError("Board size must be between 3 and 8.")
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]

    def mark_cell(self, row, col, player):
        self.grid[row][col].mark(player)

    def check_winner(self, player):
        # Check rows
        for row in self.grid:
            if all(cell.owner == player for cell in row):
                return True
        # Check columns
        for col in range(self.size):
            if all(self.grid[row][col].owner == player for row in range(self.size)):
                return True
        # Diagonal top-left to bottom-right
        if all(self.grid[i][i].owner == player for i in range(self.size)):
            return True
        # Diagonal top-right to bottom-left
        if all(self.grid[i][self.size - 1 - i].owner == player for i in range(self.size)):
            return True
        return False

    def is_full(self):
        return all(cell.owner is not None for row in self.grid for cell in row)

    def display(self):
        print("\nCurrent Board:")
        for i, row in enumerate(self.grid):
            print(" | ".join(str(cell) for cell in row))
            if i < self.size - 1:
                print("-" * (self.size * 4 - 3))
