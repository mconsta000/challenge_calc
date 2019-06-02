import csv


class EncounterDifficultyCalc:
    difficulty = ["Easy", "Medium", "Hard", "Deadly"]

    def __init__(self, encounter_xp_calc, xp_threshold_calc):
        self.encounter_xp_calc = encounter_xp_calc
        self.xp_threshold_calc = xp_threshold_calc

    def calculate_difficulty(self):
        xp_threshold = self.xp_threshold_calc.calcuate_party_xp_threshold()
        encounter_xp = \
            self.encounter_xp_calc.calcualte_adjusted_xp(
                len(self.xp_threshold_calc.party_levels))
        encounter_difficulty = "Unknown"

        for i, threshold in reversed(list(enumerate(xp_threshold))):
            if threshold <= encounter_xp:
                encounter_difficulty = self.difficulty[i]
                break

        return encounter_difficulty


class EncounterXPCalc:
    def __init__(self):
        self.encounter_xp = []

    def add_encounter_xp(self, encounter_xp):
        self.encounter_xp.append(encounter_xp)
        pass

    def calcualte_adjusted_xp(self, party_size=5):
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
        elif encounter_count == 2.0:
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
    def __init__(self):
        self.party_levels = []
        self.party_xp_theshold = []
        self.thresholds = {}

        with open("resource/xp_threshold.csv") as thresholds:
            reader = csv.reader(thresholds, delimiter=',')
            for row in reader:
                ints = [int(element) for element in row]
                self.thresholds[ints[0]] = ints[1:]

        pass

    def add_party_level(self, character_level):
        self.party_levels.append(character_level)
        pass

    def calcuate_party_xp_threshold(self):
        self.party_xp_threshold = [0] * 4

        for level in self.party_levels:
            self.party_xp_threshold = [
                x + y for x, y in zip(self.party_xp_threshold, self.thresholds[level])]

        return self.party_xp_threshold
