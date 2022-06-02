# Your PremiumUser class goes here
from User import User

class Premium(User):
    def __init__(self, paid=True):
        parent_instance = super()
        self.paid = paid

charles = Premium()    
print(charles.paid)

#  'charles',"chaz@codeplatoon.org", 1231231230, 55,
#  name, email_address, phone_number, age, 