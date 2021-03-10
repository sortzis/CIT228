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
        self.number_served=float(served)
    
    def increment_number_served(self, served):
        self.number_served += float(served)
