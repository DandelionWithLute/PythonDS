class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(1 + lheight + rheight, max(ldiameter, rdiameter))
    # return max( ldiameter + rdiameter, max(lheight, rheight))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.left.left.left = Node(6)
    # root.left.left.left.left = Node(6)

print(diameter(root))
print(height(root))
