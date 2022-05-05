import tddbuckets
import unittest

class driven_range_test(unittest.TestCase):

    def test_rangeAndFrequency(self):
        self.assertTrue(driven_range().main([1,3,2,3]) == {'1-3': '4'})
        self.assertTrue(driven_range().main([2,3,4,5,6,7,,8,10]) == {'2-8': '7', '10-10': '1'})
        self.assertTrue(driven_range().main([-5,-4,-3,1,2,3,4,6,7,8]) == {'-5--3': '3', '1-4': '4', '6-8': '3'})
        self.assertTrue(driven_range().main([2,2,4,4,10,11,12]) == {'2-4': '4', '10-12': '3'})
        self.assertTrue(driven_range().main([3,4]) == {'3-4': '2'})


if __name__ == '__main__':
  unittest.main()
