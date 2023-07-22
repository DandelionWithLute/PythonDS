def findDepByRec(tree, n, index):
    if index >= n or tree[index] == "l":
        return 0
    index += 1
    left = findDepByRec(tree, n, index)
    index += 1
    right = findDepByRec(tree, n, index)
    return max(left, right) + 1


if __name__ == "__main__":
    tree = "nlnnlll"
    n = len(tree)
    print(findDepByRec(tree, n, 0))
