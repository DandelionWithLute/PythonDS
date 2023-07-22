class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.last = None
        self.head = None

    def append(self, val):
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
        else:
            new_node = Node(val)
            self.last.next = new_node
            new_node.prev = self.last
            self.last = self.last.next
            self.last.next = None

    def display(self,Type):
        if Type == "ORD":
            current=self.head
            while current:
                print(current.val,end=" ")
                current=current.next
            print()
        if Type == "REV":
            current=self.last
            while current:
                print(current.val,end=" ")
                current=current.prev
            print()
            
            
            
if __name__ == "__main__":
    L=DoublyLinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.display("ORD")
    L.display("REV")