class Fibonacci:

    def fibonacci(self, x):
        if x == 0:
            return 0
        elif x == 1 or x == 2:
            return 1
        elif x > 2:
            return self.fibonacci(x-1) + self.fibonacci(x-2)


output = Fibonacci()
for i in range(10):
    print(output.fibonacci(i))
