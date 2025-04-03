def insertionSort(lst):
    n = len(lst)
    pass_count = 0
    swap_count = 0
    comparison_count = 0

    for i in range(1, n):
        pass_count += 1
        key = lst[i]
        j = i - 1

        # Move elements that are greater than key one position ahead
        while j >= 0:
            comparison_count += 1  # Each iteration is a comparison
            if lst[j] > key:
                lst[j + 1] = lst[j]
                swap_count += 1  # Treat shifting as a swap
            else:
                break  # No need for further comparisons
            j -= 1

        lst[j + 1] = key  # Insert key in the correct position

    print("Passes:", pass_count)
    print("Swaps:", swap_count)
    print("Comparisons:", comparison_count)
    return lst
