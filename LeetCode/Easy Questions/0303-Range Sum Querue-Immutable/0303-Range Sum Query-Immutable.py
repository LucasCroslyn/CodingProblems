from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.cumsum = [nums[0]]
        for i in range(1, len(nums)):
            self.cumsum.append(nums[i] + self.cumsum[i-1])

    def sumRange(self, left: int, right: int) -> int:
        # All numbers used up to nums[right]
        if left == 0:
            return self.cumsum[right] 
        else:
        # cumsum[left-1] gives the sum we are at outside the range
        # Then cumsum[right] - that gives what we needed the sum to be to give the final cumsum
            return self.cumsum[right] - self.cumsum[left-1] 