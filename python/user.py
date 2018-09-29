class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.home = "GuangDong"
        self.sex = "man"
        self.age = 6
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is a " + self.sex + ", and his age is " + str(self.age))

user1 = User("derek", "yuan")
user1.describe_user()

