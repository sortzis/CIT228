class Restaurant:
    def __init__(self,restaurant_name,cusine_type):
        self.restaurant_name=restaurant_name
        self.cusine_type=cusine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cusine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

print("--------------Exercise 9-1--------------")
restaurant=Restaurant("Outback Steakhouse", "American")
print("The restaurant name is ", restaurant.restaurant_name)
print("The restaurant cuisine is ", restaurant.cusine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()

print("------------------Exercise 9-2-------------")
restaurant=Restaurant("Outback Steakhouse","American")
restaurant.describe_restaurant()