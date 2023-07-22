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

    # There must be a value of head passed
    def reverseMy(self, head):
        # prev=None
        # next=None
        # current=self.head
        # while current:
        #     next=current.next
        #     current.next=prev
        #     prev=current
        #     current=next
        # self.head=prev
        if self.head is None or self.head.next is None:
            return None

        rec = self.reverse(self.next)
        self.head.next.next = self.head
        self.head.next = None
        return rec

    def reverse(self, head):
        # If head is empty or has reached the list's end
        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest


if __name__ == "__main__":
    L = LinkedList()
    # adding elements to the linked list
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.display()
    L.head = L.reverse(L.head)
    # L.reverse(L.head)
    # L.head = L.reverse(L.head)
    L.display()
