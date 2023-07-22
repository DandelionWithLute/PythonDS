class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, val):
        if self.last_node is None:
            self.head = Node(val)
            self.last_node = self.head
        else:
            self.last_node.next = Node(val)
            self.last_node = self.last_node.next
            self.last_node.next = self.head

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


# Driver code
if __name__ == "__main__":
    L = CircularLinkedList()
    L.append(12)
    L.append(56)
    L.append(2)
    L.append(11)

    # Function call
    L.display()
