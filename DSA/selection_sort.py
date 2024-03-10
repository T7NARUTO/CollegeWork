import datetime as time
import matplotlib.pyplot as plt
import random


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def measure_time_complexity_selection_sort(arr_size):
    ary = [random.randint(0, arr_size) for i in range(arr_size)]
    start_time = time.datetime.now()
    selection_sort(ary)
    end_time = time.datetime.now()
    return (end_time - start_time).total_seconds()


x = [500, 1000, 1500]  # Input sizes
y_selection_sort = []

for size in x:
    y_selection_sort.append(measure_time_complexity_selection_sort(size))

plt.bar([str(size) for size in x], y_selection_sort)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Selection Sort Time Complexity')
plt.show()
