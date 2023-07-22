class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(node):
    lheight = height(node.left)
    rheight = height(node.right)
    return lheight + rheight + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function Call
    print(diameter(root))
