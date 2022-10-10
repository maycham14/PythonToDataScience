class ArrayStacks:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()

    def peep(self):
        return self.stack[0]

    def is_empty(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            return "stack is not empty"


class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) == 0:
            return "queue is empty"
        else:
            return "queue is not empty"


output = ArrayStacks()
output.push(2)
output.push(6)
print(output.pop())
print(output.pop())
print(output.pop())
print(output.is_empty())
checker = ArrayQueue()
checker.enqueue(2)
checker.enqueue(23)
print(checker.dequeue())
print(checker.dequeue())
print(checker.dequeue())
print(checker.is_empty())
