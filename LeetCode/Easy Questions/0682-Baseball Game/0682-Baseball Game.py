from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        scores_stack = []
        for op in operations:
            if op == "+":
                scores_stack.append(scores_stack[-1] + scores_stack[-2])
                sum += scores_stack[-1]
            elif op == "D":
                scores_stack.append(2*scores_stack[-1])
                sum += scores_stack[-1]
            elif op == "C":
                sum -= scores_stack.pop()
            # Must be an number given contrainsts, no unknown ops
            else:
                scores_stack.append(int(op))
                sum += scores_stack[-1]
        return sum