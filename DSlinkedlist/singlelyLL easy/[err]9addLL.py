# modified with literally no knowledge
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, val):
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add(self, a, b):
        self.reverse()
        a = self.head
        b = self.head
        current = a
        prev = None
        while a or b:
            current.val += a.val + b.val
            a = a.next
            b = b.next
            current = current.next

        carry = 0
        while a or b and carry > 0 or current.val > 9:
            current.val += carry
            current.val %= 10
            carry = current.val // 10
            prev = current
            current = current.next
        if carry > 0:
            prev.next = Node(carry)
        self.reverse()

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    L = LinkedList()
    A = LinkedList()
    A.append(2)
    A.append(3)
    A.append(4)
    B = LinkedList()
    B.append(4)
    B.append(5)
    B.append(6)
    L.display()
    A.add(A.head, B.head)
    L.display()
