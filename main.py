# from game import Game
# from utils import get_move_input
# from exceptions import InvalidMoveError, CellOccupiedError

# def main():
#     print("Welcome to Tic Tac Toe!")
#     while True:
#         try:
#             size = int(input("Choose board size (3-8): "))
#             game = Game(size)
#             break
#         except Exception as e:
#             print(f"Error: {e}")

#     while not game.is_game_over():
#         game.board.display()
#         print(f"Player {game.current_player.value}'s turn.")
#         row, col = get_move_input(game.board.size)
#         try:
#             game.play_turn(row, col)
#         except CellOccupiedError as e:
#             print(e)

#     game.board.display()
#     if game.get_winner() == "Draw":
#         print("It's a draw!")
#     else:
#         print(f"Player {game.get_winner().value} wins!")

# if __name__ == "__main__":
#     main()



from db.database import init_db, login_user, register_user, update_win, get_wins
from game import Game
from exceptions import InvalidMoveException, PositionOccupiedException

def main():
    init_db()
    print("Welcome to Tic Tac Toe!")

    username = None
    while not username:
        choice = input("Do you want to (1) Login or (2) Register? ").strip()
        if choice == "1":
            username, password = input("Username: "), input("Password: ")
            if login_user(username, password):
                print(f"Welcome back, {username}!")
            else:
                print("Invalid login. Try again.")
                username = None
        elif choice == "2":
            username, password = input("Choose a username: "), input("Choose a password: ")
            if register_user(username, password):
                print(f"Account created. Welcome, {username}!")
            else:
                print("Username already taken.")
                username = None

    while True:
        result = play_game(username)
        if result == "X":
            print("You won!")
            update_win(username)
        elif result == "O":
            print("Computer won!")
        else:
            print("It's a draw.")

        wins = get_wins(username)
        print(f"{username} has {wins} win(s).")

        if input("Play again? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()


# # File: main.py
# from game import Game

# def main():
#     print("Welcome to Tic-Tac-Toe!")
#     game = Game(size=3)
#     winner = game.play()
#     if winner:
#         print(f"Congratulations! {winner.value} has won.")
#     else:
#         print("Game ended in a draw.")

# if __name__ == "__main__":
#     main()
