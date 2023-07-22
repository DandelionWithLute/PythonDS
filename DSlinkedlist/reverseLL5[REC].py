class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.last = None
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rec = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rec
    
    def reverseIterative(self):
        prev=None
        current=self.head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        
if __name__ == "__main__":
    L=LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.display()
    # L.head=L.reverse(L.head)
    L.reverseIterative()
    L.display()
