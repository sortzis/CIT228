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

user1 = User("Susie","Green", 25, 50000, "sueZ", "sGreen@example.com")
user2 = User("Steve","Smith", 34, 75000, "sSmith", "sSmith@example.com")
user3 = User("Jeff","Goldblum", 65, 130000, "JGold", "goldenJay@example.com")
user4 = User("Dave","Bingham", 32, 40000, "d_bing", "dbing@example.com")

user1.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()

user1.describe()
user2.describe()
user3.describe()
user4.describe()

print("-----------------Exercise 9-5-----------------")
print("Login attempts initialized")
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
print("Log in attempts: " + str(user4.login_attempts))

print("Resetting login attempts")
user4.reset_login_attempts()
print("Log in attempts: " + str(user4.login_attempts))
