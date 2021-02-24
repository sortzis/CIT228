from restaurant import Restaurant
from icecream import IceCreamStand

restaurant=Restaurant("Outback Steakhouse", "American", 4)
restaurant.open_restaurant()
restaurant.describe_restaurant()
#printing number served
print("The number of customers initially served is ", restaurant.number_served)
#changing the number served
restaurant.number_served = 20
print("The new number of customers served is ", restaurant.number_served)
#using set_number_served method to change customers served
served = input("How many customers have been served?")
restaurant.set_number_served(served)
print("The new number of customers served is ", restaurant.number_served)
#adding customers served using increment_number_served()
served = input("How many additional customers have been served?")
restaurant.increment_number_served(served)
print("The total number of customers served is ", restaurant.number_served)

flavors = []
flavor = ""
flavor = input("Name your first flavor: ")
flavors.append(flavor)
flavor = input("Name your second flavor: ")
flavors.append(flavor)
flavor = input("Name your third flavor: ")
flavors.append(flavor)

stand = IceCreamStand("Dairy Queen", "Desert", 0, flavors)

print(f"The restaurant is called {stand.restaurant_name} it serves {stand.cusine_type}")

stand.displayFlavors()