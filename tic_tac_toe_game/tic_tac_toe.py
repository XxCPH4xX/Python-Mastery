"""Basic console Tic Tac Toe — smoke test to verify the environment runs."""

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def print_board(board):
    print()
    for row in range(3):
        cells = [board[row * 3 + col] for col in range(3)]
        print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("---+---+---")
    print()


def check_win(board, player):
    return any(
        all(board[pos] == player for pos in line) for line in WINNING_LINES
    )


def get_move(board, player):
    while True:
        choice = input(f"Player {player}, pick a square (1-9): ").strip()
        if not choice.isdigit():
            print("Please enter a number.")
            continue
        move = int(choice) - 1
        if not 0 <= move <= 8:
            print("That number is out of range (1-9).")
            continue
        if board[move] != " ":
            print("That square is already taken.")
            continue
        return move


def main():
    board = [" "] * 9
    player = "X"

    print("=== Tic Tac Toe ===")
    print("Squares are numbered 1-9, left to right, top to bottom.")

    for _ in range(9):
        print_board(board)
        move = get_move(board, player)
        board[move] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        player = "O" if player == "X" else "X"
    else:
        print_board(board)
        print("It's a draw!")


if __name__ == "__main__":
    main()
