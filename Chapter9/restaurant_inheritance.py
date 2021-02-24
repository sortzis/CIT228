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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cusine_type, number_served=0, flavors=[]):
        super().__init__(restaurant_name, cusine_type, number_served=0)
        self.flavors = flavors

    def displayFlavors(self):
        print("The following flavors are available")
        for f in self.flavors:
            print(f.title())

print("--------------Exercise 9-6--------------")
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