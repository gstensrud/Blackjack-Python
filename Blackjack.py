import os
import Deck_of_Cards
import Blackjack_Card_Points
import People
import Get_Date_Function
import datetime

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

def yes_or_no_validation(user_question_to_answer):
    """A validation function to validate a 'yes' or 'no' question from the user, and returns the response as a variable called validated_answer"""
    validate = False
    while validate == False :
        check = input(user_question_to_answer).strip().upper()
        if check == "" :
            print("\t*** YOUR ANSWER CAN NOT BE BLANK --- TRY AGAIN ***\n")
            continue
        
        validated_answer = check[0]
        
        if validated_answer != "Y" and validated_answer !="N" :
            print("\t*** THAT IS NOT A VALID ANSWER --- TRY AGAIN ***\n")
            
        elif validated_answer == "N" :
            print("\t You have answered 'No'.  Thank you..." )            
            validate = True
            return validated_answer
        
        elif validated_answer == "Y" :
            print("\t You have answered 'Yes'.  Thank you...")
            validate = True
            return validated_answer
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
print(instructions)
answer = yes_or_no_validation(user_question_to_answer = question)
if answer == "N" :
    stop()

Blackjack_Card_Points.blackjack_points
deck1 = Deck_of_Cards.Deck()
deck1.shuffle()
print(deck1.deck)


