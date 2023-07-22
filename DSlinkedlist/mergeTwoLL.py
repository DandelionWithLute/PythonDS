class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

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


def mergeLists(headA, headB):
    dummyNode = Node(0)
    tail = dummyNode
    while True:
        # If any of the list gets completelyempty directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
            # Compare the data of the lists and whichever is smaller is appended to the last of the merged list and the head is changed
        if headB is None:
            tail.next = headA
            break
        if headA.val <= headB.val:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    return dummyNode.next


if __name__ == "__main__":
    LA = LinkedList()
    LA.append(5)
    LA.append(10)
    LA.append(15)
    LA.display()
    LB = LinkedList()
    LB.append(2)
    LB.append(3)
    LB.append(20)

    LA.head = mergeLists(LA.head, LB.head)
    LA.display()
