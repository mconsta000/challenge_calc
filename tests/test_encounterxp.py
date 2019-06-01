import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calc.challenge_calc import XPThresholdCalc
from calc.challenge_calc import EncounterXPCalc
from calc.challenge_calc import EncounterDifficultyCalc

class CalcTestCase(unittest.TestCase):
    calculator = None

    def setUp(self):
        self.calculator = EncounterXPCalc()

    def tearDown(self):
        self.calculator = None

    def test_adjusted_xp1(self):
        self.calculator.add_encounter_xp(1000)
        self.assertEqual(self.calculator.calcualte_adjusted_xp(), 1000)

    def test_adjusted_xp2(self):
        self.calculator.add_encounter_xp(1000)
        self.assertEqual(self.calculator.calcualte_adjusted_xp(2), 1500)

    def test_adjusted_xp3(self):
        self.calculator.add_encounter_xp(1000)
        self.assertEqual(self.calculator.calcualte_adjusted_xp(6), 500)

if __name__ == '__main__':
    unittest.main()