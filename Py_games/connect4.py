from termcolor import colored

currentField = [['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '],
                ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '],
                ['   ', '   ', '   ', '   ', '   ', '   ']]

def drawField(field):
    print(colored('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |', 'yellow'))
    print(colored('-' * 29, 'yellow'))
    for row in range(12):
        if row % 2 == 0:
            for column in range(13):
                if column % 2 == 0:
                    if column == 0:
                        print(colored('|', 'blue')+field[int(column / 2)][int(row / 2)], end='')
                    elif column != 12:
                        print(field[int(column / 2)][int(row / 2)], end='')
                    else:
                        print(field[int(column / 2)][int(row / 2)]+colored('|', 'blue'))
                else:
                    print(colored('|', 'blue'), end='')
        else:
            print(colored('-' * 29, 'blue'))

drawField(currentField)

player = 1
def spotCheck():
    row = 5
    while row >= -1:
        if currentField[chooseColumn - 1][row] != '   ':
            row -= 1
        else:
            break
    return row


while True:
    print(colored(f'Players turn: {player}', 'magenta'))
    answer = input(colored('Please, choose the column: ', 'magenta'))
    if answer == 'exit':
        break
    else:
        chooseColumn = int(answer)
        if chooseColumn > 7 or chooseColumn < 1:
            print(colored('-' * 30, 'red'))
            print(colored('You choosed wrong column.', 'red'))
            print(colored('-' * 30, 'red'))
        elif answer == 'exit':
            break
        else:
            if player == 1:
                row = spotCheck()
                if row < 0:
                    print(colored('The column is full, please, choose another: ', 'red'))
                else:
                    currentField[chooseColumn - 1][row] = colored(' 0 ', 'red')
                    player = 2
            else:
                row = spotCheck()
                if row < 0:
                    print(colored('The column is full, please, choose another: ', 'red'))
                else:
                    currentField[chooseColumn - 1][row] = colored(' 0 ', 'green')
                    player = 1
        drawField(currentField)
