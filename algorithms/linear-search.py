def linear_search(search_value, array):
    for key, value in enumerate(array):
        if value == search_value:
            return key
    return -1


def linear_search_sorted(search_value, array):
    for key, value in enumerate(array):
        if value == search_value:
            return key
        if value > search_value:
            return -1
    return -1

