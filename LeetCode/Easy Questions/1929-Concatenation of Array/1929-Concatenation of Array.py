from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # More Explicit Solution
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
    
    def getConcatenation2(sel, nums: List[int]) -> List[int]:
        # Simplified Solution
        return nums * 2