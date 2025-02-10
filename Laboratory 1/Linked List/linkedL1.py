class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class linkedL1:
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 


linked_list = linkedL1()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

print("Linked List:")
linked_list.display()
