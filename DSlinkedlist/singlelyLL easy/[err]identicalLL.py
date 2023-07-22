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
            self.last = Node(val)
            self.head = self.last


    def append1(self, val):
        if self.last == None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last = Node(val)
            self.last = self.last.next