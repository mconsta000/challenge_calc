import csv

class Calc:

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

    def add_encounter_xp(self, encounter_xp):
        pass

    def calcualte_adjusted_xp(self):
        return -1

    def calcuate_party_xp_threshold(self):
        work = [0] * 4

        for level in self.party_levels:
            work = [x + y for x, y in zip(work, self.thresholds[level])]

        return work

    def reset_encounter_xp(self):
        pass