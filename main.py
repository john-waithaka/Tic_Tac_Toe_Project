from game import Game
from utils import get_move_input
from exceptions import InvalidMoveError, CellOccupiedError

def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        try:
            size = int(input("Choose board size (3-8): "))
            game = Game(size)
            break
        except Exception as e:
            print(f"Error: {e}")

    while not game.is_game_over():
        game.board.display()
        print(f"Player {game.current_player.value}'s turn.")
        row, col = get_move_input(game.board.size)
        try:
            game.play_turn(row, col)
        except CellOccupiedError as e:
            print(e)

    game.board.display()
    if game.get_winner() == "Draw":
        print("It's a draw!")
    else:
        print(f"Player {game.get_winner().value} wins!")

if __name__ == "__main__":
    main()
