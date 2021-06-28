from random import shuffle

def createDeck():
    deck = []
    faceValues = ['A', 'J', 'Q', 'K']
    for i in range(4):
        for card in range(2, 11):
            deck.append(str(card))
        for card in faceValues:
            deck.append(card)
    shuffle(deck)
    return deck

class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.setScore()
        self.money = float(money)
        self.bet = 0
    def __str__(self):
        currentHand = ''
        for card in self.hand:
            currentHand += str(card) + ' '
        finalStatus = currentHand + 'Score: ' + str(self.score)
        return finalStatus

    def setScore(self):
        self.score = 0
        faceCardsDict = {'A':11, 'J':10, 'Q':10, 'K':10}
        aceCounter = 0
        for card in self.hand:
            if card in faceCardsDict:
                self.score += faceCardsDict[card]
            else:
                self.score += int(card)
            if card == 'A':
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet
            else:
                self.money += 2 * self.bet
            self.bet = 0
            print(f'You won with {player1}. House {house}')
        else:
            self.bet = 0
            print(f'You lose with {player1}. House {house}')

    def draw(self):
        self.money += self.bet
        self.bet = 0
        print((f'Draw with {player1}. House {house}'))

    def has_black_jack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def printHouse(house):
    for card in range(len(house.hand)):
        if card == 0:
            print('*', end=' ')
        elif card == len(house.hand) - 1:
            print(house.hand[card])
        else:
            print(house.hand[card], end=' ')

cardDeck = createDeck()
firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
player1 = Player(firstHand)
house = Player(secondHand)

while True:
    if len(cardDeck) < 20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(), cardDeck.pop()]
    secondHand = [cardDeck.pop(), cardDeck.pop()]
    player1.play(firstHand)
    house.play(secondHand)
    bet = int(input(f'Please, enter your bet (You have {player1.money}): '))
    player1.bet_money(bet)
    printHouse(house)
    print(player1)

    if player1.has_black_jack():
        if house.has_black_jack():
            player1.draw()
        else:
            player1.win(True)
    elif house.has_black_jack():
        player1.win(False)
    else:
        while player1.score < 21:
            action = input('Do you want another cart? (y/n): ')
            if action == 'y':
                player1.hit(cardDeck.pop())
                printHouse(house)
                print(player1)
            else:
                break
        while house.score < 16:
            house.hit(cardDeck.pop())
        if player1.score > 21:
            if house.score > 21:
                player1.draw()
            else:
                player1.win(False)
        elif player1.score > house.score:
            player1.win(True)
        elif player1.score == house.score:
            player1.draw()
        else:
            if house.score > 21:
                player1.win(True)
            else:
                player1.win(False)

    print(player1.money)
