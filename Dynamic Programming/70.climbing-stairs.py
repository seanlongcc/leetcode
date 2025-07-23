#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force recursion
        # this is fibonacci basically
        # if n <= 1:
        #     return 1

        #     return climbStairs(n - 1) + climbStairs(n - 2)

        # 1D DP
        # base case
        if n <= 1:
            return 1

        # we do n+1 since we actually use dp[0]
        # so for example n = 3, we ould get a list with [0,0,0,0]
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
# @lc code=end
