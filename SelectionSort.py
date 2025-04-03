def selectionSort(lst):
    n = len(lst)
    pass_count = 0
    swap_count = 0
    comparison_count = 0

    for i in range(n - 1):  # Only need to loop until n-1
        min_index = i
        pass_count += 1
        for j in range(i + 1, n):
            comparison_count += 1  # Count each comparison
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:  # Swap only when needed
            lst[i], lst[min_index] = lst[min_index], lst[i]
            swap_count += 1

    print("Passes:", pass_count)
    print("Swaps:", swap_count)
    print("Comparisons:", comparison_count)
    return lst
