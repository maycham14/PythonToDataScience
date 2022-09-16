import random


class Lottery:

    def __init__(self):
        self.letters = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
        self.guess = []

    def select_nth_items(self, num):
        for i in range(num):
            index = random.randint(0, len(self.letters) - 1)
            self.guess.append(self.letters[index])

        return self.return_format()

    def return_format(self):
        output = ""
        for char in self.guess:
            if type(char) == int:
                output += str(char)
            else:
                output += char

        print(f"This is the lottery output \"{output}\"")


lotto = Lottery()
lotto.select_nth_items(4)
