def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score

    best_score = 100
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, True)
                board[i][j] = ' '
                best_score = min(best_score, score)
    return best_score


def best_move(board):
    best_score = -100
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print('You are X and the computer is O.')

    while True:
        print_board(board)
        row = int(input('Enter row (0-2): '))
        col = int(input('Enter column (0-2): '))

        if board[row][col] != ' ':
            print('That move is not valid. Try again.')
            continue

        board[row][col] = 'X'
        if check_winner(board) == 'X':
            print_board(board)
            print('You win!')
            break
        if is_full(board):
            print_board(board)
            print('Draw!')
            break

        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'

        if check_winner(board) == 'O':
            print_board(board)
            print('Computer wins!')
            break
        if is_full(board):
            print_board(board)
            print('Draw!')
            break


play_game()
