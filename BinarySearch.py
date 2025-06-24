# Function for Iterative Binary Search
def binary_search(arr, target):
    low = 0  # Start index of the array
    high = len(arr) - 1  # End index of the array
    
    # Loop till low <= high
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        if arr[mid] == target:
            return mid  # Target found at mid index
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Target not found

# Main program
if __name__ == "__main__":
    # Sorted array to search
    arr = [2, 4, 6, 7, 9, 12, 15, 18, 21, 67,98,101]
    
    # User input for target number
    target = int(input("Enter the number to search: "))
    
    # Call iterative binary search
    index = binary_search(arr, target)
    
    # Show the results
    if index != -1:
        print(f"Iterative: Number {target} found at position: {index + 1}")
    else:
        print(f"Iterative: Number {target} not found.")



# Function for Recursive Binary Search
def binary_search_recursive(arr, target, low, high):
    # Base case: If low exceeds high, target not found
    if low > high:
        return -1
    
    mid = (low + high) // 2  # Find middle index
    
    if arr[mid] == target:
        return mid  # Target found at mid
    elif arr[mid] < target:
        # Search in right half
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        # Search in left half
        return binary_search_recursive(arr, target, low, mid - 1)

# Main program
if __name__ == "__main__":
    # Sorted array to search
    arr = [2, 4, 6, 7, 9, 12, 15, 18, 21]
    
    # User input for target number
    target = int(input("Enter the number to search: "))
    
    # Call recursive binary search
    index = binary_search_recursive(arr, target, 0, len(arr) - 1)
    
    # Show the results
    if index != -1:
        print(f"Recursive: Number {target} found at index: {index}")
    else:
        print(f"Recursive: Number {target} not found.")