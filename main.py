from BinarySearch import binary_search, binary_search_binary
import random
from BubbleSort import BubbleSort
import random

#random_numbers = [10, 9 ,8, 7 ,6, 5, 4, 3, 2, 1]
random_numbers = [random.randint(100, 10000) for _ in range(10000)]
print("Unsorted: " + str(random_numbers))
print("Sorted: " + str(BubbleSort(random_numbers)))


