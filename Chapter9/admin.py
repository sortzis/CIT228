from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, income, username, email, permissions):
        super().__init__(first_name, last_name, age, income, username, email)
        self.priveleges = Privileges(permissions)