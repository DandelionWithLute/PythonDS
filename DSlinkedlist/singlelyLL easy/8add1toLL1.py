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
        head = self.head
        carry = 0
        prev = None
        head.val += 1
        while head != None and head.val > 9 or carry > 0:
            prev = head
            head.val += carry
            carry = head.val // 10
            head.val = head.val % 10
            head = head.next

        if carry > 0:
            prev.next = Node(carry)
        return self.reverse()

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    L = LinkedList()
    L.append(9)
    L.append(9)
    L.append(9)
    L.display()
    L.reverse()
    L.display()
    L.add1()
    L.display()
