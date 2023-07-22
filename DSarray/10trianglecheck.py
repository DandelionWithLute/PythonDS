def findNumberOfTriangles(arr, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (
                    arr[i] + arr[j] > arr[k]
                    and arr[i] + arr[k] > arr[j]
                    and arr[j] + arr[k] > arr[i]
                ):
                    count += 1
    return count

if __name__ == "__main__":
    arr = [10, 21, 22, 100, 101, 102, 200, 300]
    size = len(arr)
    # functional call
    print("Total number of triangles possible is ", findNumberOfTriangles(arr, size))
