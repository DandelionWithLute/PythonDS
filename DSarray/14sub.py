def subArraySum(arr, n, sum):
    for i in range(n):
        currentSum = arr[i]
        if currentSum == sum:
            print("Sum found at indexes", i)
            return
        else:
            for j in range(i + 1, n):
                currentSum += arr[i]
                if currentSum == sum:
                    print("Sum found between indexes", i, "and", j)
                    return
    print("No Subarray Found")


# Driver Code
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum = 23
    subArraySum(arr, n, sum)
