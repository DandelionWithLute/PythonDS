class newnode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sumSubtreeUtil(ptr, cur_sum, sum):
    if ptr is None:
        cur_sum[0] = 0
        return False
    sum_left, sum_right = [0], [0]
    x = sumSubtreeUtil(ptr.left, sum_left, sum)
    y = sumSubtreeUtil(ptr.right, sum_right, sum)
    cur_sum[0] = sum_left[0] + sum_right[0] + ptr.val
    return x or y or cur_sum[0] == sum


def sumSubtree(root, sum):
    cur_sum = [0]
    return sumSubtreeUtil(root, cur_sum, sum)


# Driver Code
if __name__ == "__main__":
    root = newnode(8)
    root.left = newnode(5)
    root.right = newnode(4)
    root.left.left = newnode(9)
    root.left.right = newnode(7)
    root.left.right.left = newnode(1)
    root.left.right.right = newnode(12)
    root.left.right.right.right = newnode(2)
    root.right.right = newnode(11)
    root.right.right.left = newnode(3)
    sum = 22

    if sumSubtree(root, sum):
        print("Yes")
    else:
        print("No")

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
