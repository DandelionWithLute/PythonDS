class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.last = None
        self.head = None

    def append(self, val):
        if self.last is None:
            self.last = Node(val)
            self.head = self.last
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def display(self, list):
        current = list
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def reverse(self, list):
        prev = None
        current = list
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        prev = self.head

    def addTwo(self, first, second):
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        sum_list = None
        while first is not None or second is not None or carry == 1:
            new_val = carry
            if first is not None:
                new_val += first.val
            if second is not None:
                new_val += second.val
            carry = new_val // 10
            new_val %= 10

            new_node = Node(new_val)
            new_node.next = sum_list
            sum_list = new_node

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        self.display(sum_list)


if __name__ == "__main__":
    A = LinkedList()
    A.append(1)
    A.append(2)
    A.append(3)
    A.display(A.head)
    B = LinkedList()
    B.append(2)
    B.append(3)
    B.append(4)
    B.display(B.head)
    A.addTwo(A.head, B.head)
