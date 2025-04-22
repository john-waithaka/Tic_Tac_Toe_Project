from enum import Enum

class Player(Enum):
    X = "X"
    O = "O"

    def other(self):
        return Player.X if self == Player.O else Player.O
