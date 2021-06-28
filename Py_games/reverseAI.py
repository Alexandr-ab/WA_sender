import random
from math import floor
from os import system
from time import sleep

width = 8
height = 8

def drawBoard(board):
    # draw game board which was sent to this function. Don't return nothing
    print('  ', end='')
    for i in range(width):
        if i < 10:
            print('  ' + str(i + 1), end='')
        else:
            print(' ' + str(i + 1), end='')
    print('\n  +' + ('-' * width * 3) + '+')
    for y in range(height):
        if y < 9:
            print(' ' + str(y + 1) + '|', end='')
            for x in range(width):
                print(board[x][y], end='')
            print('|' + str(y + 1) + ' ')
        else:
            print(str(y + 1) + '|', end='')
            for x in range(width):
                print(board[x][y], end='')
            print('|' + str(y + 1))
    print('  +' + ('-' * width * 3) + '+')
    print('  ', end='')
    for i in range(width):
        if i < 10:
            print('  ' + str(i + 1), end='')
        else:
            print(' ' + str(i + 1), end='')
    print()

def getNewBoard():
    # create clear new clear board
    board = []
    for i in range(width):
        board.append(['   '] * height)
    return board

def isOnBoard(x, y):
    # return True if coordinates is on board
    return 0 <= x <= width - 1 and 0 <= y <= height - 1

def isValidMove(board, tile, xstart, ystart):
    # return False if move to the spot with coordinate xstart and ystart is invalid
    # if it's valid - return list of spots that would become PC1's
    if board[xstart][ystart] != '   ' or not isOnBoard(xstart, ystart):
        return False
    if tile == ' X ':
        otherTile = ' O '
    else:
        otherTile = ' X '
    tilesToFlip = []
    nextToMove = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for xdir, ydir in nextToMove:
        x, y = xstart, ystart
        x += xdir # first step to x
        y += ydir # first step to y
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # continue to move this side
            x += xdir
            y += ydir
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original
                # space, noting all the tiles along the way.
                while True:
                    x -= xdir
                    y -= ydir
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    if len(tilesToFlip) == 0: # if none of pieces doesn't flip it's invalid move
        return False
    return tilesToFlip

def getBoardCopy(board):
    # make and return copy of a board
    boardCopy = getNewBoard()
    for x in range(width):
        for y in range(height):
            boardCopy[x][y] = board[x][y]
    return boardCopy

def getValidMoves(board, tile):
    # return list of a lists with x and y for valid moves
    validMoves = []
    for x in range(width):
        for y in range(height):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getBoardWithValidMoves(board, tile):
    # Return a new board with periods marking the valid moves the PC1 can make
    boardCopy = getBoardCopy(board)
    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = ' • '
    return boardCopy

def getScoreOfBoard(board):
    # get the score, after counting the tiles. Return dict with keys 'X' and 'O'
    xscore = 0
    oscore = 0
    for x in range(width):
        for y in range(height):
            if board[x][y] == ' X ':
                xscore += 1
            if board[x][y] == ' O ':
                oscore += 1
    return {' X ':xscore, ' O ':oscore}

def enterPC1Tile():
    # let PC1 enter choosed tile
    tile = [' O ', ' X ']
    random.shuffle(tile)
    return tile

def whoGoesFirst():
    # random chose who goes first
    if random.randint(0, 1) == 0:
        return 'PC'
    return 'PC1'

def makeMove(board, tile, xstart, ystart):
    # put the tile on the board in position xstart, ystart and flip tale of opponente
    # return False if move is invalid, True if valid
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def isOnCorner(x, y):
    # return True if position is on corner
    return (x == 0 or x == width - 1) and (y == 0 or y == height - 1)

