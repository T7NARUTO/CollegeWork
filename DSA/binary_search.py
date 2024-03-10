import datetime as time
import matplotlib.pyplot as plt
import random


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


def measure_time_complexity_binary_search(arr_size):
    ary = sorted([random.randint(0, arr_size) for i in range(arr_size)])
    target = random.randint(0, arr_size)
    start_time = time.datetime.now()
    binary_search(ary, target)
    end_time = time.datetime.now()
    return (end_time - start_time).total_seconds()


x = [5000, 10000, 15000]
y_binary_search = []

for size in x:
    y_binary_search.append(measure_time_complexity_binary_search(size))

plt.bar([str(size) for size in x], y_binary_search)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Binary Search Time Complexity')
plt.show()
