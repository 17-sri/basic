def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# User input
input_str = input("Enter array elements separated by spaces: ")
arr = list(map(int, input_str.strip().split()))
arr.sort()  # Sort the array to ensure binary search works
print("Sorted array:", arr)

x = int(input("Enter the element to search for: "))

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
