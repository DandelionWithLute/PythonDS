class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def postOrderIterative(node):
    if node is None:
        return
    s1 = []
    s2 = []

    s1.append(node)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        node = s2.pop()
        print(node.val, end=" ")

        # print(s1.pop(node.val), end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrderIterative(root)
