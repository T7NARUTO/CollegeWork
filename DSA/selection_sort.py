def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


while True:
    print("1. Initialise the Array.")
    print("2. Sort the array using Selection Sort.")
    print("3. Exit.")
    option = int(input("Select an option to continue: "))

    if option == 1:
        arr = []
        n = int(input("Enter the size of the array: "))
        for i in range(n):
            element = int(input(f"Enter the {i+1}th element of the array: "))
            arr.append(element)
    elif option == 2:
        if 'arr' in locals():
            sorted_arr = selection_sort(arr)
            print("Sorted array using Selection Sort:", sorted_arr)
        else:
            print("Please initialize the array first.")
    elif option == 3:
        break
    else:
        print("Invalid option. Please select again.")
