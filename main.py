from BubbleSort import bubbleSort
from SelectionSort import selectionSort
from InsertionSort import insertionSort
import random
import time

# random_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
random_numbers = [random.randint(100, 10000) for _ in range(10000)]

# print("Unsorted: " + str(random_numbers))

start_time = time.time()
print ("Sorted: " + str(insertionSort(random_numbers)))
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.10f} seconds")