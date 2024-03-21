def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
x = 30
result = linear_search(arr, x)
if result != -1:
    print("Element", x, "found at index", result)
else:
    print("Element", x, "not found in the array")
