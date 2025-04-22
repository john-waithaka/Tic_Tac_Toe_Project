from enums import Player
from board import Board
from exceptions import InvalidMoveError, CellOccupiedError

class Game:
    def __init__(self, board_size=3):
        self.board = Board(board_size)
        self.current_player = Player.X
        self.winner = None

    def play_turn(self, row, col):
        try:
            self.board.mark_cell(row, col, self.current_player)
        except (InvalidMoveError, CellOccupiedError) as e:
            raise e

        if self.board.check_winner(self.current_player):
            self.winner = self.current_player
        elif self.board.is_full():
            self.winner = "Draw"
        else:
            self.current_player = self.current_player.other()

    def is_game_over(self):
        return self.winner is not None

    def get_winner(self):
        return self.winner
