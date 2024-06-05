from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol_head = sol_tail = ListNode()
        carry = 0
        while l1 or l2 or carry:
            digit_sum = 0
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next
            if carry:
                digit_sum += carry
            carry = digit_sum  // 10
            digit_sum = digit_sum % 10

            sol_tail.next = ListNode(digit_sum)
            sol_tail = sol_tail.next
        return sol_head.next