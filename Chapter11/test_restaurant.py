import unittest
from restaurant import Restaurant

class RestaurantTest(unittest.TestCase):
    """Unit Tests for the Restaurant Class"""
    def setUp(self):
        restaurant_name="Bob's Burgers"
        cusine_type="American"
        number_served=20
        self.restaurant=Restaurant(restaurant_name, cusine_type, number_served)

    def test_number_served_int(self):
        served = 30
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,30)

    def test_number_served_string(self):
        served = "30"
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,30)

    def test_increment_served_float(self):
        served=30.5
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,50.5)

    def test_increment_served_string(self):
        served = "40"
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,60)

if __name__=='__main__':
    unittest.main()