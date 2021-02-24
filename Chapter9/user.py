class User:
    def __init__(self, first_name, last_name, age, income, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.income = income
        self.username = username
        self.email = email
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}")

    def describe(self):
        print(f"The user {self.first_name} {self.last_name} is {self.age} and makes {self.income} a year.")
        print(f"{self.first_name}'s username is {self.username} and email is {self.email}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0