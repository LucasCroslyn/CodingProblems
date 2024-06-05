from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if len(str(num)) & 1 == 0:
                res += 1
        return res