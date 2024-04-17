import random

class TicTacToe:
    def __init__(self):
        self.gameboard = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']
        random.shuffle(self.players)
        self.current_player = self.players[0]

    def print_gameboard(self):
        for row in self.gameboard:
            print(' | '.join(row))
            print('-' * 9)

    def winner_check(self, player):
        for row in self.gameboard:
            if row.count(player) == 3:
                return True
        for col in range(3):
            if all(self.gameboard[row][col] == player for row in range(3)):
                return True
        if all(self.gameboard[i][i] == player for i in range(3)) or all(self.gameboard[i][2 - i] == player for i in range(3)):
            return True
        return False

    def play(self):
        print('Start game')
        self.print_gameboard()

        for _ in range(9):
            while True:
                row = int(input('Enter row (0, 1, 2): '))
                col = int(input('Enter column (0, 1, 2): '))
                if self.gameboard[row][col] == ' ':
                    break
                print('Cell is taken, try again')

            self.gameboard[row][col] = self.current_player
            self.print_gameboard()

            if self.winner_check(self.current_player):
                print('You win.')
                return

            while True:
                rival_row = random.randint(0, 2)
                rival_col = random.randint(0, 2)
                if self.gameboard[rival_row][rival_col] == ' ':
                    break

            self.gameboard[rival_row][rival_col] = 'O'
            print("Rival player's move: ")
            self.print_gameboard()

            if self.winner_check('O'):
                print('You lost')
                return

        if all(cell != ' ' for row in self.gameboard for cell in row) and not self.winner_check('X') and not self.winner_check('O'):
            print('Draw')
        else:
            print('No one wins')

game = TicTacToe()
game.play()