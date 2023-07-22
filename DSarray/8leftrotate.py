# geeksforgeeks.org
# https://www.geeksforgeeks.org/print-left-rotation-array/?ref=lbp
# Python implementation of left rotation of
# an array K number of times
def leftRotate(arr, n, k):
    # To get the starting point of rotated array
    mod = k % n
    s = " "
    # Prints the rotated array from start position
    temp = n * [0]
    for i in range(n):
        print(arr[(mod + i) % n], end=" "),
    print
    return


# Driver code
arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2

# Function Call
leftRotate(arr, n, k)
