
# Searching Algorithms


# Linear Search
def linear_search(book_list,target):

    for i, book in enumerate(book_list):
        if book.lower() == target.lower():
            return i
        
    return -1


library_books = ["All Good People Here", "The Challenge", "Overkill", "The 6-20 Man", "Wrong Place Wrong Time", "Portrait of an Unknown Women"]

target_book = "All Good People Here"

index = linear_search(library_books,target_book)

if index != -1:
    print("Element found at index : {}".format(index))
else:
    print("Element Not Found")
    

# Binary Search
def binary_search(medicine_list, target):
    low, high = 0, len(medicine_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if medicine_list[mid] == target:
            return mid
        elif medicine_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


pharmacy_medicines = [233,334,776,8776,11223,21123]

target_medicine = 334
result = binary_search(pharmacy_medicines,target_medicine)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element not found")