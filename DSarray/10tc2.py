def CountTriangles(A):
    n = len(A)
    A.sort()
    count = 0
    for i in range(n - 1, 0, -1):
        l = 0
        r = i - 1
        while l < r:
            if A[l] + A[r] > A[i]:
                count += r - 1


# Driver Code
if __name__ == "__main__":
    A = [10, 21, 22, 100, 101, 200, 300]

    # Function call
    CountTriangles(A)

# This code is contributed by PrinciRaj1992
