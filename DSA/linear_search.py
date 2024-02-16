def linear_search(array ,value):
    len_arr = len(array)
    pos = None
    i = 0
    while i < len_arr:
        if array[i] == value:
            pos = i
            return print(f'element found at position {pos}')
        i += 1
    return print('element not found')


n = int(input("Enter the size of the Array"))
arr = []
for i in range(n):
    el = int(input(f"Enter the {i + 1} element of the array "))
    arr.append(el)
print(arr)
linear_search(arr, 30)
