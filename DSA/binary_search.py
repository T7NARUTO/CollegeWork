def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


while True:
    print("1. Initialise the Sorted Array.")
    print("2. Search for an element using Binary Search.")
    print("3. Exit.")
    option = int(input("Select an option to continue: "))

    if option == 1:
        arr = []
        n = int(input("Enter the size of the sorted array: "))
        print("Enter the sorted elements of the array:")
        for i in range(n):
            element = int(input(f"Enter the {i+1}th element: "))
            arr.append(element)
        arr.sort()  # Sorting the array to ensure it's in ascending order

    elif option == 2:
        if 'arr' in locals():
            target = int(input("Enter the element to search: "))
            index = binary_search(arr, target)
            if index != -1:
                print(f"Element {target} found at index {index}.")
            else:
                print(f"Element {target} not found in the array.")
        else:
            print("Please initialize the array first.")
    elif option == 3:
        break
    else:
        print("Invalid option. Please select again.")
