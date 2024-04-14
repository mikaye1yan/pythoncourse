import random


def printGameboard(gameboard):
    for rows in gameboard:
        print(' | '.join(rows))
        print('-'*9)
def winnerCheck(gameboard, player):
    for rows in gameboard:
        if rows.count(player)==3:
            return True
    for columns in range(3):
         if all(gameboard[rows][columns] == player for rows in range(3)):
            return True
    if all(gameboard[i][i]==player for i in range(3)) or all(gameboard[i][2-i]==player for i in range(3)):
        return True
    return False
def game():
    gameboard=[[' ' for _ in range(3)] for _ in range(3)]
    players=['X', 'O']
    random.shuffle(players)
    rival=players[0]

    print('Start game')
    printGameboard(gameboard)

    for _ in range(9):

        while True:
            rows=int(input('Enter row (0,1,2):  '))
            columns=int(input('Enter columns (0,1,2):  '))
            if gameboard[rows][columns]== ' ':
                break
            print('Cell is taken, try again')

        gameboard[rows][columns]='X'
        printGameboard(gameboard)
        if winnerCheck(gameboard, 'X'):
            print('You win.')
            return
        
        while True:
            rivalRows=random.randint(0,2)
            rivalColumns=random.randint(0,2)
            if gameboard[rivalRows][rivalColumns]==' ':
                break

        gameboard[rivalRows][rivalColumns]='O'
        print("Rival player's move: ")
        printGameboard(gameboard)
        if winnerCheck(gameboard,'O'):
            print('You lost')
            return
    if all(cell!=' ' for rows in gameboard for cell in rows) and not winnerCheck(gameboard, 'X') and not winnerCheck(gameboard, 'O'):
        print('No one')
    else:
        print('No one')
game()