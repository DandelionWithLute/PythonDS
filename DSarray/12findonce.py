def findSingle(arr, n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return -1


arr = [2, 3, 5, 4, 5, 3, 4]
n = len(arr)
print("Element occurring once is", findSingle(arr, n))
