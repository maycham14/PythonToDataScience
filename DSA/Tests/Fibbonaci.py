class Fibonacci:

    def fibonacci(self, value):

        if value == 0:
            return 0
        elif value == 1 or value == 2:
            return 1
        elif value > 2:
            return self.fibonacci(value - 1) + self.fibonacci(value - 2)


checker = Fibonacci()
print(checker.fibonacci(10))
