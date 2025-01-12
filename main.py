import random
import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def timsort(arr):
    return sorted(arr)

def measure_time(algorithm, data):
    setup_code = f"from __main__ import {algorithm}, random_data"
    stmt = f"{algorithm}(random_data.copy())"
    return timeit.timeit(stmt=stmt, setup=setup_code, number=5)

data_sizes = [100, 1000, 10000]
results = []

for size in data_sizes:
    random_data = [random.randint(0, 100000) for _ in range(size)]

    print(f"\n{size} елементів:")
    for algo in ["insertion_sort", "merge_sort", "timsort"]:
        time = measure_time(algo, random_data)
        results.append((algo, size, time))
        print(f"Алгоритм {algo}: {time:.5f} секунд")
