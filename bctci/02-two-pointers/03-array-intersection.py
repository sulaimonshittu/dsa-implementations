def common_elements(arr1, arr2):
    one = two = 0
    ans = []
    while one < len(arr1) and two < len(arr2):
        if arr1[one] == arr2[two]:
            ans.append(arr1[one])
            one += 1
            two += 1
        elif arr1[one] < arr2[two]:
            one += 1
        else:
            two += 1
    return ans

def run_tests():
  tests = [
      # Example 1 from the book
      ([1, 2, 3], [1, 3, 5], [1, 3]),
      # Example 2 from the book
      ([1, 1, 1], [1, 1], [1, 1]),
      # Additional test cases
      ([], [], []),
      ([1], [], []),
      ([], [1], []),
      ([1], [1], [1]),
      ([1, 2, 3], [4, 5, 6], []),
      ([1, 2, 2, 3], [2, 2, 3], [2, 2, 3]),
  ]
  for arr1, arr2, want in tests:
    got = common_elements(arr1, arr2)
    assert got == want, f"\ncommon_elements({arr1}, {arr2}): got: {
        got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()