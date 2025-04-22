# File: board.py
from enums import PlayerSymbol
from exceptions import InvalidMoveException, PositionOccupiedException

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[PlayerSymbol.EMPTY for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(" | ".join(cell.value for cell in row))
            print("-" * (self.size * 4 - 1))

    def is_full(self):
        return all(cell != PlayerSymbol.EMPTY for row in self.grid for cell in row)

    def place_move(self, row, col, symbol):
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise InvalidMoveException("Move out of bounds.")
        if self.grid[row][col] != PlayerSymbol.EMPTY:
            raise PositionOccupiedException("Position already taken.")
        self.grid[row][col] = symbol

    def check_winner(self, symbol):
        # Check rows and columns
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True
        return False

