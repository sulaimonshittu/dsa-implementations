import collections

def longestSubarray(nums, limit):
    """
    need to keep track of the largest and smallest element
    monotonic decreasing for largest element
    monotonic increasing for smallest element
    """
    left = right = 0
    max_num = 0
    larg_element = collections.deque()
    smal_element = collections.deque()
    while right < len(nums):
        while larg_element and nums[right] >= nums[larg_element[-1]]:
            larg_element.pop()
        larg_element.append(right)
        while smal_element and nums[right] <= nums[smal_element[-1]]:
            smal_element.pop()
        smal_element.append(right)
        while nums[larg_element[0]] - nums[smal_element[0]] > limit:
            left += 1
            if larg_element[0] < left:
                larg_element.popleft()
            if smal_element[0] < left:
                smal_element.popleft()
        max_num = max(max_num, right - left + 1)
        right += 1
    return max_num

longestSubarray([10,1,2,4,7,2], 5)