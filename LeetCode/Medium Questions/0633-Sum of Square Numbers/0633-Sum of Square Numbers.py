import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            print(f"Left is: {left}")
            print(f"Right is: {right}")
            sum_sqr = (left ** 2) + (right ** 2)
            print(f"Square sum is: {sum_sqr}")
            if sum_sqr == c:
                return True
            elif sum_sqr < c:
                left += 1
            elif sum_sqr > c:
                right -= 1
        return False