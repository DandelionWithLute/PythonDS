class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, val):
        if self.last == None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def areIdentical(self, a, b):
        if a == None and b == None:
            return True
        if a != None and b != None:
            return a.val == b.val and self.areIdentical(a.next, b.next)
        else:
            return False


if __name__ == "__main__":
    A = LinkedList()
    B = LinkedList()
    A.append(1)
    A.append(2)
    A.append(3)
    B.append(1)
    B.append(2)
    B.append(3)
    B.append(4)

if A.areIdentical(A.head, B.head):
    print("yes")
else:
    print("no")
