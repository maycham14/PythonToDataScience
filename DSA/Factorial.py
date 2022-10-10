from math import factorial


class Factorial:
    def fact(self,number):
        if number == 1:
            return 1
        else:
            output = number * factorial(number-1)
            print(f"the factorial of {number} is {output}")


my = Factorial()
my.fact(8)
