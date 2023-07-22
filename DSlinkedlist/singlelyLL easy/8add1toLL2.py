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

    def add1(self):
        self.reverse()
        current = self.head
        prev = None
        current.val += 1
        carry = 0
        while current and carry > 0 or current.val > 9:
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
    L.append(2)
    L.append(3)
    L.append(4)
    L.display()
    L.add1()
    L.display()
