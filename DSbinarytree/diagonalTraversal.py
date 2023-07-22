class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diagonalPrintUtil(root, d, diagonalPrintMap):
    if root is None:
        return

    diagonalPrintMap[d].append(root.val)
    # try:
    #     diagonalPrintMap[d].append(root.val)
    # except KeyError:
    #     diagonalPrintMap[d] = [root.val]

    diagonalPrintUtil(root.left, d + 1, diagonalPrintMap)
    diagonalPrintUtil(root.right, d, diagonalPrintMap)


def diagonalPrint(root):
    diagonalPrintMap = dict()
    diagonalPrintUtil(root, 0, diagonalPrintMap)
    print("Diagonal Traversal of binary tree: ")
    for i in diagonalPrintMap:
        for j in diagonalPrintMap[i]:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    diagonalPrint(root)
