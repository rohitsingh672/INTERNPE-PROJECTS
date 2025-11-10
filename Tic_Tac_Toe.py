# Create an empty board
board = [" " for _ in range(9)]
# Function to print the board
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")
# Function to check win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
        ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
# Function to check draw
def check_draw():
    return " " not in board
# Main game function
def play_game():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Choose a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That spot is already taken. Try again.")
                continue
            board[move] = current_player
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
# Start the game
if __name__ == "__main__":
    play_game()
