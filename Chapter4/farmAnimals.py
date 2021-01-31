print("-------------------------Hands On #3---------------------------")
animals = ["horse","cow","pig","chicken","rooster","goat"]
print("-------------------------Original List---------------------------")
for animal in animals:
    print(animal)

newAnimals = animals[:]
newAnimals.append("cat")
newAnimals.append("dog")
newAnimals.append("llama")
newAnimals.append("mink")
print("-------------------------New List---------------------------")
for new in newAnimals:
    print(new)

print("------------------------Exercise 4-10----------------------------")
print("The first three items in the list are:", newAnimals[0:3])
print("Three items in the middle of the list are:", newAnimals[4:7])
print("The last three items in the list are:", newAnimals[7:11])