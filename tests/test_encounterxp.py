import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from challenge.calc import EncounterDifficultyCalc
from challenge.calc import EncounterXPCalc
from challenge.calc import XPThresholdCalc


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

    def test_adjusted_xp4(self):
        xp = [1000]*2
        for x in xp:
            self.calculator.add_encounter_xp(x)

        self.assertEqual(self.calculator.calcualte_adjusted_xp(), 3000)

    def test_adjusted_xp5(self):
        xp = [1000]*3
        for x in xp:
            self.calculator.add_encounter_xp(x)

        self.assertEqual(self.calculator.calcualte_adjusted_xp(), 6000)

    def test_adjusted_xp6(self):
        xp = [1000]*7
        for x in xp:
            self.calculator.add_encounter_xp(x)

        self.assertEqual(self.calculator.calcualte_adjusted_xp(), 17500)

    def test_adjusted_xp7(self):
        xp = [1000]*11
        for x in xp:
            self.calculator.add_encounter_xp(x)

        self.assertEqual(self.calculator.calcualte_adjusted_xp(), 33000)

    def test_adjusted_xp8(self):
        xp = [1000]*15
        for x in xp:
            self.calculator.add_encounter_xp(x)

        self.assertEqual(self.calculator.calcualte_adjusted_xp(), 60000)

if __name__ == '__main__':
    unittest.main()
