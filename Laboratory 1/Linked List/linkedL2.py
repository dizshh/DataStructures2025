class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedL2:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delete(self, value):
        current = self.head
        prev = None

        if current and current.data == value:
            self.head = current.next
            current = None
            return


        while current and current.data != value:
            prev = current
            current = current.next

        if not current:
            print(f"Node with value {value} not found.")
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = linkedL2()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)

print("Linked List before deletion:")
linked_list.display()

linked_list.delete(20)

print("Linked List after deletion of 20:")
linked_list.display()

linked_list.delete(100)
