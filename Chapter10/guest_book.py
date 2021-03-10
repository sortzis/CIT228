#appends multiple lines to the file
"""guest = input("What is your name (q to quit)?")
with open("Chapter10/guest.txt","a") as guestFile:
    while guest!='q':
        guest+="\n"
        print(f"Hello {guest} how are you today?")
        guestFile.write(guest)
        guest = input("What is your name (q to quit)?")"""
import random
import os
filename="Chapter10/guest.txt"
if os.path.exists(filename):
    os.remove(filename)
#creating a new file
rooms = []
with open(filename, "w") as guestFile:
    guest=input("Please enter your name (q to quit)?")
    while guest != 'q':
        number=random.randint(1,50)
        while number in rooms:
            number=random.randint(1,50)
        print(f"{guest} you will be in room number {number}")
        rooms.append(number)
        guest+=", room# " + str(number) + "\n"
        guestFile.write(guest)
        guest=input("Please enter your name (q to quit)?")
#reading from the new file
with open(filename) as guestFile:
    print("-------------Guest and Rooms Assigned------------\n")
    for line in guestFile:
        print(line)