from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # This dictionary can be used to keep track of elements that appear in both arrays and only arr1
        arr1counts = Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num]*arr1counts.pop(num))
        # Elements in only arr1 are sorted in ascending order
        remain = sorted(arr1counts.keys())
        for num in remain:
            res.extend([num]*arr1counts.pop(num))
        return res