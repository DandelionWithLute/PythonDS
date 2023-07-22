class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getLevelUtil(node, val, level):
    if node is None:
        return
    if node.val == val:
        return level
    downlevelLeft = getLevelUtil(node.left, val, level + 1)
    downlevelRight = getLevelUtil(node.right, val, level + 1)
    return downlevelLeft or downlevelRight


def getLevel(node, val):
    return getLevelUtil(node, val, 1)


if __name__ == "__main__":
    # Let us construct the Tree shown
    # in the above figure
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(1)
    root.left.right = newNode(4)
    for x in range(1, 6):
        level = getLevel(root, x)
        if level:
            print("Level of", x, "is", getLevel(root, x))
        else:
            print(x, "is not present in tree")

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
