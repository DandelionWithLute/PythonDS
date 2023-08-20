class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def inOrder(node):
    current = node
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right
        else:
            break
    print()


# Driver program to test above function
if __name__ == "__main__":
    """ Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    inOrder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
