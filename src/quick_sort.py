from math import log
import time
import random
import sys

swap_times = 0
comparison_quantity = 0


def quick_sort_log():
    global swap_times
    global comparison_quantity

    logs = []

    sys.setrecursionlimit(100000)

    for i in range(20):
        # test quick sort to random list with 100 elements
        swap_times = 0
        comparison_quantity = int(1000 * log(1000))
        arr = [random.randint(0, 100) for i in range(1000)]
        start_time = time.time()
        quick_sort_desc(arr)
        logs.append([1000, time.time() - start_time,
                    swap_times, comparison_quantity])

    f = open('../logs/quick_sort_log.txt', "w")

    f.write("quick sort log:\n")
    f.write("number of elements, time, number of swaps, number of comparisons\n")
    for i in range(len(logs)):
        f.write(str(logs[i][0]) + ", " + str(logs[i][1]) +
                ", " + str(logs[i][2]) + ", " + str(logs[i][3]) + "\n")

    f.close()


def quick_sort_desc(arr):
    global swap_times

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x >= pivot]
        right = [x for x in arr[1:] if x < pivot]
        swap_times += len(left) + len(right)
        return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)


quick_sort_log()
