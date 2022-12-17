import os
import Deck_of_Cards
import Blackjack_Card_Points
import People
import Get_Date_Function
import datetime
import Yes_No_Validation
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



Blackjack_Card_Points.blackjack_points
deck1 = Deck_of_Cards.Deck()
deck1.shuffle()

path = "E:\Python Code\Blackjack-Python\_Blackjack__.txt"

checked_for_file = Check_for_File.check_for_file(path)

###  NEED TO FIGURE OUT THE READ IN FROM THE FILE FIRST!!!



stop()




