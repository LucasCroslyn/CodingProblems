from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time O(n) but also uses O(n) space 
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # Time O(nlogn) but space O(1) because of space
        # It also changes nums itself for the O(1) space
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False