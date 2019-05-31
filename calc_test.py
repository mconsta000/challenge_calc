import unittest
from calc import Calc

class CalcTestCase(unittest.TestCase):
    calculator = None

    def setUp(self):
        self.calculator = Calc()

    def tearDown(self):
        self.calculator = None

    def test_party_xp_threshold(self):
        self.calculator.add_party_level(3)
        self.calculator.add_party_level(3)
        self.calculator.add_party_level(3)
        self.calculator.add_party_level(2)

        self.assertEqual(self.calculator.calcuate_party_xp_threshold(), [275, 550, 825, 1400], "1st Level Threshold Test")

if __name__ == '__main__':
    unittest.main()