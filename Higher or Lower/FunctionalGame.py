#Higher or Lower
import random 

#Card Constants
SUIT_TUPLE = ('Spades', 'Diamond', 'Hearts', 'Clubs')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

print('''WEOLCOME TO HIGHER OR LOWER

You will have to choose whetehr the next card to be shown will be 
higher or lower than the current card.

Getting it right adds 20 points; get it wrong and you loose 15 points.
You have 50 points to start.''')

startingDeckList=[]

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue +1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print('')
    gameDeckList = shuffle(startingDeckList)

    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f'Starting card is: {currentCardRank} of {currentCardSuit}\n')

    for cardNumber in range (0, NCARDS):
        answer = input(f'Will the next card be higher or lower than the {currentCardRank} of {currentCardSuit}?\n 1 or 0')
        answer = answer.casefold

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print(f'Next card is {nextCardRank} of {nextCardSuit}')

        if answer == 1:
            if nextCardValue > currentCardValue:
                print('correct')
                score = score + 20
            else:
                score = score -15
                print('It was not higher.')
        elif answer == 0:
            if nextCardValue < currentCardValue:
                score = score +20
                print ('Well done correct')
            else:
                score = score - 15
                print('You go it wrong')

        print(f'Your socre is {score}\n')
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
    goAgain = input('To play again press ENTER or "q" to quit: ')
    
    if goAgain == "q":
        break
print('OK bye')