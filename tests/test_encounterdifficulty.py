import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calc.challenge_calc import XPThresholdCalc
from calc.challenge_calc import EncounterXPCalc
from calc.challenge_calc import EncounterDifficultyCalc

class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.party = XPThresholdCalc()
        self.encounter = EncounterXPCalc()
        self.difficulty = EncounterDifficultyCalc(self.encounter, self.party)

    def tearDown(self):
        self.party = None

    def test_party_xp_threshold(self):
        self.party.add_party_level(3)
        self.party.add_party_level(3)
        self.party.add_party_level(3)
        self.party.add_party_level(2)

        self.encounter.add_encounter_xp(1000)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Hard")

if __name__ == '__main__':
    unittest.main()