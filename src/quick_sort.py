import time
import random
import sys

swap_times = 0


def quick_sort_log():
    global swap_times

    logs = []

    sys.setrecursionlimit(100000)

    # test quick sort to random list with 100 elements
    swap_times = 0
    arr = [random.randint(0, 100) for i in range(100)]
    start_time = time.time()
    quick_sort_desc(arr)
    logs.append([100, time.time() - start_time, swap_times])

    # test quick sort to random list with 1000 elements
    swap_times = 0
    arr = [random.randint(0, 100) for i in range(1000)]
    start_time = time.time()
    quick_sort_desc(arr)
    logs.append([1000, time.time() - start_time, swap_times])

    # test quick sort to random list with 10000 elements
    swap_times = 0
    arr = [random.randint(0, 100) for i in range(10000)]
    start_time = time.time()
    quick_sort_desc(arr)
    logs.append([10000, time.time() - start_time, swap_times])

    # test quick sort to random list with 100000 elements
    swap_times = 0
    arr = [random.randint(0, 100) for i in range(100000)]
    start_time = time.time()
    quick_sort_desc(arr)
    logs.append([100000, time.time() - start_time, swap_times])

    f = open("../logs/quick_sort_log.txt", "w")

    f.write("quick sort log:\n")
    f.write("number of elements, time, number of comparisons\n")
    for i in range(len(logs)):
        f.write(str(logs[i][0]) + ", " + str(logs[i][1]) +
                ", " + str(logs[i][2]) + "\n")

    f.close()


def quick_sort_desc(arr):
    global swap_times

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x >= pivot]
        right = [x for x in arr[1:] if x < pivot]
        swap_times += 1
        return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)


quick_sort_log()
