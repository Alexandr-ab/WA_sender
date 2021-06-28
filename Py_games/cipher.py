# Cesar cipher
from termcolor import colored

SYMBOLS = ''.join(chr(i) for i in range(32, 127))

def getMode():
    while True:
        print('Do you want to encrypt or decrypt or hack? (e/d/h)')
        mode = input().lower()
        if mode in 'edh':
            return mode[0]
        else:
            print('Enter \'e\' for encrypt or \'d\' for decrypt or \'h\' for hack')

def getMessage():
    return input('Enter your message: ')

def getKey():
    while True:
        key = int(input(f'Enter the key (1-{len(SYMBOLS)}): '))
        if 1 <= key <= len(SYMBOLS):
            return key

def getTranslatedMessage(mode, message, key):
    if mode == 'd':
        key = -key
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # symbol was not found in SYMBOLS
            # just add this symbol without changes
            translated += symbol
        else:
            # encrypt or decrypt
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
    return colored(translated, 'red')

def wannaMore():
    while True:
        answer = input('Try again? (y/n): ')
        if answer in 'yn':
            return answer[0]

while True:
    mode = getMode()
    message = getMessage()
    if mode == 'h':
        for key in range(1, len(SYMBOLS) + 1):
            print(key, getTranslatedMessage('d', message, key))
    else:
        key = getKey()
        if mode == 'e':
            print('Encrypted text:', end=' ')
        else:
            print('Decrypted text:', end=' ')
        print(getTranslatedMessage(mode, message, key))
    if wannaMore() == 'n':
        exit()