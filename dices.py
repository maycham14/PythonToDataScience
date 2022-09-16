import random


class Dice:

    def __init__(self, side=6):
        self.guessValue = None
        self.side = side

    def roll_die(self):
        self.guessValue = random.randint(1, self.side)
        return self.guessValue

    def no_of_rolls(self, roll):
        rolled = []
        for i in range(roll):
            rolled.append(self.roll_die())
        return rolled


die = Dice(8)
die.no_of_rolls(7)
output = die.no_of_rolls(1_000_000)
print(output)