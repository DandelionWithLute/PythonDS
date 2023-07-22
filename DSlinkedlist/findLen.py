class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node=Node(val)
        new_node=new_node.next
        new_node.next = self.head