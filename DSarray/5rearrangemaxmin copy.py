def rea(a, n):
    temp = n * [0]
    p, q = 0, n - 1
    flag = True
    for i in range(n):
        if flag:
            temp[i] = a[p]
            p += 1
            flag = not flag
        else:
            temp[i] = a[q]
            q -= 1
            flag = not flag
    print(temp)


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
rea(arr, n)
