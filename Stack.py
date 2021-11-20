class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]
