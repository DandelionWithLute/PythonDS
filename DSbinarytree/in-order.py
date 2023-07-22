class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # Then print the data of node
        print(root.val, end=" ")

        # First recur on left child
        printInorder(root.left)

        # Now recur on right child
        printInorder(root.right)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # root.left.left.left = Node(8)
    # root.left.left.right = Node(9)
    # root.left.right.left = Node(10)
    # root.left.right.right = Node(11)
    # root.right.left.left = Node(12)
    # root.right.left.right = Node(13)
    # root.right.right.left = Node(14)
    # root.right.right.right = Node(15)

    # Function call
    print("Preorder traversal of binary tree is")
    printInorder(root)