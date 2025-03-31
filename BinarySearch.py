
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)-1
    count = 0

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        count +=1
        if midpoint_value == item:
            print(count)
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint +1

    return None

def binary_search_binary(sequence, item, low = 0, high = None):

    if high is None:
        high = len(sequence) -1

    if low > high:
        return None

    midpoint = low + (high - low) // 2
    midpoint_value = sequence[midpoint]

    if midpoint_value == item:
        return midpoint
    elif item < midpoint_value:
        return binary_search_binary(sequence, item, low, midpoint-1)
    else:
        return binary_search_binary(sequence, item, midpoint+1, high)


