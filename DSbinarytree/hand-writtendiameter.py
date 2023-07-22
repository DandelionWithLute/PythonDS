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
    if node is None:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)

    ldiameter = diameter(node.left)
    rdiameter = diameter(node.right)

    return max(1 + lheight + rheight, max(ldiameter, rdiameter))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(diameter(root))
