import os
import shutil
import Deck_of_Cards
import Blackjack_Card_Points
import People
import Get_Date_Function
import datetime
import Check_for_File

def stop():
    _ = input("\n\n Press <Enter> to quit ")
    print()

def pause():
    _ = input(" Press <Enter> to continue ")

def clear(msg=""):
    if not msg == "":
        _ = input("\u0020{}\u0020".format(msg))
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
the_deck = Deck_of_Cards.Deck() # Gets a Deck of cards from the Deck of Cards.py file
#print(the_deck.deck)

#print(Blackjack_Card_Points.blackjack_points) # Gets the point values for blackjack

the_deck.shuffle() # Shuffles the deck from the Deck of Cards.py file.  The deck will never be shuffled unless this command is wrote

#print(the_deck.deck)
path = "E:\Python Code\Blackjack-Python\_Blackjack__.txt"

house_cash = 1000000
# user_question1 = input("enter your first name: ")
# user_question2 =  input("enter your last name: ")


to_write = "    House Money: ${:0,d}".format(house_cash)
    # The user first name is: {}
    # The user last name is: {}
    # The user birthday is: {}
    # The full name is: {}
    # """.format(user_question1, user_question2)




checked_for_file = Check_for_File.check_for_file(path)
if not checked_for_file : # same as if checked_for_file != True :
    game_file = open(path, "a")
    game_file.write(to_write)
    game_file.close()
    print("No file was found.   One has been created")
    pause()
         

#   this is where we take the user input to create a People...use all of the required arguments that are asked for in the __init__()

# Code here for the dealer or player choice, and creating the files for one or the other, ans looking to see...similar code to what is above


player_first =  input("enter your first name: ")
player_last = input("enter your last name: ")
#   Birthday is not asked for here, as I don't want to parse it yet (laziness at time of coding)

#   this is going to take the input just received and create the Person in the People module.  To call upon this Person, we need a variable (user)
user = People.Person(first_name = player_first, last_name = player_last, birthday = datetime.date(1950, 11, 16))

#this will go to the greeting property (method) on the People module, and apply the user info to it
print(user.greeting)
print(user.DOB)
# We assume that this program has never been ran before. So we declare all the variables, and set them to their required values, and will have the program change them as we need them to.



with open(path, "r") as player_file :
    file_context = player_file.readlines()  
    print(file_context)
    house_cash_string = file_context[0]
    print(house_cash_string)
    money_index = house_cash_string.index("$")
    print(money_index)
    _stripedCommas = house_cash_string[money_index + 1:].replace(",", "")
    print(_stripedCommas)
    program_cash = int(_stripedCommas)
    print(program_cash)
    
    

# with open(path, "w") as player_file :
#     file_context = player_file.writelines(file_context)

# file_context[0] = "House Money: ${:0,d}\n".format(house_cash)
    
# house_cash = 50000

print("end")


# Will need more similar code for the player money overwrite once game as been played more than once