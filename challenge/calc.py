import csv
import pkg_resources

class EncounterXPCalc:
    """Calculate the adjusted encounter xp"""

    def __init__(self):
        self.encounter_xp = []

    def add_encounter_xp(self, encounter_xp: int):
        """Add difficulty class as an integer for each member of the
        opposing party"""

        self.encounter_xp.append(encounter_xp)
        pass

    def remove_encounter_xp(self, encounter_xp: int):
        """Remove difficulty from the existing list"""

        if encounter_xp in self.encounter_xp:
            self.encounter_xp.remove(encounter_xp)
        pass

    def calcualte_adjusted_xp(self, party_size: int=5) -> int:
        """Calculates the adjusted xp based on the challenging party 
        sizze"""

        encounter_multiplier = 0
        adjusted_xp = 0
        multiplier = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
        multiplier_idx = 1

        encounter_count = len(self.encounter_xp)

        if party_size < 3:
            multiplier_idx = 2
        elif party_size > 5:
            multiplier_idx = 0

        if encounter_count == 1:
            encounter_multiplier = multiplier[multiplier_idx]
        elif encounter_count == 2:
            encounter_multiplier = multiplier[multiplier_idx+1]
        elif encounter_count >= 3 and encounter_count <= 6:
            encounter_multiplier = multiplier[multiplier_idx+2]
        elif encounter_count >= 7 and encounter_count <= 10:
            encounter_multiplier = multiplier[multiplier_idx+3]
        elif encounter_count >= 11 and encounter_count <= 14:
            encounter_multiplier = multiplier[multiplier_idx+4]
        elif encounter_count >= 15:
            encounter_multiplier = multiplier[multiplier_idx+5]

        for xp in self.encounter_xp:
            adjusted_xp += xp

        adjusted_xp = int(adjusted_xp * encounter_multiplier)

        return adjusted_xp


class XPThresholdCalc:
    """Calculate the party xp threshold"""

    def __init__(self):
        """Intitilize member variables and load xp threshold table"""

        self.party_levels = []
        self.party_xp_theshold = []
        self.thresholds = {}

        # TODO: make thresholds map a class variable
        thresholds = pkg_resources \
            .resource_string(__name__, '/'.join(('resource','xp_threshold.csv'))) \
            .decode('utf-8')

#        with open("resource/xp_threshold.csv") as thresholds:
        reader = csv.reader(thresholds.splitlines(), delimiter=',')
        for row in reader:
            ints = [int(element) for element in row]
            self.thresholds[ints[0]] = ints[1:]

        pass

    def add_party_level(self, character_level: int):
        """Add each party member as an integer value"""

        self.party_levels.append(character_level)
        pass

    def remove_party_level(self, character_level: int):
        """Remove part level from existing list"""

        if character_level in self.party_levels:
            self.party_levels.remove(character_level)
        pass

    def calcuate_party_xp_threshold(self) -> [int]:
        """Calculate the party xp threshold as an array of 4 integers"""

        self.party_xp_threshold = [0] * 4

        for level in self.party_levels:
            self.party_xp_threshold = [
                x + y for x, y in zip(self.party_xp_threshold, self.thresholds[level])]

        return self.party_xp_threshold


class EncounterDifficultyCalc:
    """Calculate the difficulty of an encounter"""

    difficulty = ["Easy", "Medium", "Hard", "Deadly"]

    def __init__(self, encounter_xp_calc: EncounterXPCalc, 
        xp_threshold_calc: XPThresholdCalc):
        """Construct the EncounterDifficultyCalc with EncounterXPCalc 
        and XPThresholdCalc.  This class uses the calculations 
        provided by the passed classes to determine the difficulty of
        the encounter"""

        self.encounter_xp_calc = encounter_xp_calc
        self.xp_threshold_calc = xp_threshold_calc

    def calculate_difficulty(self) -> str:
        """Determine encounter difficulty using object passed during
        instantiation"""

        xp_threshold = self.xp_threshold_calc.calcuate_party_xp_threshold()
        encounter_xp = \
            self.encounter_xp_calc.calcualte_adjusted_xp(
                len(self.xp_threshold_calc.party_levels))
        encounter_difficulty = self.difficulty[0]

        for i, threshold in reversed(list(enumerate(xp_threshold))):
            if threshold <= encounter_xp:
                encounter_difficulty = self.difficulty[i]
                break

        return encounter_difficulty