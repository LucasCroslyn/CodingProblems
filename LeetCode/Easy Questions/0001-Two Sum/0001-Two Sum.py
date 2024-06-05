from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_hash:
                return [num_hash[remainder], i]
            num_hash[nums[i]] = i
        