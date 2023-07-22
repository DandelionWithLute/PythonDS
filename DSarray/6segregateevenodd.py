def segregate(arr, n):
    temp = n * [0]
    p, q = 0, n - 1
    for i in range(n):
        if arr[i] % 2 == 0:
            temp[p] = arr[i]
            p += 1
        else:
            temp[q] = arr[i]
            q -= 1
    print(temp)


# arr = [1, 9, 5, 3, 2, 6, 7, 11]
arr = [ 1, 3, 2, 4, 7, 6, 9, 10 ]
n = len(arr)
segregate(arr, n)
