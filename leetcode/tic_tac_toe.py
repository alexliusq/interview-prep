

class TicTacToe:

    TURN_TO_SYMBOL = ('X', 'O')

    def __init__(self, size) -> None:
        self.size = size
        self.pieces_remaining = self.size ** 2
        self.board = [['-' for _ in range(size)] for _ in range(size)]
        self.turn = 0 ## 0 for X, 1 for O, this way is easier to toggle
    
    def __str__(self):
        return '\n---BOARD---\n' + '\n'.join(
            ' | '.join(self.board[row]) for row in range(len(self.board))
            )
    
    def place_piece(self, row, col, symbol):
        if (not 0 <= row < self.size
            or not 0 <= col < self.size):
            return False 
        if not symbol:
            return False
        if self.board[row][col] != '-':
            return False
        self.board[row][col] = symbol
        self.pieces_remaining -= 1
        return True
    
    def play(self, play_computer = False):
        while self.pieces_remaining > 0:
            print(self)
            if play_computer and self.turn == 1:
                self.computer_play()
            else:
                row, col = self.get_user_input()
                while not self.place_piece(row, col, self.get_current_symbol()):
                    print(f'failed to place {self.get_current_symbol()} at {row}, {col}, please try again')
                    row, col = self.get_user_input()
            
            if self.win_check(self.get_current_symbol()):
                print(f'player {self.turn} has won!')
                break
            self.turn ^= 1

    def computer_play(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == '-':
                    print(f'\nAI MOVES TO {row},{col}')
                    self.place_piece(row, col, self.get_current_symbol())
                    return


    def get_current_symbol(self):
        return TicTacToe.TURN_TO_SYMBOL[self.turn]

    def get_user_input(self):
        print('')
        player_input = input(f'Player {self.turn} enter position to place {self.get_current_symbol()}: ')
        [row, col] = player_input.split()
        return (int(row), int(col))
    
    def win_check(self, symbol):
        row_win = self.win_check_rows(symbol)
        col_win = self.win_check_cols(symbol)
        diagonal_win = self.win_check_diagonals(symbol)
        return any([row_win, col_win, diagonal_win])
    
    def win_check_diagonals(self, symbol):
        n = self.size
        left_to_right = [self.board[i][i] for i in range(n)]
        right_to_left = [self.board[i][-1 - i] for i in range(n)]
        return self.win_check_arrays(symbol, [left_to_right, right_to_left])
    
    def win_check_rows(self, symbol):
        return self.win_check_arrays(symbol, self.board)

    def win_check_cols(self, symbol):
        cols_to_rows = zip(*self.board)
        return self.win_check_arrays(symbol, cols_to_rows)
    
    def win_check_arrays(self, symbol, arrays):
        for array in arrays:
            win = all(x == symbol for x in array)
            if win:
                return True
        return False

game = TicTacToe(3)
game.play(play_computer=True)

def test_row():
    game = TicTacToe(3)
    game.place_piece(0,0,'X')
    game.place_piece(0,1,'X')
    game.place_piece(0,2,'X')
    print(game)
    print(game.win_check('X'))

def test_diag():
    game = TicTacToe(3)
    game.place_piece(0,2, 'X')
    game.place_piece(1,1, 'X')
    print(game)
    print(game.win_check('X'))
    game.place_piece(2,0, 'X')
    print(game)
    print(game.win_check('X'))
