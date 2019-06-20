# challenge_calc

## about

challenge_calc is python utility project used to calculate encounter difficulty using D&D 5e rules.  The driver program main.py is a basic command interpreter to the calculation classes in the calc.challenge_calc.py module

## running

run the main module with python main.py

## main

starting the main.py entry program starts the interpreter the following commands are recognized

### party

party commands are used to define the character levels for the adventuring party.  character levels are 1 - 20

#### party add <level>

adds a character level to the party

#### party remove <level>

removes a character level from the party

#### party list

display the list of entered character levels

### foe

foes represent the opposing party and are represented by adding the xp level of the individual foe to the calculation

#### foe add <xp>

adds a foes xp to the challenge calculation

#### foe remove <xp>

removes the foes xp from the challenge calculation

#### foe list

lists xp of foes in calculation

### challenge

calcuates the challenge level for an encounter based on party and foe enties

## testing

python -m  unittest discover -s tests
