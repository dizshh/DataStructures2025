class Stack2:
    def __init__(self):

        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack


my_stack = Stack2()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Current Stack:", my_stack.display())

print("Top element:", my_stack.peek())

print("Popped element:", my_stack.pop())

print("Stack after pop:", my_stack.display())

print("Is stack empty?", my_stack.is_empty())

print("Stack size:", my_stack.size())
