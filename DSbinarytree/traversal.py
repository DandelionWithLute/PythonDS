class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traversal(node):
    if node:
        print(node.val, end=" ")
        traversal(node.left)
        traversal(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    traversal(root)
