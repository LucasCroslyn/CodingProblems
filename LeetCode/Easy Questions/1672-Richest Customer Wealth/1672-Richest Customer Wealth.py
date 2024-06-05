from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            if customer_wealth > ans:
                ans = customer_wealth
        return ans