def binary_search(value, array):
    left_start = 0
    right_start = len(array) - 1

    while left_start <= right_start:
        middle_value = (left_start + right_start) // 2
        if array[middle_value] == value:
            return middle_value
        if array[middle_value] > value:
            right_start = middle_value - 1
            continue
        if array[middle_value] < value:
            left_start = middle_value + 1
            continue
    return -1


