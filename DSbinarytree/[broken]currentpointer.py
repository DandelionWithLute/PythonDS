class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftToRight(root):
    curr = root
    while curr:
        # If left child is null, print the
        # current node data. And, update
        # the current pointer to right child.
        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(leftToRight(root))
