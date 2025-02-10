class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def reverse_string(input_string):
    stack = Stack()

    for char in input_string:
        stack.push(char)

    reversed_string = ""

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


if __name__ == "__main__":
    input_str = "Hello, World!"
    reversed_str = reverse_string(input_str)
    print(f"Original String: {input_str}")
    print(f"Reversed String: {reversed_str}")