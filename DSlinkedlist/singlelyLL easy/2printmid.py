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

    # just forget this wrong one
    # def getMid(self, head):
    #     slow = head
    #     fast = head
    #     current = head
    #     while current:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if fast.next or fast.next.next is None:
    #             return slow.val

    def getMiddle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.val

    def get2Mid(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        current = head
        count = 0
        while current:
            current = current.next
            count += 1
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        if count % 2 == 0:
            slow = slow.next
            return slow.val
        else:
            return slow.val


if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.append(6)
    # L.append(7)
    L.head = L.get2Mid(L.head)
    print(L.head)
