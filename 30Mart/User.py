class User():
    def __init__(self, first_name, last_name,
                 user_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.location = location
        self.email = email

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + '\n' +
              "Username: " + self.user_name + '\n' + "Email: " +
              self.email + "\n" + "Location: " + self.location.title())


eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
print("")
willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
