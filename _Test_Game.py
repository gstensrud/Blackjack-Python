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
path = "E:\Python Code\Blackjack-Python\__Blackjack__.txt"

# Create Empty lists for later
full_name_list = []
# another empty list to get the birthdays in case there is the same first and last name more than once
birthday_list = []

# String to write if there is no file found in the path
to_write = """BLACKJACK USER DATA

    House Cash: $1,000,000
    
    Player's First Name: 
    Player's Last Name: 
    Player's Birthday is: 
    Player's Full Name: 
    Player's Available Funds: $0
"""  
    
# Check to see if the file exists ... this will return a boolean
checked_for_file = Check_for_File.check_for_file(path) # "File Found" on the console comes from the function here

file_created = False # Random switch variable if the file gets created

if not checked_for_file : # same as if checked_for_file != True :
    game_file = open(path, "a")
    game_file.write(to_write)
    file_created = True # Flip the switch variable to True because we created the file
    
    # Write to file code stuff here ... this is also where the birthday stuff will go ...
    # I decided to write this code later, as I have all the variables converted to their appropriate data types required later in the code, so I'll just do it there
    
    game_file.close()
    print("No file was found. One has been created")
    pause()
# ********   THIS WITH BLOCK MAY BE WRONG!!!!!
with open(path, "r") as game_file :
    file_context = game_file.readlines() #reading each line and saving as a list index item 
    # now we read in all the information that we want from each line of the text file, and parse them to whatever data type we want them to be in later
    p_first_name = Text_String_Search.String_Search(file_context[4], ":")
    p_last_name = Text_String_Search.String_Search(file_context[5], ":")
    p_bday = Text_String_Search.String_Search(file_context[6], ":")
    p_full_name = Text_String_Search.String_Search(file_context[7], ":")
    p_funds = Text_String_Search.String_Search(file_context[8], "$")
    player_funds = int(p_funds)

if p_first_name == "" :
# Ask for the user input.  Do this now, as we need it in a few places later, but this is the easiest place to put is, since we can use the variable its stored as when we choose to.
    player_first =  input("enter your first name: ")
    player_last = input("enter your last name: ")
    
    bad_DOB = True # Variable for birthday format validation
    while bad_DOB :
        player_DOB = input("enter your birthday [Month(xx) Day(xx) Year(xxxx)]: ").strip()
        # We need to manipulate this birthday string so it is always in the forma that the program knows, regardless of how the user entered it.
        
        # Here I can code a dictionary to make things the date input from numbers to Month names.  That way, the user can enter the birthday any way they want

        # We need to change the birthday from a string to a date so that we can work with it.  We put this in a try/except block so that if the user enters a bad date, the program won't allow it
        try:
            date_DOB = datetime.datetime.strptime(player_DOB, "%m %d %Y").date()
            bad_DOB = False
        except:
            print("BAD DATE FORMAT")
            pause()
#  Now we need to write this information to the file
    # game_file = open(path, "w") # open the game file ... THIS WILL BE IN WRITE MODE!!!
    # game_file.writelines(file_context)
    # game_file.writelines(to_write)
    # game_file.close()
    print("variable player_first (when path file first name is found to be empty)= " + player_first + " is a : ", type(player_first))
    print("variable player_last (when path file first name is found to be empty)= " + player_last + " is a : ", type(player_last))
    print("variable player_DOB (when path file first name is found to be empty)= " + player_DOB + " is a : ", type(player_DOB)) 
    print("concatenated name to form full name (when path file first name is found to be empty)= " + player_first + " " + player_last) 
    
    player_full_name = player_first + " " + player_last
    the_overwrite = """BLACKJACK USER DATA

    House Cash: $1,000,000
    
    Player's First Name: {}
    Player's Last Name: {}
    Player's Birthday is: {}
    Player's Full Name: {}
    Player's Available Funds: $0
""".format(player_first, player_last, date_DOB, player_full_name)
    
    with open(path, "w") as game_file :
        
        game_file.writelines(the_overwrite)
        
    print("the file should be updated")
    
   # open the (path) file as a "r"ead only file
with open(path, "r") as game_file :        
    # This will return a LIST of each line in the (path) as it's own index
    file_context = game_file.readlines()    
    # for each indexed line from the created file_context list
    for index_line in file_context:
        # *** this could be replaced with text_string_search function and do very similar to what  is doing now ***
        # if "full name" is found in any of the indexed lines ...
        if "Full Name" in index_line :
            # look for the (":") and get that index location
            search = index_line.index(":")
            # when that is found +1 (to go to where the value of what we're looking for actually is), then strip all the whitespace
            _full_name = index_line[search + 1:].strip()
            # Take that stripped string, and add (.append) it to the empty full_name [] list 
            full_name_list.append(_full_name)
                
        # We do the same thing here as we did above to get the birthday.  We probably won't need this, but it's easier to do this now, rather than later.
        if "Birthday is" in index_line:
            search = index_line.index(":")
            _bday = index_line[search + 1:].strip()
            birthday_list.append(_bday)
    
    # This input will be used later to create the Player...use all of the required arguments that are asked for in the __init__(), unless some of that will have their values hard coded.

birthday = str(birthday_list)
    
    #   this is going to take the input just received and create the Player in the People module.  To call upon this Person, we need a variable (user)
user = People.Player(first_name = player_first, last_name = player_last, birthday = date_DOB, funds = 0)
# These are not populating the lists ... this needs to be looked into to see why
# I should just have to read in the file again


print("file_context = ", file_context, "-", type(file_context))
print("full_name list = ", full_name_list, "-", type(full_name_list))   
print("birthday_list = ", birthday_list, "-", type(birthday_list))

# Now we check to see if the user is in the file
# We take the full_name list we created that only contains the full name of the user
existing_user = True
if user.full_name in full_name_list :
    print("You have been found in the file")
    pause()
else:
    print("NOT FOUND")
    existing_user = False
    pause()

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
    
    program_cash = int(money_string.replace(",", "")) # Parse the variable to an number,and strip off the whitespace, so that we can do math later
    print(program_cash)
    


print()
print("p_first_name variable = " + p_first_name + " - ", type(p_first_name))
print("p_last_name variable = " + p_last_name + " - ", type(p_last_name))
print("p_full_name variable (from data file) =  " + p_full_name + " - ", type(p_full_name))
print("full_name_list (Empty List created at in when the code was checking \n\t to \
    see if the file in the path exists) = ", full_name_list ," - ", type(full_name_list))
print("p_bday variable = " + p_bday + " - ", type(p_bday))
print("birthday variable (changed to a string from the birthday_list) = " + birthday + \
    " - ", type(birthday))
print("birthday_list (Empty List created at the same time when the code was checking \
    \n\t to see if the file in the path exists) = ", birthday_list, " - ", type(birthday_list))
print("p_funds variable = " + p_funds + " - ", type(p_funds))
print("player_funds (above variable parsed to an int) = ", player_funds, " - ", type(player_funds))



    


# house_cash = 50000

print("end")



# Will need more similar code for the player money overwrite once game as been played more than once