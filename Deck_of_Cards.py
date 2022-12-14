import random

class Card :
    def __init__(self, suit, value) :
        self.suit = suit
        self.value = value
        
    def show_card(self) :
#   This is where the unicode or ASCII art for the cards will go, still using the {} to show where the value of the  card is
        a_card = "{} of {}".format(self.value, self.suit)
        return a_card # This gives the 'answer' to this function a variable

class Deck :
    def __init__(self) :
        self.cards = []
        self.deck = []
        self.build()
    
    def build(self) :
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"] :
             for value in range (1, 14) :
                if value == 1 :
                    value = "Ace"
                elif value == 11 :
                    value = "Jack"
                elif value == 12 :
                    value = "Queen"
                elif value == 13 :
                    value = "King"
                self.cards.append(Card(suit, value))
                self.deck.append("{} of {}".format(value, suit))
                 
                 
    def show_cards(self) :
        for card in self.cards :
            x_card = card.show_card()
            print(x_card)
            
    def shuffle(self) :
        random.shuffle(self.deck)
    
