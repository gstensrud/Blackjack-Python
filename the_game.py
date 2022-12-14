import Deck_of_Cards
import Blackjack_Card_Points

the_deck = Deck_of_Cards.Deck() # Gets a Deck of cards from the Deck of Cards.py file
print(the_deck.deck)

print(Blackjack_Card_Points.blackjack_points) # Gets the point values for blackjack

the_deck.shuffle() # Shuffles the deck from the Deck of Cards.py file.  The deck will never be shuffled unless this command is wrote

print(the_deck.deck)