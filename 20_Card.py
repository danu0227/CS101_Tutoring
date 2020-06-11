import random
import time

faces = list(range(2,11))+['Jack', 'Queen', 'King', 'Ace']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class Card:
    """Cards"""
    def __init__(self, face, suit):
        assert face in faces and suit in suits
        self.face = face
        self.suit = suit
        self.picked = False
    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10
    def __str__(self):
        article = 'a '
        if self.face in [8, 'Ace']:
            article = 'an '
        return (article + str(self.face) + " of " + self.suit)

class Deck:
    """A deck of cards"""
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(face, suit))
    def shuffle(self):
        random.shuffle(self.cards)

print("==========ENJOY CARD GAME===========\n")
play = "Y"
while play == "Y" or play == "y":
    print("===========GAME START!!!============")
    deck = Deck()
    deck.shuffle()
    a = [0, 0, 0, 0, 0]
    b = ["1st", "2nd", "3rd", "4th", "5th"]
    integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for i in range(5):
        while True:
            ask = "choose "+b[i]+" card(integer between 1 to 10): "
            a[i] = input(ask)
            if a[i] in integers:
                if deck.cards[int(a[i])-1].picked:
                    print("YOU ALREADY CHOOSED", a[i],"!!!")
                    continue
                deck.cards[int(a[i])-1].picked = True
                print(deck.cards[int(a[i])-1], "has value", deck.cards[int(a[i])-1].value())
                break
            print("WRONG INPUT!!")

    print("your cards:")
    your = 0
    for i in range(10):
        if deck.cards[i].picked:
            print("   ", deck.cards[i], "-> value:", deck.cards[i].value())
            time.sleep(0.5)
            your += deck.cards[i].value()
    print("YOUR SCORE:", your)
    print("\n\n")

    print("COMPUTER's CARDS :")
    comp = 0
    for i in range(10):
        if not deck.cards[i].picked:
            print("   ", deck.cards[i], "-> value:", deck.cards[i].value())
            time.sleep(0.5)
            comp += deck.cards[i].value()
    print("COMPUTER's SCORE:", comp)
    print("\n\n")

    if your > comp:
        print("Congratulation!! You WON!!\n\n")
    elif your == comp:
        print("TIE!! Try Again!\n\n")
        continue
    else:
        print("You LOSE...\n\n")
    play = input("Play one more time? Y/N\n").strip('\n')

