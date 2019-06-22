# challenge_calc

challenge_calc is python utility project used to calculate encounter difficulty using D&D 5e rules.  The driver program main.py is a basic command interpreter for the calculation classes in the calc.challenge_calc.py module

## running

run the main module with python main.py

starting the main.py entry program starts the interpreter the following commands are recognized

### party

party commands are used to define the character levels for the adventuring party.  character levels are 1 - 20

> party add [level]

adds a character level to the calculation

> party remove [level]

removes a character level from the calculation

> party list

display the list of entered character levels

### foe

foes represent the opposing party and are added by entering the xp level of the individual foe to the calculation

> foe add [xp]

adds a foes xp to the challenge calculation

> foe remove [xp]

removes the foes xp from the challenge calculation

> foe list

lists xp of foes in calculation

### challenge

> challenge

calculates the challenge level for an encounter based on party and foe entries

## testing

python -m  unittest discover -s tests

## prerequisites

Development and testing were completed with python 3.6.4 64-bit
