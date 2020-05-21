import random;

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
    def contents(self):
        cardnames = []
        for card in self.cards:
            cardnames.append(str(card))
        return cardnames

print("==========ENJOY CARD GAME===========\n")
play = "Y"
while play == "Y":
    print("===========GAME START!!!============")
    deck = Deck()
    deck.shuffle()
    a = [0, 0, 0, 0, 0]
    b = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
    integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for i in range(5):
        while True:
            ask = "CHOOSE "+b[i]+" CARD!!!(integer between 1 to 10) : "
            a[i] = input(ask)
            if a[i] in integers:
                if deck.cards[int(a[i])-1].picked:
                    print("YOU ALREADY CHOOSE", a[i],"!!!")
                    continue
                deck.cards[int(a[i])-1].picked = True
                print(deck.cards[int(a[i])-1], "has value", deck.cards[int(a[i])-1].value())
                break
            print("WRONG INPUT!!")

    print("YOUR CARDS :")
    your = 0
    for i in range(10):
        if deck.cards[i].picked:
            print("   ", deck.cards[i], "-> value :", deck.cards[i].value())
            your += deck.cards[i].value()
    print("YOUR CARDS SCORE IS", your)
    print("\n\n")

    print("COMPUTER's CARDS :")
    comp = 0
    for i in range(10):
        if not deck.cards[i].picked:
            print("   ", deck.cards[i], "-> value :", deck.cards[i].value())
            comp += deck.cards[i].value()
    print("COMPUTER's SCORE IS", comp)
    print("\n\n")

    if your > comp:
        print("CONGRATULATION!!!! YOU WON THE GAME!!\n\n")
    elif your == comp:
        print("YOU AND YOUR COMPUTER GOT SAME SCORE!! TRY AGAIN\n\n")
        continue
    else:
        print("YOUR COMPUTER WON THE GAME...\n\n")
    play = input("DO YOU WANT TO PLAY ONE MORE TIME? Y/N").strip('\n')
    print(play)

