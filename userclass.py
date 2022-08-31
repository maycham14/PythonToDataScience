class User:

    def __init__(self, username, first_name, last_name, age):
        self.username = username
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def describe_user(self):
        print(f" username:\n\t {self.username}")
        print(f" name:\n\t {self.first_name} {self.last_name}")
        print(f" age:\n\t {self.age}")


my_info = User("maycham14","mariama", "cham", 22)
my_info.describe_user()
