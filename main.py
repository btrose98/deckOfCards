import random

class Card (object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def show(self):
        print(str(self.value) + " of " + self.suit)

class Deck (object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in range(1,14):
            for suit in ["Hearts", "Diamonds","Clubs", "Spades"]:
                self.cards.append(Card(value, suit))
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self): #Fishcer Yates shuffle
        for i in range(len(self.cards)-1, 0, -1): 
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]     
    
    def draw(self):
        return (self.cards.pop())


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.draw())
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return (self.hand.pop()) #NEED TO IMPLEMENT DISCARDING A SPECIFIC CARD

               

deck = Deck()
deck.shuffle()

player = Player("Bob")
player.draw(deck)
player.showHand()