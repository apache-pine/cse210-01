# Tic Tac Toe Game
# CSE 210 W02 Prove: Developer - Solo Code Submission
# Kylar Sorensen


def main():
    total_moves = 0
    board = create_board()
    cur_player = "O"
    while not (is_winner(board, "X") or is_winner(board, "O") or board_full(board)):
        cur_player = next_player(cur_player)
        print_board(board)
        cur_move(cur_player, board)
    print_board(board)
        

def create_board():
    board = list(range(1,10))
    return board

def print_board(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")

def cur_move(cur_player, board):
    move = False
    while move == False:
        try:
            selection = int(input(f"Player {cur_player}, choose a square (1-9): "))
        except ValueError:
            print("Invalid input, please try again.")

        if selection < 1 or selection > 9:
            print("Invalid input, please try again.")
        elif board[selection - 1] == "X" or board[selection - 1] == "O":
            print("Box already filled. Please try again.")
        else:
            board[selection - 1] = cur_player
            move = True

def next_player(cur_player):
    if cur_player == "X":
        return "O"
    else:
        return "X"

def is_winner(board, letter):
    if (board[0] == letter and board[1] == letter and board[2] == letter) or \
        (board[3] == letter and board[4] == letter and board[5] == letter) or \
        (board[6] == letter and board[7] == letter and board[8] == letter) or \
        (board[0] == letter and board[3] == letter and board[6] == letter) or \
        (board[1] == letter and board[4] == letter and board[7] == letter) or \
        (board[2] == letter and board[5] == letter and board[8] == letter) or \
        (board[0] == letter and board[4] == letter and board[8] == letter) or \
        (board[2] == letter and board[4] == letter and board[6] == letter):
        print(f"\nCongratulations Player {letter}, you win!")
        return True
    return False


def board_full(board):
    for square in range(9):
        i = board[square]
        if i != "X" and i != "O":
            return False
    return True


if __name__ == "__main__":
    main()