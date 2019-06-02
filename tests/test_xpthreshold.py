import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from calc.challenge_calc import EncounterDifficultyCalc
from calc.challenge_calc import EncounterXPCalc
from calc.challenge_calc import XPThresholdCalc


class CalcTestCase(unittest.TestCase):
    calculator = None

    def setUp(self):
        self.calculator = XPThresholdCalc()

    def tearDown(self):
        self.calculator = None

    def test_party_xp_threshold(self):
        self.calculator.add_party_level(3)
        self.calculator.add_party_level(3)
        self.calculator.add_party_level(3)
        self.calculator.add_party_level(2)

        self.assertEqual(self.calculator.calcuate_party_xp_threshold(), [
                         275, 550, 825, 1400], "Woot!")


if __name__ == '__main__':
    unittest.main()
