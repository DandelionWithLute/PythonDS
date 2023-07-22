class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isFoldable(node):
    if node == None:
        return True
    mirror(node.left)
    res = isStructSame(node.left, node.right)
    mirror(node.left)
    return res


def isStructSame(a, b):
    if a == None and b == None:
        return True
    if (
        a != None
        and b != None
        and isStructSame(a.left, b.left)
        and isStructSame(a.right, b.right)
    ):
        return True
    return False


def mirror(node):
    if node is None:
        return
    else:
        mirror(node.left)
        mirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp


# Driver Code
if __name__ == "__main__":
    """
    The constructed binary tree is
             1
           /   \
          2     3
           \    /
            4  5
    """
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.right.left = newNode(4)
    root.left.right = newNode(5)

    if isFoldable(root):
        print("tree is foldable")
    else:
        print("Tree is not foldable")
