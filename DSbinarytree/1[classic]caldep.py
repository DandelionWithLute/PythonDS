def findDepthRec(tree, n, index):
    if index >= n or tree[index] == "l":
        return 0
    index += 1
    left = findDepthRec(tree, n, index)
    index += 1
    right = findDepthRec(tree, n, index)
    return max(left, right) + 1


if __name__ == "__main__":
    tree = "nlnnlllnllnllnllnllnllnllnll"
    n = len(tree)
    print(findDepthRec(tree, n, 0))

# def findDepth(tree, n):
#     index = 0
#     return findDepthRec(tree, n, index)