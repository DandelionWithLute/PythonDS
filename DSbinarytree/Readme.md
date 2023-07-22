diameter!=height in binary tree

 try:
     diagonalPrintMap[d].append(root.val)
 except KeyError:
     diagonalPrintMap[d] = [root.val]


d:\Programming\python\DSbinarytree\diagonalTraversal2.py:28: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if __name__ is "__main__":


def diagonalPrint(root):
diagonalPrintMap = dict()
diagonalPrintUtil(root, 0, diagonalPrintMap)
for i in diagonalPrintMap:
    for j in diagonalPrintMap[i]:
        print(j, end=" ")
        # j can't be root.val or [8] [8] [8] [8] [8] [8] [8] [8] [8] 
    print()


4 If it's not on the left,the function will be dead.
def level(root, ptr, lev):
     
    # Base Case
    if root is None :
        return 0
    if root == ptr:
        return lev
 
    # Return level if Node is present in left subtree
    l = level(root.left, ptr, lev+1)
    if l != 0:
        return l
 
    # Else search in right subtree
    return level(root.right, ptr, lev+1)


def isPerfectRec(root, d, level = 0):
     
    # An empty tree is perfect
    if (root == None):
        return True
 
    # If leaf node, then its depth must
    # be same as depth of all other leaves.
    if (root.left == None and root.right == None):
        return (d == level + 1)
 
    # If internal node and one child is empty
    if (root.left == None or root.right == None):
        return False
 
    # Left and right subtrees must be perfect.
    return (isPerfectRec(root.left, d, level + 1) and
            isPerfectRec(root.right, d, level + 1))


def isMirror(root1, root2):
def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (
        root1.val == root2.val
        and areIdentical(root1.left, root2.left)
        and areIdentical(root1.right, root2.right)
    )


def identicalTrees(a, b):
    # 1. Both empty
    if a is None and b is None:
        return True

    # 2. Both non-empty -> Compare them
    if a is None or b is None:
        # 3. one empty, one not -- false
        return False
    return (
        (a.data == b.data)
        and identicalTrees(a.left, b.left)
        and identicalTrees(a.right, b.right)
    )


def identicalTrees(a, b):
 
    # 1. Both empty
    if a is None and b is None:
        return True
 
    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right))
 
    # 3. one empty, one not -- false
    return False
 