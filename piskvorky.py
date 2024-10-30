# Piškvorky v Pythonu

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    # Kontrola řádků a sloupců
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Kontrola diagonál
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f'Hráč {current_player}, zadejte řádek (0-2): '))
        col = int(input(f'Hráč {current_player}, zadejte sloupec (0-2): '))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Neplatné pole, zkuste to znovu.')
            continue

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f'Hráč {winner} vyhrál!')
                break
            elif is_full(board):
                print_board(board)
                print('Hra skončila remízou!')
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Toto pole je již obsazeno, zkuste to znovu.')

if __name__ == '__main__':
    main()
