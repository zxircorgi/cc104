class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):  # O(n)
        new_node = Node(data)
print("None")