def bubbleSort(lst):
    n = len(lst)
    pass_count = 0
    swap_count = 0
    comparison_count = 0
    sorted = False

    while not sorted:
        sorted = True
        pass_count += 1  # Count each pass through the list

        for i in range(n - 1):
            comparison_count += 1  # Count each comparison
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap_count += 1  # Count each swap
                sorted = False  # If a swap happens, the list isn't sorted yet

    print("Passes:", pass_count)
    print("Swaps:", swap_count)
    print("Comparisons:", comparison_count)
    return lst


