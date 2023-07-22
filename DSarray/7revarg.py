def revarg(arr, n, d):
    temp = n * [0]
    for i in range(n):
        if i < n - d:
            temp[i] = arr[i + d]
        else:
            temp[i] = arr[i - (n - d)]
    return temp


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
print(revarg(arr, n, d))