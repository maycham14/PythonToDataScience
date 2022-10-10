class ListSack:

    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def push(self, data):
        self.data.append(data)

    def is_empty(self):
        if self.length() == 0:
            raise ValueError("Empty data")
        else:
            return self.data[self.length() - 1]

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[self.length() - 1]


checker = ListSack()
checker.push(6)
checker.push(7)
checker.push(8)
print(checker.top())
print(checker.length())
