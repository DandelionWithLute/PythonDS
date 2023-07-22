# Python code to add two nodes by reversing the two lists


# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
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

    def reverse_list(self, list):
        current = list
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add_two_lists(self, first, second):
        # Reverse both lists
        first = self.reverse_list(first)
        second = self.reverse_list(second)
        carry = 0
        head = None
        prev = None
        sum_list = None
        # Add the two lists and carry over if necessary
        while first is not None or second is not None or carry == 1:
            new_val = carry
            if first is not None:
                new_val += first.data
            if second is not None:
                new_val += second.data
            carry = new_val // 10
            new_val = new_val % 10
            # Create a new node for the sum and append it
            # to the beginning of the final ans list
            new_node = Node(new_val)
            new_node.next = sum_list
            sum_list = new_node
            # Initialize nodes for the next iteration
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        self.display(sum_list)

    def display(self, list):
        current = list
        while current is not None:
            print(current.data, end=" ")
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
    L.add_two_lists(A.head, B.head)
