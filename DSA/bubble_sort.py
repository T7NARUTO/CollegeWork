import datetime as time
import matplotlib.pyplot as plt
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def measure_time_complexity_bubble_sort(arr_size):
    ary = [random.randint(0, arr_size) for i in range(arr_size)]
    start_time = time.datetime.now()
    bubble_sort(ary)
    end_time = time.datetime.now()
    return (end_time - start_time).total_seconds()


x = [500, 1000, 1500]  # Input sizes
y_bubble_sort = []

for size in x:
    y_bubble_sort.append(measure_time_complexity_bubble_sort(size))

plt.bar([str(size) for size in x], y_bubble_sort)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Bubble Sort Time Complexity')
plt.show()
