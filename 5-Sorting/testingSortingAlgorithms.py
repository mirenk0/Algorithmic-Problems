import random
import time

# Merge Sort
def merge_sort(items):
    n = len(items)

    if n <= 1: return

    left = items[0:n//2]
    right = items[n//2:]

    merge_sort(left)
    merge_sort(right)

    a = b = 0
    for i in range(n):
        if b == len(right) or \
           (a < len(left) and left[a] < right[b]):
            items[i] = left[a]
            a += 1
        else:
            items[i] = right[b]
            b += 1

# Insertion Sort
def swap(items, a, b):
    temp = items[a]
    items[a] = items[b]
    items[b] = temp

def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i - 1, -1, -1):
            if items[j] > items[j + 1]:
                swap(items, j, j + 1)
            else:
                break


if __name__ == "__main__":
    n = 10**5
    random.seed(1337)
    numbers = [random.randint(1, n) for _ in range(n)]

    start_time_insertion = time.time()
    insertion_sort(numbers)
    end_time_insertion = time.time()

    start_time_merge = time.time()
    merge_sort(numbers)
    end_time_merge = time.time()

    start_time_sort = time.time()
    numbers.sort()
    end_time_sort = time.time()

    print(" ++++++ ")
    print("insertion sort time:", round(end_time_insertion - start_time_insertion, 2), "s")
    print("merge sort time:", round(end_time_merge - start_time_insertion, 2), "s")
    print("sort (timsort) time:", round(end_time_sort - start_time_sort, 2), "s")
    

