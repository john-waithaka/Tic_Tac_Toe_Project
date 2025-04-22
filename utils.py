
import re

def get_move_input(board_size):
    while True:
        raw = input("Enter your move (row col): ").strip()

        # Accept formats like: "1 1", "1,1", "1-1"
        match = re.match(r"^\s*(\d+)[\s,.-]+(\d+)\s*$", raw)
        if not match:
            print("Invalid input. Please enter two numbers separated by space, comma, or dash.")
            continue

        row, col = map(int, match.groups())

        if 0 <= row < board_size and 0 <= col < board_size:
            return row, col
        else:
            print(f"Coordinates must be between 0 and {board_size - 1}")
