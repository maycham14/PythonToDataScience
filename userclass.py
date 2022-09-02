class User:

    def __init__(self, username, first_name, last_name, age):
        self.username = username
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.login_attempts = 56

    def describe_user(self):
        print(f" username:\n\t {self.username}")
        print(f" name:\n\t {self.first_name} {self.last_name}")
        print(f" age:\n\t {self.age}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f" login attempts:\n\t {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = self.login_attempts - self.login_attempts + 0
        print(f"login attempts: {self.reset_login_attempts}")


my_info = User("maycham14", "mariama", "cham", 22)
my_info.describe_user()
my_info.increment_login_attempts()
my_info.increment_login_attempts()
my_info.increment_login_attempts()
my_info.reset_login_attempts()
