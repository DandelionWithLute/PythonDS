class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def count(root):
    if root is None:
        return 0
    return count(root.left)+count(root.right)+1

def checkRec(root,n):
    if root is None:
        return False
    if count(root) == n - count(root):
        return True
    return checkRec(root.left,n) or checkRec(root.right,n)

def check(root):
    n=count(root)
    return checkRec(root,n)

if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(1)
    root.right = newNode(6)
    root.left.left = newNode(3)
    root.right.left = newNode(7)
    root.right.right = newNode(4)
 
    if check(root):
        print("YES")
    else:
        print("NO")
         
# This code is contributed by PranchalK