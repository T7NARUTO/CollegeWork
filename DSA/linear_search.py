import datetime as time
import matplotlib.pyplot as plt
import random


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def measure_time_complexity_linear_search(arr_size):
    ary = [random.randint(0, arr_size) for i in range(arr_size)]
    target = random.randint(0, arr_size)
    start_time = time.datetime.now()
    linear_search(ary, target)
    end_time = time.datetime.now()
    return (end_time - start_time).total_seconds()


x = [500, 1000, 1500]  # Input sizes
y_linear_search = []

for size in x:
    y_linear_search.append(measure_time_complexity_linear_search(size))

plt.bar([str(size) for size in x], y_linear_search)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Linear Search Time Complexity')
plt.show()
