import random


class Lottery:
    def __init__(self):
        self.letters = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
        self.guess = []

    def add(self, number):
        for i in range(number):
            index = random.randint(0, len(self.letters) - 1)
            self.guess.append(self.letters[index])
        return self.guess

    def change_char(self):
        checker = ""
        for i in self.guess:
            if type(i) == int:
                checker += str(i)
            else:
                checker += i
            return checker


lottery = Lottery()
lottery.add(23)
print(lottery.change_char())
