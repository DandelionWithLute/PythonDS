class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printLevelOrder(node):
    h = height(node)

    for i in range(1 + h):
        printCurrentLevel(node, i)


def printCurrentLevel(node, level):
    if node is None:
        return 0
    if level == 1:
        print(node.val, end=" ")
    if level > 1:
        printCurrentLevel(node.left, level - 1)
        printCurrentLevel(node.right, level - 1)


def height(node):
    if node is None:
        return 0
    left = height(node.left)
    right = height(node.right)
    return max(left, right) + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is -")
    printLevelOrder(root)
