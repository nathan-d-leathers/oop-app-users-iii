from User import User

class Free(User):
    def __init__(self, name, email_address, phone_number, age, post_count, paid=False):
        self.paid = paid
        self.post_count = post_count
        super().__init__(self, name, email_address, phone_number, age)

    def add_post(self,post_count):
        if post_count > 2 and self.paid == False:
            return("Upgrade to Premium for Unlimted Posting")


ben = Free('ben',"chaz@codeplatoon.org", 1231231230, 55,3)    
# print(ben.paid)

ben.add_post('its a jungle out there')
print(ben.post)

