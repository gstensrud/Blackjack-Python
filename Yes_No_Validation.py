
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