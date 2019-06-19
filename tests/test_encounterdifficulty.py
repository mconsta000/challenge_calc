import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

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

    def test_party_xp_threshold1(self):
        self.party.add_party_level(3)
        self.party.add_party_level(3)
        self.party.add_party_level(3)
        self.party.add_party_level(2)

        self.encounter.add_encounter_xp(1000)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Hard")

    def test_party_xp_threshold2(self):
        self.party.add_party_level(10)
        self.party.add_party_level(10)
        self.party.add_party_level(10)

        self.encounter.add_encounter_xp(1000)
        self.encounter.add_encounter_xp(1000)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Easy")

    def test_party_xp_threshold3(self):
        self.party.add_party_level(10)
        self.party.add_party_level(10)

        self.encounter.add_encounter_xp(1000)
        self.encounter.add_encounter_xp(1000)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Hard")

    def test_party_xp_threshold4(self):
        self.party.add_party_level(10)

        self.encounter.add_encounter_xp(1000)
        self.encounter.add_encounter_xp(1000)
        self.encounter.add_encounter_xp(1000)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Deadly")

    def test_party_xp_threshold5(self):
        self.party.add_party_level(10)
        self.party.add_party_level(10)
        self.party.add_party_level(10)

        self.encounter.add_encounter_xp(3600)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Medium")

    def test_party_xp_threshold6(self):
        self.party.add_party_level(10)
        self.party.add_party_level(10)
        self.party.add_party_level(10)

        self.encounter.add_encounter_xp(1200)
        self.encounter.add_encounter_xp(1200)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Medium")

    def test_party_xp_threshold7(self):
        self.party.add_party_level(10)
        self.party.add_party_level(10)

        self.encounter.add_encounter_xp(900)
        self.encounter.add_encounter_xp(900)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Medium")

    def test_party_xp_threshold8(self):
        self.party.add_party_level(1)
        self.party.add_party_level(1)
        self.party.add_party_level(2)
        self.party.add_party_level(2)

        self.encounter.add_encounter_xp(10)
        self.encounter.add_encounter_xp(10)
        self.encounter.add_encounter_xp(10)
        self.encounter.add_encounter_xp(10)

        self.assertEqual(self.difficulty.calculate_difficulty(), "Easy")

if __name__ == '__main__':
    unittest.main()
