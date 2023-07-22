class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def append(self, val):
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()

    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.val <= b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    L = LinkedList()
    L.append(15)
    L.append(10)
    L.append(5)
    L.append(20)
    L.append(3)
    L.append(2)
    L.display()
    L.head = L.mergeSort(L.head)
    L.display()