from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        consec_ones = 0
        for num in nums:
            if num == 0:
                consec_ones = 0
            else:
                consec_ones += 1
                if consec_ones > max_ones:
                    max_ones = consec_ones
        return max_ones