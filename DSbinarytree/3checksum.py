class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum(root):
    if root == None:
        return 0
    return sum(root.left) + root.val + sum(root.right)


def isSumTree(node):
    if node == None or node.left == None and node.right == None:
        return 1
    ls = sum(node.left)
    rs = sum(node.right)
    if node.val == ls + rs and isSumTree(node.left) and isSumTree(node.right):
        return 1
    return 0


if __name__ == "__main__":
    root = node(26)
    root.left = node(10)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(6)
    root.right.right = node(3)

    if isSumTree(root):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")
