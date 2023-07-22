class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def append(self, val):
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        next = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.display()
    L.reverse()
    L.display()
