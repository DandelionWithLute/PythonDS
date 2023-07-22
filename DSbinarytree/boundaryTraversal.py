class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printLeaves(root):
    if root:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.val)

        printLeaves(root.right)


def printBoundaryLeft(root):
    if root:
        if root.left:
            print(root.val)
            printBoundaryLeft(root.left)
        elif root.right:
            print(root.val)
            printBoundaryLeft(root.right)


def printBoundaryRight(root):
    if root:
        if root.right:
            printBoundaryRight(root.right)
            print(root.val)
        elif root.left:
            printBoundaryLeft(root.left)
            print(root.val)


def printBoundary(root):
    if root:
        print(root.val)
        printBoundaryLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printBoundaryRight(root.right)


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    printBoundary(root)