def getPC1Move(board, PC1Tile):
    # let the PC1 enter his move
    # return move [x, y] (or return strings 'Hint' or 'Exit')
    if height > width:
        digits = [str(i) for i in range(1, height + 1)]
    else:
        digits = [str(i) for i in range(1, width + 1)]
    while True:
        move = input('Enter your move (\'e\' to exit, \'s\' to show hints or \'h\' to hide hints): ').lower()
        while move == '':
            move = input(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height}): ')
        if move in 'ehs':
            return move
        if width < 10 and height < 10:
            if len(move) == 3 and move[0] in digits and move[2] in digits:
                x = int(move[0]) - 1
                y = int(move[2]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            else:
                print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
        elif width >= 10 and height < 10:
            if len(move) == 3 and move[0] in digits and move[2] in digits:
                x = int(move[0]) - 1
                y = int(move[2]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            elif len(move) == 4 and move[:2] in digits and move[3] in digits:
                x = int(move[:2]) - 1
                y = int(move[3]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            else:
                print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
        elif width >= 10 and height >= 10:
            if len(move) == 3 and move[0] in digits and move[2] in digits:
                x = int(move[0]) - 1
                y = int(move[2]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            elif len(move) == 4 and move[:2] in digits and move[3] in digits:
                x = int(move[:2]) - 1
                y = int(move[3]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            elif len(move) == 4 and move[2:] in digits and move[0] in digits:
                x = int(move[0]) - 1
                y = int(move[2:]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            elif len(move) == 5 and move[:2] in digits and move[3:] in digits:
                x = int(move[:2]) - 1
                y = int(move[3:]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            else:
                print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
        elif width < 10 and height >= 10:
            if len(move) == 3 and move[0] in digits and move[2] in digits:
                x = int(move[0]) - 1
                y = int(move[2]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            elif len(move) == 4 and move[0] in digits and move[2:] in digits:
                x = int(move[0]) - 1
                y = int(move[2:]) - 1
                if isValidMove(board, PC1Tile, x, y) == False:
                    # print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
                    continue
                else:
                    break
            else:
                print(f'Invalid move. Please, enter collumn(1-{width}) and row(1-{height})')
    return [x, y]

def getComputerMove(board, computerTile):
    sleep(0.5)
    # check the board and PC's tile and decide where make a move, return list [x, y]
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # make random moves order
    # make a move on corner if it's possible
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
    # find a move with max score
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, PC1Tile, computerTile):
    scores = getScoreOfBoard(board)
    print(f'PC1 score: {scores[PC1Tile]}. PC2 score: {scores[computerTile]}')

def playGame(PC1Tile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(turn, 'goes first.')
    # clear game board and put starting tales
    board = getNewBoard()
    board[floor(width / 2) - 1][floor(height / 2) - 1] = ' X '
    board[floor(width / 2) - 1][floor(height / 2)] = ' O '
    board[floor(width / 2)][floor(height / 2) - 1] = ' O '
    board[floor(width / 2)][floor(height / 2)] = ' X '
    while True:
        PC1ValidMoves = getValidMoves(board, PC1Tile)
        computerValidMoves = getValidMoves(board, computerTile)
        if PC1ValidMoves == [] and computerValidMoves == []:
            return board # out of moves, end game
        elif turn == 'PC1': # PC1's move
            if PC1ValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, PC1Tile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, PC1Tile, computerTile)

                move = getComputerMove(board, PC1Tile)
                makeMove(board, PC1Tile, move[0], move[1])
                system('cls||clear')
            turn = 'PC'

        elif turn == 'PC': # pc's move
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, PC1Tile, computerTile)
                # input('Press \'Enter\' to see PC\'s move')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
                system('cls||clear')
            turn = 'PC1'

print('R E V E R S E')
PC1Tile, computerTile = enterPC1Tile()

while True:
    finalBoard = playGame(PC1Tile, computerTile)
    # show final score
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print(f'X score: {scores[" X "]}, O score: {scores[" O "]}')
    if scores[PC1Tile] > scores[computerTile]:
        print(f'PC1 beats PC2 by {scores[PC1Tile] - scores[computerTile]} points!')
    elif scores[PC1Tile] < scores[computerTile]:
        print(f'PC2 beats PC1 by {scores[computerTile] - scores[PC1Tile]} points!')
    else:
        print('DRAW!')
    print('Want to play more? (y/n):')
    if input().lower() != 'y':
        break