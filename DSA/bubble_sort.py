def Bubble_sort(arr):
    len_arr = len(arr)
    while len_arr > 0:
        i = 0
        while i < len_arr - 1:
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            i += 1
        len_arr -= 1
    return arr


n = int(input("Enter the size of the Array"))
arr = []
for i in range(n):
    el = int(input(f"Enter the {i + 1} element of the array "))
    arr.append(el)
print(arr)
Bubble_sort(arr)
print(arr)
