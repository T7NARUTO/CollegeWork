def linear_search(array, value):
    len_arr = len(array)
    i = 0
    while i < len_arr:
        if array[i] == value:
            pos = i
            return print(f'element found at position {pos}. ')
        i += 1
    return print('element not found')


while True:
    print("1.Initialise the Array. "
          "2.Search for elements using Linear search. "
          "3.Exit. ")
    options = int(input('Select a Option to continue. '))
    if options == 1:
        arr = []
        n = int(input("Enter the size of the array. "))
        for i in range(n):
            element = int(input(f"Enter the {i} element of the array. "))
            arr.append(element)
        continue
    elif options == 2:
        sc = int(input("Enter the Element to search in the array. "))
        linear_search(arr, sc)
    elif options == 3:
        break
