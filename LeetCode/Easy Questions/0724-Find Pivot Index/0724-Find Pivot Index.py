from typing import List

class Solution:
    # Unoptimal in terms of space, this space is O(n) 
    # Time is still O(n) here
    def pivotIndex(self, nums: List[int]) -> int:
        cumsums = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            cumsums.append(sum)

        if cumsums[-1] == cumsums[0]:
            return 0

        for j in range(1, len(cumsums)-1):
            if cumsums[j-1] == (cumsums[-1] - cumsums[j]):
                return j

        if cumsums[-2] == 0:
            return len(cumsums)-1

        return -1
    

    def pivotIndexOptimal(self, nums: List[int]) -> int:
        # This has O(1) space and O(n) time complexities
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            left_sum += nums[i]
            if left_sum == right_sum:
                return i
            right_sum -= nums[i]
        return -1