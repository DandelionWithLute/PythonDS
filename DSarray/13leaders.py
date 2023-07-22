def printLeaders(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] <= arr[j]:
                break
        if j == n - 1:  # this is for the last one
            print(arr[i], end=" ")


arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
print(printLeaders(arr, n))