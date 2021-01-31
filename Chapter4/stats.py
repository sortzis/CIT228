import random

number = random.randrange(10,100)
numList = list(range(number))
print(numList)
print("The largest number in the list is ", max(numList))
print("The smallest number in the list is ", min(numList))
print("The total of all the numbers is: ", sum(numList))
print("The average number is: ", sum(numList)/len(numList))