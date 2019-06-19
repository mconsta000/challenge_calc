from calc.challenge_calc import EncounterDifficultyCalc
from calc.challenge_calc import XPThresholdCalc
from calc.challenge_calc import EncounterXPCalc

def main():
    xp_threshold = XPThresholdCalc()
    xp_encounter = EncounterXPCalc()
    challenge = EncounterDifficultyCalc(xp_encounter,xp_threshold)

    command = ["continue"]
    while command != ["quit"]:
        command = input().split(' ')
        if command[0] == "party":
            if command[1] == "add":
                xp_threshold.add_party_level(int(command[2]))
                pass
            elif command[1] == "remove":
                xp_threshold.party_levels.remove(int(command[2]))
                pass
            elif command[1] == "list":
                print(xp_threshold.party_levels)
                pass
            elif command[1] == "threshold":
                print(xp_threshold.calcuate_party_xp_threshold())
                pass
        elif command[0] == "foe":
            if command[1] == "add":
                xp_encounter.add_encounter_xp(int(command[2]))
                pass
            elif command[1] == "remove":
                xp_encounter.encounter_xp.remove(int(command[2]))
                pass
            elif command[1] == "list":
                print(xp_encounter.encounter_xp)
                pass
            elif command[1] == "xp":
                print(xp_encounter.calcualte_adjusted_xp(len(xp_threshold.party_levels)))
                pass
        elif command[0] == "challenge":
            print (challenge.calculate_difficulty())

if __name__ == "__main__":
    main()