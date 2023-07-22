# O(N) Low time complexity
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.h = 0


def diameterOpt(root, height):
    lh = Height()
    rh = Height()

    if root is None:
        height.h = 0
        return 0

    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)

    height.h = max(lh.h, rh.h) + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))


def diameter(root):
    height = Height()
    return diameterOpt(root, height)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    """
  Constructed binary tree is
              1
          /   \
          2      3
        /  \
      4     5
  """

    print("The diameter of the binary tree is:", end=" ")
    # Function Call
    print(diameter(root))

# This code is contributed by Shweta Singh(shweta44)
