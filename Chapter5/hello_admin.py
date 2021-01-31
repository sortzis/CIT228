print("-------------------------Exercise 5-8---------------------------")

users = ["admin","Sammi","Liane","Andrew","Andrea"]

for u in users:
    if u == "admin":
        print("Hello", u, "would you like to see a status report?")
    else:
        print("Hello", u, "thank you for logging in again.")

print("-------------------------5-9---------------------------")
users = []
if users == []:
    print("We need to find some users!")
for u in users:
    if u == "admin":
        print("Hello", u, "would you like to see a status report?")
    else:
        print("Hello", u, "thank you for logging in again.")

users = ["admin","Sammi","Liane","Andrew","Andrea"]
newUsers = ["Tina","Joe","Liane","Michael","Andrea"]

print("-------------------------5-10---------------------------")
for new in newUsers:
    for old in users:
        if new.lower() == old.lower():
            print("Sorry", new, "is taken")