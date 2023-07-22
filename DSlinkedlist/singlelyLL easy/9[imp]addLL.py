# Python code to add two nodes by reversing the two lists

# Node class for linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# LinkedList class
class LinkedList:
	# Function to reverse the linked list and
	# return the head of the reversed list
	def reverse_list(self, list):
		prev = None
		curr = list
		next = None
		while curr is not None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev

	# Function that calculates and prints the sum
	# of two numbers represented by linked lists
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

		self.print_list(sum_list)

	# Utility function to print a linked list
	def print_list(self, head):
		while head.next is not None:
			print(head.data, end=" ")
			head = head.next
		print(head.data)


# Test the LinkedList class
linked_list = LinkedList()

# Create first list
linked_list.head1 = Node(7)
linked_list.head1.next = Node(5)
linked_list.head1.next.next = Node(9)
linked_list.head1.next.next.next = Node(4)
linked_list.head1.next.next.next.next = Node(6)

# Create second list
linked_list.head2 = Node(8)
linked_list.head2.next = Node(4)

print("Sum is:", end = " ")
# Add the two lists and see the result
linked_list.add_two_lists(linked_list.head1, linked_list.head2)

# This code is contributed by lokeshmvs21.
