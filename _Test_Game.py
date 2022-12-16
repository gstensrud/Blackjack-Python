import os
import shutil
import Deck_of_Cards
import Blackjack_Card_Points
import People
import Yes_No_Validation
import Get_Date_Function
import datetime
import Check_for_File
import Text_String_Search

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
        
welcome = """
     __        _______ _     ____ ___  __  __ _____ 
     \ \      / / ____| |   / ___/ _ \|  \/  | ____|
      \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
       \ V  V / | |___| |___ |___ |_| | |  | | |___ 
        \_/\_/  |_____|_____\____\___/|_|  |_|_____|
                   _____ ___  
                  |_   _/ _ \ 
                    | || | | |
                    | || |_| |
                    |_| \___/ 
  ____  _        _    ____ _  __   _   _    ____ _  ___ _ 
 | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ / | |
 |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' /| | |
 | |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \|_|_|
 |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_(_)_)
"""

print()
print(welcome)
pause()
clear()
print()

instructions = """
    The rules for Blackjack are simple.  You need to beat the Dealer's hand with
    the hand that you are dealt.  the closest to 21 without going over is the 
    winner.  You as the player get to go first, and can choose to:
                Hit (H),
                Stand (S),
                or Double Down (D)
        You can only Double Down if the FIRST TWO (2) CARDS that are dealt to you
            match.

"""

question = r"""
  ____   ___   __   _____  _   _  __        ___    _   _ _____ 
 |  _ \ / _ \  \ \ / / _ \| | | | \ \      / / \  | \ | |_   _|
 | | | | | | |  \ V / | | | | | |  \ \ /\ / / _ \ |  \| | | |  
 | |_| | |_| |   | || |_| | |_| |   \ V  V / ___ \| |\  | | |  
 |____/ \___/    |_| \___/ \___/     \_/\_/_/   \_\_| \_| |_| 
          _____ ___     ____  _        _ __   __
        |_   _/ _ \   |  _ \| |      / \\ \ / /
          | || | | |  | |_) | |     / _ \\ V / 
          | || |_| |  |  __/| |___ / ___ \| |  
          |_| \___/   |_|   |_____/_/   \_\_|  
  ____  _        _    ____ _  __   _   _    ____ _  _____ ___ 
 | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /__ \__ \
 |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' /  / / / /
 | |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \ |_| |_| 
 |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\(_) (_) 
"""

answer = Yes_No_Validation.yes_or_no_validation(question)

if answer == "N" :
    stop()

print(instructions)

Blackjack_Card_Points.blackjack_points # read in the dictionary blackjack_points from the Blackjack_Card_Points.py file

deck_of_cards = Deck_of_Cards.Deck() # Gets a Deck of cards from the Deck of Cards.py file
#print(deck_of_cards.deck)

#print(Blackjack_Card_Points.blackjack_points) # Gets the point values for blackjack

deck_of_cards.shuffle() # Shuffles the deck from the Deck of Cards.py file.  The deck will never be shuffled unless this command is wrote

#print(deck_of_cards.deck)

# Set the path to where the file should be located
path = "E:\Python Code\Blackjack-Python\_Blackjack__.txt"


to_write = """BLACKJACK USER DATA

    House Cash: $1,000,000
    
    Player's First Name: 
    Player's Last Name: 
    Player's Birthday is: 
    Player's Full Name: 
    Player's Available Funds: $0
"""  
    
# Check to see if the file exists ... this will return a boolean
checked_for_file = Check_for_File.check_for_file(path)

# Ask for the user input.  Do this now, as we need it in a few places later, but this is the easiest place to put is, since we can use the variable its stored as when we choose to.
player_first =  input("enter your first name: ")
player_last = input("enter your last name: ")

bad_DOB = True
while bad_DOB :
    player_DOB = input("enter your birthday [Month(xx) Day(xx) Year(xxxx)]: ").strip()
    # We need to manipulate this birthday string so it is always in the forma that the program knows, regardless of how the user entered it.


    # We need to change the birthday from a string to a date so that we can work with it.  We put this in a try/except block so that if the user enters a bad date, the program won't allow it
    try:
        date_DOB = datetime.datetime.strptime(player_DOB, "%m %d %Y").date()
        bad_DOB = False
    except:
        print("BAD DATE FORMAT")
        pause()
# This input will be used later to create the Player...use all of the required arguments that are asked for in the __init__(), unless some of that will have their values hard coded.

if not checked_for_file : # same as if checked_for_file != True :
    game_file = open(path, "a")
    game_file.write(to_write)
    game_file.close()
    print("No file was found.   One has been created")
    pause()

# elif (or else :) that returns true:
elif checked_for_file:
    # open the (path) file as a "r"ead only file
    with open(path, "r") as game_file :
        # This will return a LIST of each line in the (path) as it's own index
        file_context = game_file.readlines()        
    # Create an empty list
    full_name_list = []
    # another empty list to get the birthdays in case there is the same first and last name more than once
    birthday_list = []
    # for each indexed line from the created file_context list
    for index_line in file_context:
        # if "full name" is found in any of the indexed lines ...
        if "Full Name" in index_line :
            # look for the (":") and get that index location
            search = index_line.index(":")
            # when that is found +1 (to go to where the value of what we're looking for actually is), then strip all the whitespace
            _full_name = index_line[search + 1:].strip()
            # Take that stripped string, and add (.append) it to the empty full_name [] list 
            full_name_list.append(_full_name)
        
    # We do the same thing here as we did above to get the birthday.  We probably won't need this, but it's easier to do this now, rather than later.
        if "Birthday is" in file_context:
            search = index_line.index(":")
            _bday = index_line[search + 1:].strip()
            birthday_list.append(_bday)
    
    #   this is going to take the input just received and create the Player in the People module.  To call upon this Person, we need a variable (user)
    user = People.Player(first_name = player_first, last_name = player_last, birthday = date_DOB, funds = 0)
    """
    print(file_context)
    print(full_name_list)   
    print(birthday_list)
    """
    # Now we check to see if the user is in the file
    # We take the full_name list we created that only contains the full name of the user
    if user.full_name in full_name_list :
        print("You have been found in the file")
        pause()
    else:
        print("NOT FOUND")
        stop()

 #this will go to the greeting property (method) on the People module, and apply the user info to it
print(user.greeting)
print(user.DOB)
# We assume that this program has never been ran before. So we declare all the variables, and set them to their required values, and will have the program change them as we need them to.


# This reads in the House cash, which I hae deleted, and changed, so variables are wrong, and non existent

with open(path, "r") as game_file :
    file_context = game_file.readlines() #reading each line and saving as a list index item 
    #print(file_context)
    
    # Go to the module, use the function there, and use the file_context at index[1] to search for a "$"        
    money_string = Text_String_Search.String_Search(file_context[2], "$")
    
    program_cash = int(money_string.replace(",", "")) # Cast the variable to an number,and strip off the whitespace, so that we can do math later
    print(program_cash)
   
   # NEED TO READ IN THE OTHER INFO FROM THE FILE, AND MAKE IS USEABLE... The above is only to read in the House Cash
   

# with open(path, "w") as game_file : # open the game file ... THIS WILL BE IN WRITE MODE!!!
#     file_context = game_file.writelines(file_context)

# file_context[1] = "House Money: ${:0,d}\n".format(house_cash)
    
# house_cash = 50000

print("end")


# Will need more similar code for the player money overwrite once game as been played more than once