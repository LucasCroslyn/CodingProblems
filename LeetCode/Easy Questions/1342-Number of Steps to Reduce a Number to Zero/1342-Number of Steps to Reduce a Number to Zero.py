class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        cur_num = num
        while cur_num != 0:
            steps += 1
            if cur_num % 2 == 0:
                cur_num = cur_num / 2
            else:
                cur_num -= 1
        return steps