import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """testing the max_list_iter function"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist) #Test Case 1
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(max_list_iter(tlist),10) #Test Case 2
        tlist = [9, 8, 10 ,4, 9]
        self.assertEqual(max_list_iter(tlist),10) #Test Case 3
        tlist = [5, 9, 8 ,4, 10]
        self.assertEqual(max_list_iter(tlist),10) #Test Case 4
        tlist = [-10, -9, -1 ,-4, -9]
        self.assertEqual(max_list_iter(tlist),-1) #Test Case 5
        tlist = []
        self.assertEqual(max_list_iter(tlist), None) #Test Case 6

    def test_reverse_rec(self):
        '''testing the reverse_rec function'''
        tlist = [1, 2, 3]
        self.assertEqual(reverse_rec(tlist),[3,2,1]) #Test Case 1
        tlist = []
        self.assertEqual(reverse_rec(tlist), []) #Test Case 2
        tlist = [2]
        self.assertEqual(reverse_rec(tlist), [2]) #Test Case 3
        tlist = [3, -4, 5, 0]
        self.assertEqual(reverse_rec(tlist), [0, 5, -4, 3]) #Test Case 4
        tlist = None
        with self.assertRaises(ValueError): # used to check for exception
            reverse_rec(tlist) #Test Case 5

    def test_bin_search(self):
        list_val = [0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4) #Test Case 1

        list_val = [0,1,2,3,5,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), None) #Test Case 2

        list_val = None
        with self.assertRaises(ValueError): # used to check for exception
            bin_search(5, low, high, list_val) #Test Case 3
        
        list_val = [0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, low, high, list_val), 7) #Test Case 4

        list_val = [0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, low, high, list_val), 0) #Test Case 5

if __name__ == "__main__":
        unittest.main()

    
