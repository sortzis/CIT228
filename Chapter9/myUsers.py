from user import User
from privileges import Privileges
from admin import Admin

priv = ["Can add post", "Can delete post", "Can ban users"]

privileges = Privileges(priv)
user1 = User("Susie","Green", 25, 50000, "sueZ", "sGreen@example.com")
user2 = User("Steve","Smith", 34, 75000, "sSmith", "sSmith@example.com")
user3 = User("Jeff","Goldblum", 65, 130000, "JGold", "goldenJay@example.com")
user4 = User("Dave","Bingham", 32, 40000, "d_bing", "dbing@example.com")
admin1 = Admin("Scott","Stevenson", 38, 72000, "s_steven", "sSteve@example.com", privileges)

user1.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()
admin1.greet_user()

user1.describe()
user2.describe()
user3.describe()
user4.describe()
admin1.describe()
privileges.show_privileges()