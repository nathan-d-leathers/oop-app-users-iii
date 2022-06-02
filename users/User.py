# Your User class goes here
class User:

    public_posts = []

    def __init__(self, name, email_address, phone_number, age,post_count):
        self.name = name
        self.email_address = email_address
        self.phone_number = str(phone_number)
        self.age = age
        self.post = []
        self.post_count = post_count

    def add_post(self, content):
            self.post_count += 1
            self.post.append({self.name:  content})
            User.public_posts.append({'name': self.name, 'content' : content})

jake = User('Jake',"jakeboy@codeplatoon.org", 1231231230, 5, 0)
new_post = jake.add_post("Another great day in Ohmaha?")

# print(jake.post)
# output:  [{'JAKE': 'Another great day in Ohmaha?'}]

# print(jake.public_posts)
# output:  [{'name': 'JAKE', 'content': 'Another great day in Ohmaha?'}]

