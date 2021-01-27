print("-------------------------Exercise 3-4-------------------")
guestList = ["Bryan","Barbara","Ricky"]
print(guestList[0], ", can you make it to dinner this Saturday?")
print(guestList[1], ", can you make it to dinner this Saturday?")
print(guestList[2], ", can you make it to dinner this Saturday?")

print("-------------------------Exercise 3-5-------------------")
print(guestList[1], ", can't make it to dinner.")
guestList[1] = "Sylvester"
print(guestList[0], ", can you make it to dinner this Saturday?")
print(guestList[1], ", can you make it to dinner this Saturday?")
print(guestList[2], ", can you make it to dinner this Saturday?")

print("-------------------------Exercise 3-6-------------------")
print("We found a bigger table allowing more guests!")
guestList.insert(0,"William")
guestList.insert(2,"John Oliver")
guestList.append("Joe Biden")
print("We will be having ", len(guestList), "guests for dinner.") # exercise 3-9 <<<<<<<<<<<<
print(guestList[0], ", can you make it to dinner this Saturday?")
print(guestList[1], ", can you make it to dinner this Saturday?")
print(guestList[2], ", can you make it to dinner this Saturday?")
print(guestList[3], ", can you make it to dinner this Saturday?")
print(guestList[4], ", can you make it to dinner this Saturday?")
print(guestList[5], ", can you make it to dinner this Saturday?")

print("-------------------------Exercise 3-7-------------------")
print("The table won't arrive in time for dinner.")
removedGuest = guestList.pop(0)
print(removedGuest, ", I'm sorry about the cancellation. Maybe next time?")
removedGuest = guestList.pop(1)
print(removedGuest, ", I'm sorry about the cancellation. Maybe next time?")
removedGuest = guestList.pop(1)
print(removedGuest, ", I'm sorry about the cancellation. Maybe next time?")
removedGuest = guestList.pop(1)
print(removedGuest, ", I'm sorry about the cancellation. Maybe next time?")
print(guestList[0], ", can you make it to dinner this Saturday?")
print(guestList[1], ", can you make it to dinner this Saturday?")
del guestList[0]
del guestList[0]
print("Revised Guest List: ", guestList)
