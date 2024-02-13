def linear_search(arr,value):
    len_arr = len(arr)
    pos = None
    i = 0
    while i < len_arr:
        if arr[i] == value:
            pos = i
            return print(f'element found at position {pos}')
        i += 1
    return print('element not found')


arr = [10,11,20,30]
linear_search(arr,30)
