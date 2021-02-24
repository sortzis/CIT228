from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cusine_type, number_served=0, flavors=[]):
        super().__init__(restaurant_name, cusine_type, number_served=0)
        self.flavors = flavors

    def displayFlavors(self):
        print("The following flavors are available")
        for f in self.flavors:
            print(f.title())