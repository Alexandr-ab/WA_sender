import time
from os import system
import HangmanWords
from random import randint
from termcolor import colored

def drawHangman(hangman):
    for i in hangman:
        print(colored(i, 'blue'))

while True:
    hangman = ['  ---------', '  |        |', '           |', '           |',
               '           |', '           |', '           |', '   ------------']
    hangman1 = ['  ---------', '  |        |', '  0        |', '           |',
                '           |', '           |', '           |', '   ------------']
    hangman2 = ['  ---------', '  |        |', '  0        |', '  |        |',
                '  |        |', '           |', '           |', '   ------------']
    hangman3 = ['  ---------', '  |        |', '  0        |', ' /|\       |',
                '  |        |', '           |', '           |', '   ------------']
    hangman4 = ['  ---------', '  |        |', '  0        |', ' /|\       |',
                '  |        |', ' / \       |', '           |', '   ------------', colored('GAME OVER', 'red')]
    hangList = [hangman1, hangman2, hangman3, hangman4]

    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    while True:
        who = int(input('1 - Human\n2 - Machine\n'))
        if who == 1:
            word = list(input('Enter your word:\n').upper())
            time.sleep(1)
            break
        elif who == 2:
            level = input('Choose your level:\n'
                          '1. Easy (5 letters word)\n'
                          '2. Medium (8 letters word)\n'
                          '3. Hard (12 letters word)\n'
                          '4. Xtreme\n')
            if level == '1':
                x = randint(0, len(HangmanWords.easy) - 1)
                choosedWord = HangmanWords.easy[x].upper()
                word = list(choosedWord)
                break
            elif level == '2':
                x = randint(0, len(HangmanWords.medium) - 1)
                choosedWord = HangmanWords.medium[x].upper()
                word = list(choosedWord)
                break
            elif level == '3':
                x = randint(0, len(HangmanWords.hard) - 1)
                choosedWord = HangmanWords.hard[x].upper()
                word = list(choosedWord)
                break
            elif level == '4':
                x = randint(0, len(HangmanWords.extreme) - 1)
                choosedWord = HangmanWords.extreme[x].upper()
                word = list(choosedWord)
                break
            else:
                print(colored('Wrong choise', 'red'))
        else:
            print(colored('Wrong choise', 'red'))

    wordSec = ['_'] * len(word)
    space = ' '

    if space in word:
        for i, d in enumerate(word):
            if d == space:
                wordSec[i] = space

    wordString = ''.join(wordSec).upper()
    counter = 0

    while counter < 4:
        if wordSec == word:
            break
        else:
            alphabetStr = '  '.join(alphabet).upper()
            system('cls||clear')
            drawHangman(hangman)
            print(wordString)
            print(colored(alphabetStr, 'green'))
            # print(word)
            letter = input('Enter your letter: ').upper()
            if letter in alphabet:
                index = alphabet.index(letter)
                alphabet[index] = '_'

            if letter in word:
                for i, d in enumerate(word):
                    if d == letter:
                        wordSec[i] = letter
                        wordString = ''.join(wordSec).upper()
            else:
                hangman = hangList[counter]
                counter += 1

    system('cls||clear')

    if counter == 4:
        drawHangman(hangman4)
    elif counter == 0:
        hangman.append(colored('YOU WON', 'yellow'))
        drawHangman(hangman)
        print(wordString)
    else:
        currentHangman = hangList[counter - 1]
        currentHangman.append(colored('YOU WON', 'yellow'))
        drawHangman(currentHangman)
        print(wordString)

    while True:
        wannaMore = input('Want to play more? (y/n): ').lower()
        if wannaMore not in 'yn':
            print('Please, choose y or n')
        elif wannaMore == 'y':
            break
        else:
            exit()


