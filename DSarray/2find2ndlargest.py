# arr = [1]
arr = [1,2,54,5342,3]
arr.sort()
len = len(arr)
#validate input
if len < 2:
    print("Invalid input")
# print(arr[len-2]) Totally wrong, you forgot to check the circumstances of the same.
for i in range(len-2,-1,-1):
    if arr[i] != arr[len-1]:
        print(arr[i])
        break