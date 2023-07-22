# utility function to return new node
class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isFoldable(root):
    if root is None:
        return True
    return isFoldableUtil(root.left, root.right)


def isFoldableUtil(n1, n2):
    if n1 == None and n2 == None:
        return True
    if n1 != None or n2 != None:
        return False
    d1 = isFoldableUtil(n1.left, n2.right)
    d2 = isFoldableUtil(n1.right, n2.left)
    return d1 and d2


# Driver code
if __name__ == "__main__":
 
    """ The constructed binary tree is 
    1 
    / \ 
    2 3 
    \ / 
    4 5 
"""
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(4)
    root.right.left = newNode(5)
 
    if isFoldable(root):
        print("tree is foldable")
    else:
        print("tree is not foldable")
 
# This code is contributed by
# Anupam Baranwal(anupambaranwal)
