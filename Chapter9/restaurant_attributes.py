class Restaurant:
    def __init__(self,restaurant_name,cusine_type, number_served=0):
        self.restaurant_name=restaurant_name
        self.cusine_type=cusine_type
        self.number_served=number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cusine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, served):
        self.number_served=int(served)
    
    def increment_number_served(self, served):
        self.number_served += int(served)

print("--------------Exercise 9-4--------------")
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