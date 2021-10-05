from math import log
import time
import random
import sys

swap_times = 0

def quick_sort(arr):
    global swap_times

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        swap_times += len(left) + len(right)
        return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)

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
