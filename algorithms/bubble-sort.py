def bubble_sort(array):
    sorted_until_index = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, sorted_until_index):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        sorted_until_index -= 1

    return array

print([0] * 11)