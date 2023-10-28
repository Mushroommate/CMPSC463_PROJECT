import threading

# check sorted or not
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# check sorted reversely or not
def is_reverse_sorted(arr):
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

# Define if there's duplicate
def duplicates(arr):
    from collections import Counter
    counts = Counter(arr)
    return max(counts.values()) > len(arr) / 2

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# Define bubble_sort function for nearly sorted arrays
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def parallel_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]


        left_thread = threading.Thread(target=parallel_merge_sort, args=(L,))
        right_thread = threading.Thread(target=parallel_merge_sort, args=(R,))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def parallel_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]


        left_thread = threading.Thread(target=parallel_quick_sort, args=(left,))
        right_thread = threading.Thread(target=parallel_quick_sort, args=(right,))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        return quicksort(left) + [pivot] + quicksort(right)

# with the heuristics 
def hybrid_sort(arr):
    min_run = 64
    n = len(arr)

    # Heuristic 1: 
    if is_sorted(arr):
        return arr
    if is_reverse_sorted(arr):
        reversed(arr)
        return arr

    # Heuristic 2: Insertion Sort for small arr
    if n <= min_run:
        insertionsort(arr)
        return arr

    # Heuristic 3: Counting Sort for duplicate
    if duplicates(arr):
        counting_sort(arr)
        return arr

    # Heuristic 4: Bubble sort for nearly sorted arr
    if is_nearly_sorted(arr):
        bubblesort(arr)
        return arr

    # Heuristic 5: Merge Sort and Quick Sort For medium-sized arr
    if n <= 10000:
        mergesort(arr)
        quicksort(arr)
        return arr

    # Heuristic 6: Parallel Sort for larger arr
    if n > 10000:
        parallel_merge_sort(arr)
        parallel_quick_sort(arr)
        return arr


if __name__ == "__main__":
    arr = [320, 323, 444, 2888, 2901, 9038, 29681]
    result = hybrid_sort(arr)
    print(result)

""""
import time


# Record the start time
start_time = time.time()

# Call the sorting function
hybrid_sort(arr)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
execution_time = end_time - start_time

# Print the execution time
print("Execution Time:", execution_time, "seconds")
"""

"""from memory_profiler import profile

@profile
def main():
    # Call the sorting function
    hybrid_sort(arr)

if __name__ == "__main__":
    main()
"""