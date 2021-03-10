import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_formatted_city(self):
        city_test = city_country('Santiago', 'Chile')
        self.assertEqual(city_test, 'Santiago, Chile')

    def test_formatted_population(self):
        city_test = city_country('Santiago','Chile','5,000,000')
        self.assertEqual(city_test, 'Santiago, Chile - Population: 5,000,000')

if __name__=='__main__':
    unittest.main()
