import random
from termcolor import colored

num_digits = 3
max_guess = 10

def getSecretNum():
    # return string unique with lenght = num_digits
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def triedNumsList(triedNums, guess):
    # return string of tried numbers
    triedNums.append(colored(guess, 'green'))
    return ' '.join(triedNums)

def getHints(guess, secretNum):
    # return hint 'cold', 'warm', 'hot'
    if guess == secretNum:
        return 'You got it!'

    hints = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            hints.append(colored('Hot', 'red'))
        elif guess[i] in secretNum:
            hints.append(colored('Warm', 'yellow'))
    if len(hints) == 0:
        return 'Cold'
    hints.sort()
    return ' '.join(hints)

def isOnlyDigit(num):
    # return True if num is a string of digits, else - False
    if num == '':
        return False

    for i in num:
        if not i.isdigit():
            return False
    return True

print(colored(f'You should geuss {num_digits}-digit number.', 'blue'))
print(colored('I\'ll give you some hints.', 'blue'))
print(colored('\nif I say:    That means:', 'blue'))
print('Cold         None of the digits is correct.')
print(colored('Warm         One digit is correct but in the wrong position.', 'yellow'))
print(colored('Hot          One digit is correct and in the right position.', 'red'))

while True:
    triedNums = []
    secretNum = getSecretNum()
    print(colored(f'\nSo, I\'m thinking about the number. You have {max_guess} tries to get it.', 'blue'))
    guessesTaken = 1
    while guessesTaken <= max_guess:
        guess = ''
        while len(guess) != num_digits or not isOnlyDigit(guess):
            print(colored(f'You alredy tried: {" ".join(triedNums)}', 'blue'))
            print(colored(f'Try №{guessesTaken}:', 'blue'))
            guess = input()
            triedNumsList(triedNums, guess)
        print(getHints(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > max_guess:
            print(f'No more tries. My nubmer was {secretNum}')
    while True:
        wannaMore = input('Want to play more? (y/n): ').lower()
        if wannaMore not in 'yn':
            print('Please, choose y or n')
        elif wannaMore == 'y':
            break
        else:
            exit()