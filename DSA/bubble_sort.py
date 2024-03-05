def Bubble_sort(array):
    len_arr = len(array)
    while len_arr > 0:
        i = 0
        while i < len_arr - 1:
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
            i += 1
        len_arr -= 1
    return array


while True:
    print("1.Initialise the Array. "
          "2.Sort the array using Bubble sort. "
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
        Bubble_sort(arr)
        print(arr)
    elif options == 3:
        break
