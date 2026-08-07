def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

ans = binary_search([0, 1, 2, 3, 5, 7, 8, 9, 9], 8, 0, 8)
print(ans)

def test(num):
    if num == 1:
        return 90
    return test(num - 1)

ans = test(4)
print(ans)
