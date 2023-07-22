class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
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

    def display(self):
        current = self.head
        while current is not None:
            print(current.val,end=" ")
            current=current.next
        print
        
if __name__ == "__main__":
    L=LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.display()