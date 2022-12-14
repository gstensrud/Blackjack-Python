import os
import Deck_of_Cards
import Blackjack_Card_Points
import People
import Get_Date_Function
import datetime

the_deck = Deck_of_Cards.Deck() # Gets a Deck of cards from the Deck of Cards.py file
print(the_deck.deck)

print(Blackjack_Card_Points.blackjack_points) # Gets the point values for blackjack

the_deck.shuffle() # Shuffles the deck from the Deck of Cards.py file.  The deck will never be shuffled unless this command is wrote

print(the_deck.deck)

#   this is where we take the user input to create a People...use all of the required arguments that are asked for in the __init__()
player_first =  input("enter your first name: ")
player_last = input("enter your last name: ")
#   Birthday is not asked for here, as I don't want to parse it yet (laziness at time of coding)

#   this is going to take the input just received and create the Person in the People module.  To call upon this Person, we need a variable (user)
user = People.Person(first_name = player_first, last_name = player_last, birthday = datetime.date(1950, 11, 16))

#this will go to the greeting property (method) on the People module, and apply the user info to it
print(user.greeting)
print(user.DOB)
user_found = False

try:
    game_file = open("blackjack.txt", "r")
    file_contents = game_file.read()
    if user.full_name in file_contents:
        print("user found")
        user_found = True
    game_file.close()
    
except FileNotFoundError:
    game_file = open("blackjack.txt", "a")
    game_file.close()

game_file = open("blackjack.txt", "a")
to_write = """
The user first name is: {}
The user last name is: {}
The user birthday is: {}
The full name is {}
"""
if not user_found :
    game_file.write(to_write.format(user.first_name, user.last_name, user.DOB, user.full_name))

print("end")