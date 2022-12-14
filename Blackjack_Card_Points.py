import Deck_of_Cards

the_deck = Deck_of_Cards.Deck()
the_cards = the_deck.cards

card_list = []
for card in the_cards :
    if card.suit == "Spades" :
        card_list.append(card.value)

point_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
card_list.remove("Ace")
card_list.append("Ace")

blackjack_points = dict(zip(card_list, point_values))


