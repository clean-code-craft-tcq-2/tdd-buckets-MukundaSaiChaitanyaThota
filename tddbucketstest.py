import Driven_Range
import unittest

class driven_range_test(unittest.TestCase):

    def test_rangeAndFrequency(self):
        self.assertTrue(driven_range().main([4,5]) == {'4-5': '2'})

if __name__ == '__main__':
  unittest.main()
