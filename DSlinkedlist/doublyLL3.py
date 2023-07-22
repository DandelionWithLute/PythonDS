class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, val):
        if self.last == None:
            self.head = Node(val)
            self.last = self.head
        else:
            new_node = Node(val)
            self.last.next = new_node
            new_node.prev = self.last
            new_node.next = None
            self.last = self.last.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    L=LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.display()
#20230717