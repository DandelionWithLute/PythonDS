import sys

def print3largest(arr,arr_size):
    if (arr_size < 3):
        print(" Invalid input");
        return 
    
    third = first = second = -sys.maxsize
    for i in range(arr_size):
        if (arr[i] > first):
            third = second
            second = first
            first = arr[i]
        elif (arr[i] > second):
            third = second
            second = arr[i]
        elif (arr[i] > third):
            third = arr[i]
    print("The 3 largest elements are", first, second, third)

arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)