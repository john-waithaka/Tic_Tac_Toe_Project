# File: game.py
from board import Board
from enums import PlayerSymbol
from exceptions import InvalidMoveException, PositionOccupiedException
import random

class Game:
    def __init__(self, size=3):
        self.board = Board(size)

    def get_human_move(self):
        while True:
            move_input = input("Enter your move (row col): ")
            try:
                row, col = map(int, move_input.strip().split())
                return row, col
            except ValueError:
                print("Invalid input. Please enter two integers.")

    def get_computer_move(self):
        size = self.board.size
        while True:
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
            if self.board.grid[row][col] == PlayerSymbol.EMPTY:
                return row, col

    def play(self):
        current_symbol = PlayerSymbol.HUMAN
        while True:
            self.board.display()
            if current_symbol == PlayerSymbol.HUMAN:
                row, col = self.get_human_move()
            else:
                row, col = self.get_computer_move()

            try:
                self.board.place_move(row, col, current_symbol)
            except (InvalidMoveException, PositionOccupiedException) as e:
                print(e)
                continue

            if self.board.check_winner(current_symbol):
                self.board.display()
                print(f"{current_symbol.value} wins!")
                return current_symbol

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                return None

            current_symbol = PlayerSymbol.COMPUTER if current_symbol == PlayerSymbol.HUMAN else PlayerSymbol.HUMAN