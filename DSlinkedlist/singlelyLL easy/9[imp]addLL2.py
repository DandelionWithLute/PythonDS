class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def reverse(self, list):
        prev = None
        current = list
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def add2(self, first, second):
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        sumList = None
        while first or second or carry == 1:
            newVal = carry
            if first is not None:
                newVal += first.data
            if second is not None:
                newVal += second.data
            carry = newVal // 10
            newVal %= 10

            newNode = Node(newVal)
            newNode.next = sumList
            sumList = newNode

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        self.printList(sumList)

    def printList(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next
        print()


L = LinkedList()
L.head1 = Node(7)
L.head1.next = Node(5)
L.head1.next.next = Node(9)
L.head1.next.next.next = Node(4)
L.head1.next.next.next.next = Node(6)
L.head2 = Node(8)
L.head2.next = Node(4)
print("Sum is:", end=" ")
L.add2(L.head1, L.head2)