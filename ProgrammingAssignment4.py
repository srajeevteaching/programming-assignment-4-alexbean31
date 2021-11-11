# Programmers: Alex Bean
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: If the user would like another card to add to their hand
# Program Outputs: Users and dealers hands and the total card value, then telling the user if they win lose or tie

import random

def shuffled_deck():
    i = 1
    deck = []

# Use while loop for diamond cards
    while i < 14:
        CardNumber = str(i)
        deck.append(CardNumber + "d")
        i += 1
    i = 1

# Use while loop heart cards
    while i < 14:
        CardNumber = str(i)
        deck.append(CardNumber + 'h')
        i += 1
    i = 1

# Use while loop for spade cards
    while i < 14:
        CardNumber = str(i)
        deck.append(CardNumber + 's')
        i += 1
    i = 1

# Use while loop for club cards
    while i < 14:
        CardNumber = str(i)
        deck.append(CardNumber + 'c')
        i += 1

# Shuffle deck and return deck
    random.shuffle(deck)
    return deck

def CardNaming(Card):
    global CardSuit
    if Card[-1] == 'd':
        CardSuit = "Diamonds"
    elif Card[-1] == 'h':
        CardSuit = "Hearts"
    elif Card[-1] == 's':
        CardSuit = "Spades"
    elif Card[-1] == 'c':
        CardSuit = "Clubs"

# Add suit and number/name of card together and return
    CardNum = CardNumber(Card)
    CardName = "The "+CardNum+' of ' + CardSuit
    return CardName

def CardNumber(card):
    if int(card[0:len(card)-1]) == 11:
            CardNum = 'Jack'
    elif int(card[0:len(card)-1]) == 12:
            CardNum = 'Queen'
    elif int(card[0:len(card)-1]) == 13:
            CardNum = "King"
    elif int(card[0:len(card)-1]) == 1:
            CardNum = "Ace"
    else:
        CardNum = card[0:len(card)-1]
    return CardNum

def printHand(HandOfCards):
    CardName = []
    for Cards in HandOfCards:
        CardName.append(CardNaming(Cards))
    return CardName

def HandValue(HandOfCards):
    sum = 0

# For loop giving the correct value to the users hand
    for Cards in HandOfCards:
        if int(Cards[0:len(Cards) - 1]) > 10:
            sum += 10
        elif int(Cards[0:len(Cards) - 1]) == 1:
            sum += 11
        else:
            sum += int(Cards[0:len(Cards) - 1])
    return sum

def askForNewCard():
    wantCard = input("Would you like another card? (yes or no)")
    wantCard = wantCard.strip().lower()
    while not(wantCard == 'yes' or wantCard == 'no'):
        print("Input invalid")
        wantCard = input("Would you like another card? (yes or no)")
        wantCard.strip().lower()
    return wantCard

# A main function established for program to run
def main():

# Shuffle deck and give user two cards
    deck = shuffled_deck()
    HandOfCards = deck[0:2]
# Tell the user the game they are playing, what is in their hand and the value corresponding to that hand
    print("You are playing blackjack.")
    print("Your hand is ", printHand(HandOfCards))
    print("The value of your hand is ", HandValue(HandOfCards))
    wantCard = askForNewCard()
    i = 1

# While loop adding cards to the users hand if they want it
    while not(wantCard == "no"):
        HandOfCards.append(deck[i + 1])
        print("Your hand is", printHand(HandOfCards))
        print("The value of your hand is", HandValue(HandOfCards))
        wantCard = askForNewCard()
        i += 1

        if int(HandValue(HandOfCards)) > 21:
            wantCard = "No"
    j = 1
    dealerHand = []
# While loop adding cards to dealers hand. Will only take cards if their hand has a value under 17
    while HandValue(dealerHand) < 17:
        dealerHand.append(deck[i+j+1])
        j += 1
# Print the users and dealers hands and the value of the dealers hand
    print("Your hand is ", printHand(HandOfCards))
    print("The dealers hand is ", printHand(dealerHand))
    print("The value of the dealer's hand is ", HandValue(dealerHand))
# If elif else statement deciding if the user won or lost
    if HandValue(HandOfCards) < HandValue(dealerHand) or HandValue(HandOfCards) > 21:
        print("I am sorry, but you lose.")
    elif HandValue(HandOfCards) > HandValue(dealerHand) or HandValue(dealerHand) > 21:
        print("Congratulations, you win!")
    else:
        print("You tied.")

main()