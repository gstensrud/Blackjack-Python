import datetime

greeting_message = """
    Welcome {}!, Nice to see you!  Your birthday information is {}!
        Bet that's info you'll never use!
"""
class Person() :
    def __init__(self, first_name, last_name, birthday) :
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
    
    @property
    def full_name(self) :
        return self.first_name + " " + self.last_name
    
    @property
    def DOB(self) :
        return self.birthday.strftime("\t %A, %d %B, %Y (That's week %W, and Day %j of the year)")
    
    @property
    def greeting(self) :
        return (greeting_message.format(self.full_name, self.DOB))
    
class Player(Person) :
    def __init__(self, first_name, last_name, birthday, funds):
        super().__init__(first_name, last_name, birthday)
        self.funds = funds
