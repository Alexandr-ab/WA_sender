from random import randint, choice
from time import sleep
from os import system

def draw_board(board): # function is showing game board
    # board - list of 10 strings for drawing game board
    # clear the screen
    system('cls||clear')
    print(' 7 | 8 | 9 ', '---+---+---', ' 4 | 5 | 6 ', '---+---+---', ' 1 | 2 | 3', '===========', sep='\n')
    print()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('---+---+---')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('---+---+---')
    print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter(): # player is choosing his letter
    # return list where player's letter is the first element and pc's letter is second element
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Choose X or O: ')
        letter = input().upper()
    #first element is player's lettet, second - pc's
    if letter == 'X':
        return [' X ', ' O ']
    else:
        return [' O ', ' X ']

def who_goes_first(): # random choice who goes first
    if randint(0, 1) == 0:
        return 'PC'
    else:
        return 'Player'

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le): # return True if player won
    # bo = board, le = letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # accross the center
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # top to bottom by left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # top to bottom by center
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # top to bottom by right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonally
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonally

def get_board_copy(board): # function makes board copy and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def is_space_free(board, move): # return True if move was made in free space
    return board[move] == '   '

def get_player_move(board):
    move = ' '
    while move not in '123456789' or not is_space_free(board, int(move)):
        move = input('your move (1-9): ')
    return int(move)

def choose_random_move_from_list(board, moveList): # return available moves list
    # return None if no more available moves
    possibleMoves = []
    for i in moveList:
        if is_space_free(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return choice(possibleMoves)
    else:
        return

def get_pc_move(board, computerLetter): # choose available move and return it
    if computerLetter == ' X ':
        playerLetter = ' O '
    else:
        playerLetter = ' X '

    # PC algoritm:
    # first check - would pc won if makes next move
    for i in range(1, 10):
        boardCopy = get_board_copy(board)
        if is_space_free(boardCopy, i):
            make_move(boardCopy, computerLetter, i)
            if is_winner(boardCopy, computerLetter):
                return i
    # second check - would player won if makes next move, and block it
    for i in range(1, 10):
        boardCopy = get_board_copy(board)
        if is_space_free(boardCopy, i):
            make_move(boardCopy, playerLetter, i)
            if is_winner(boardCopy, playerLetter):
                return i
    # choose one of corners if it's free
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    # choose center if it's free
    if is_space_free(board, 5):
        return 5
    # make a move by one of the sides
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board): # return True if space is full, else - False
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

while True:
    # clear the screen
    system('cls||clear')

    # load game board
    theBoard = ['   '] * 10
    playerLetter, computerLetter = input_player_letter()
    turn = who_goes_first()
    print(turn, 'makes his move first.')
    sleep(2)
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Player':
            # players move
            draw_board(theBoard)
            move = get_player_move(theBoard)
            make_move(theBoard, playerLetter, move)
            if is_winner(theBoard, playerLetter):
                draw_board(theBoard)
                print('Congratulations! You won!')
                gameIsPlaying = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('Draw')
                    break
                else:
                    turn = 'PC'
        else:
            # PC move
            move = get_pc_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)
            if is_winner(theBoard,computerLetter):
                draw_board(theBoard)
                print('Computer won! You lose')
                gameIsPlaying = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('Draw')
                    break
                else:
                    turn = 'Player'
    while True:
        wannaMore = input('Want to play more? (y/n): ').lower()
        if wannaMore not in 'yn':
            print('Please, choose y or n')
        elif wannaMore == 'y':
            break
        else:
            exit()
