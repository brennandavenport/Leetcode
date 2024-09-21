from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxProfit = 0

        for i, price in enumerate(prices):
            if price < prices[buy]:
                buy = i
            else:
                diff = price - prices[buy]
                if diff > maxProfit:
                    maxProfit = diff

        return maxProfit 

s = Solution()

print(s.maxProfit([2,4,5,62,124,5265,352343,442,24,5,9]))