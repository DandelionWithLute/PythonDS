def printdistinct(arr, n):
    s = dict()
    for i in range(n):
        if arr[i] not in s.keys():
            s[arr[i]] = arr[i]
            print(arr[i], end=" ")


arr = [10, 5, 3, 4, 3, 5, 6]
n = len(arr)
printdistinct(arr, n)
