def print_board(board):
    ''' Use the loop to print the board '''
    for row in board:
        print(' | '.join(row))
        print('--*--*--')

def available_moves(board):
    ''' Return a list of available moves on the board '''
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

def player_moves(board, player, move):
    ''' Update the board with the player's move '''
    board[move[0]][move[1]] = player

def check_win(board, player):
    ''' Check if the player has won '''
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def check_tie(board):
    ''' Check if the game is a tie '''
    return all(board[i][j] != '' for i in range(3) for j in range(3))

def minimax(board, depth, maximizing_player):
    ''' Minimax algorithm for the Tic Tac Toe AI '''
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if check_tie(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            player_moves(board, 'O', move)
            eval = minimax(board, depth + 1, False)
            player_moves(board, '', move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            player_moves(board, 'X', move)
            eval = minimax(board, depth + 1, True)
            player_moves(board, '', move)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    ''' Find the best move for the computer using the Minimax algorithm '''
    best_val = float('-inf')
    best_move = None

    for move in available_moves(board):
        player_moves(board, 'O', move)
        move_val = minimax(board, 0, False)
        player_moves(board, '', move)

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move

def play_again():
    ''' Ask the player if they want to play again '''
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main_game():
    while True:
        board = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]
        print("Welcome to Tic Tac Toe!")

        # Player chooses 'X' or 'O'
        player_symbol = input("Choose 'X' or 'O': ").upper()
        if player_symbol not in ['X', 'O']:
            print("Invalid choice. Defaulting to 'X'.")
            player_symbol = 'X'

        computer_symbol = 'O' if player_symbol == 'X' else 'X'

        print(f"you are {player_symbol} and Computer is {computer_symbol}")
        print("The board is numbered from 1 to 9 as shown below:")
        print_board([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
        print("Start the game!")

        while True:
            print_board(board)

            # Player's move
            move = int(input("Enter a number from 1 to 9: ")) - 1
            row, col = divmod(move, 3)

            if board[row][col] == '':
                player_moves(board, player_symbol, (row, col))
            else:
                print("Blocked, choose another square.")
                continue

            if check_win(board, player_symbol):
                print_board(board)
                print("You win!")
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            # Computer's move
            computer_move = best_move(board)
            player_moves(board, computer_symbol, computer_move)

            if check_win(board, computer_symbol):
                print_board(board)
                print("Computer wins!")
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

        if not play_again():
            break

if __name__ == "__main__":
    main_game()
