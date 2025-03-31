
def BubbleSort(list):
    list_length = len(list) - 1
    sorted = False
    pass_count = 0
    swap_count = 0

    while not sorted:
        sorted = True
        pass_count+=1

        for i in range(0, list_length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
                swap_count+=1

    print("Passes: " + str(pass_count))
    print("Swaps: " + str(swap_count))
    return list