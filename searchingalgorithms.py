# Session 5 : Searching Algorithms


# Linear Search
def search(List, k):

    for i in range(len(List)):
        if List[i] == k:
            return True
    
    return False


List = ["A","D","F","H","I",10,50,100,"math","coding"]

v = "math"

if search(List, v):
    print("Value found in list")
else:
    print("Value not found in list")

# Binary Search

def binary_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
   

    while low <= high:
        mid = (high + low) // 2
        
        if array[mid] < x:
            low = mid + 1

        elif array[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

#  array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 8

output = binary_search(array, x)

if output != -1:
    print("Element is present at index : ",str(output))
else:
    print("Element is not present in array")