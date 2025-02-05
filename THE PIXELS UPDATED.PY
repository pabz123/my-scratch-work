
def create_board():
    return [" "] * 9

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])

def is_space_free(board, index):
    return board[index] == " "

def make_move(board, index, player):
    if is_space_free(board, index):
        board[index] = player
        return True
    return False

def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combination in winning_combinations:
        if all(board[index] == player for index in combination):
            return True
    return False

def play_tic_tac_toe():
    board = create_board()
    current_player = "X"
    while True:
        print_board(board)
        index = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if make_move(board, index, current_player):
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if all(space != " " for space in board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"

play_tic_tac_toe()