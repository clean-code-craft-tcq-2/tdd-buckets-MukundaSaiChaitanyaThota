import unittest
import tdd_buckets

class ChargingCurrentRangeTest(unittest.TestCase):
    def test_Current_Range(self):
        readings = [1,2,2,3]
        self.assertTrue(get_current_range(readings) == '1-3, 4')

if __name__ == '__main__':
  unittest.main()
