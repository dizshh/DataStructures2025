# using list
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty!"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue



my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("Current Queue:", my_queue.display())

print("Front element:", my_queue.peek())

print("Dequeued element:", my_queue.dequeue())

print("Queue after dequeue:", my_queue.display())

print("Is queue empty?", my_queue.is_empty())

print("Queue size:", my_queue.size())
