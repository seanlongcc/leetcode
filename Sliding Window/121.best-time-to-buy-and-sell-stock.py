#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
                continue

            max_profit = max(max_profit, prices[right] - prices[left])

        return max_profit
        # @lc code=end


Solution().maxProfit(prices=[7, 6, 4, 3, 1])
