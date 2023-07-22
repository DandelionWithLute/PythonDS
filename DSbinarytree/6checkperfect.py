class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findADepth(node):
    d = 0
    while node != None:
        d += 1
        node = node.left
    return d


def isPerfectRec(root, d, level=0):
    if root is None:
        return True
    if root.left == None and root.right == None:
        return d == level + 1
    if root.left == None or root.right == None:
        return False
    return isPerfectRec(root.left, d, level + 1) and isPerfectRec(
        root.right, d, level + 1
    )


def isPerfect(root):
    d = findADepth(root)
    return isPerfectRec(root, d)


if __name__ == "__main__":
    root = None
    root = newNode(10)
    root.left = newNode(20)
    root.right = newNode(30)

    root.left.left = newNode(40)
    root.left.right = newNode(50)
    root.right.left = newNode(60)
    root.right.right = newNode(70)

    if isPerfect(root):
        print("Yes")
    else:
        print("No")

# This code is contributed by pranchalK
