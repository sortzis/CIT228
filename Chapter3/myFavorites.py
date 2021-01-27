print("-------------------------Hands-On #1---------------------------")
foods = ["spaghetti","coca-cola","pizza","garlic bread","vodka pasta","cheese"]
numbers = [12,7,16,36,24,48]
movies = ["This Is The End","Bride of Chucky","Breaking Dawn"]
combo = ["spaghetti","pizza",16,24,"Bride of Chucky","Breaking Dawn"]

print("Fav Foods = ", foods)
print("Fav Numbers = ", numbers)
print("Fav Movies = ", movies)
print("Fav Combo = ", combo)

print(foods[-1])
print("Fav Number 2 =", numbers[1])
print("Fav Number 4 =", numbers[3])
print("Fav Number 6 =", numbers[5])
print("1st Movie = ", movies[0])
print("2nd Movie = ", movies[1])
print("3rd Movie = ", movies[2])
print("First food, first number, first movie = ", combo[0], combo[2], combo[4])

print("-------------------------Hands-On #2---------------------------")
movies.append("Star Wars")
print("Added Movie: ", movies)
numbers.insert(3,20)
print("Added Number at Sub 3: ", numbers)
foods.insert(5,"tacos")
print("Added Food at Sub 5: ", foods)
del foods[1]
print("Deleted Food at Sub 1: ", foods)
numbers.pop(6)
print("Deleted Last Number: ", numbers)
numbers.pop(2)
print("Deleted Number at Sub 2: ", numbers)

print("-------------------------Hands-On #3---------------------------")
movies.sort()
print("Sorted List: ", movies)
foods.sort()
print("Sorted List: ", foods)
print("Temp Sorted List: ", (sorted(numbers)))
print("Unsorted List: ", numbers)
movies.reverse()
print("Sorted in Reverse: ", movies)