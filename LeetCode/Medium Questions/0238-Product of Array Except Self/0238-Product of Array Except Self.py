from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [0]*n

        prefix_prod, suffix_prod = 1, 1

        for i in range(n):
            answer[i] = prefix_prod
            prefix_prod *= nums[i]
        
        for j in range(n-1, -1, -1):
            answer[j] *= suffix_prod
            suffix_prod *= nums[j]

        return answer