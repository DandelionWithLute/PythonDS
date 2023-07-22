def assign(a, n):
    a.sort()

    ans = n * [0]
    p = 0
    q = n - 1
    for i in range(n):
        # Assign even indexes with
        # maximum elements
        if (i + 1) % 2 == 0:
            ans[i] = a[q]
            q = q - 1
        else:
            ans[i] = a[p]
            p += 1

    for i in range(n):
        print(ans[i])


A = [1, 3, 2, 2, 5]
n = len(A)
assign(A, n)
