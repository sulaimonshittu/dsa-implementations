def selection_sort(array):
    for i in range(len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        if array[smallest] != array[i]:
            array[i], array[smallest] = array[smallest], array[i]

    return array

x = selection_sort([6,5,4,3])
print(x)
