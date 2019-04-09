import unittest
from location import Location

class TestLab1(unittest.TestCase):
    
    def test_init(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1.name, 'SLO')
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7) #Test Case 1

        loc2 = Location('Paris', 48.9, 2.4)
        self.assertEqual(loc2.name, 'Paris')
        self.assertEqual(loc2.lat, 48.9)
        self.assertEqual(loc2.lon, 2.4) #Test Case 2

        loc3 = Location('Stockton', 50, -39.4)
        self.assertEqual(loc3.name, 'Stockton')
        self.assertEqual(loc3.lat, 50)
        self.assertEqual(loc3.lon, -39.4) #Test Case 3

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1), "Location('SLO', 35.3, -120.7)") #Test Case 1
    
        loc2 = Location('Paris', 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)") #Test Case 2

        loc3 = Location('Stockton', 50, -39.4)
        self.assertEqual(repr(loc3), "Location('Stockton', 50, -39.4)") #Test Case 3

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == loc2) #Test Case 1

        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location('Paris', 48.9, 2.4)
        self.assertFalse(loc1 == loc2) #Test Case 2

        loc1 = Location('Paris', 48.9, 2.4)
        loc2 = Location('Paris', 48.9, 2.4)
        self.assertTrue(loc1 == loc2) #Test Case 3


if __name__ == "__main__":
        unittest.main()
