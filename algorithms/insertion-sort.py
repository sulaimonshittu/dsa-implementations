def insertion_sort(array):
    for i in range(1, len(array)):
        pointer_value = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > pointer_value:
                array[j + 1] = array[j]
                j -= 1
            else:
                break
        array[j + 1] = pointer_value
    return array

x = insertion_sort([6, 4, 2, 1, -1, 5])
print(x)

