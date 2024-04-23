import random


class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
    def print_board(self):
        for i in range(3):
            print(' | '.join(self.board[i*3:i*3+3]))
            if i < 2:
                print('-' * 9)
    def make_move(self, position, symbol):
        self.board[position] = symbol
    def is_valid_move(self, position):
        return self.board[position] == ' '
    def check_win(self, symbol):
        win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for condition in win_conditions:
            if all(self.board[pos] == symbol for pos in condition):
                return True
        return False
    def check_draw(self):
        return ' ' not in self.board
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    def __str__(self):
        return f"Player {self.symbol}"
class HumanPlayer(Player):
    def get_move(self):
        while True:
            try:
                move = int(input("Please enter your move (1-9): ")) - 1
                if 0 <= move <= 8:
                    return move
                else:
                    print("Invalid move, please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input, please try again.")

class ComputerPlayer(Player):
    def get_move(self, board):
        available_moves = [i for i, val in enumerate(board.board) if val == ' ']
        return random.choice(available_moves)
class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = random.choice(self.players)
    def switch_player(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]
    def play(self):
        print("Let's start the game!")
        while True:
            self.board.print_board()
            print(f"It's {self.current_player}'s turn.")
            move = self.current_player.get_move() if isinstance(self.current_player, HumanPlayer) else self.current_player.get_move(self.board)
            if self.board.is_valid_move(move):
                self.board.make_move(move, self.current_player.symbol)
                if self.board.check_win(self.current_player.symbol):
                    self.board.print_board()
                    print(f"{self.current_player} wins!")
                    break
                elif self.board.check_draw():
                    self.board.print_board()
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move, try again.")   
player1 = HumanPlayer('X')
player2 = ComputerPlayer('O')
game = TicTacToeGame(player1, player2)
game.play()