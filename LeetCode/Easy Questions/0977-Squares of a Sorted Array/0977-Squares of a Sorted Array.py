from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1

        # Fill in the squared array from largest to smallest
        index = len(nums) - 1
        square_array = [0] * len(nums)

        while index >= 0:
            left_square = abs(nums[left]**2)
            right_square = abs(nums[right]**2)
            if left_square >= right_square:
                square_array[index] = left_square
                left += 1
            else:
                square_array[index] = right_square
                right -= 1
            index -= 1
        return(square_array)
        