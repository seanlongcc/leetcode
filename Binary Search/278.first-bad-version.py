#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n

        # dont do <= since when its equal, we already have the first bad version
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                # everything ≥ mid is bad; first bad is in [left..mid]
                # dont do mid - 1 since mid could be the first bad
                right = mid
            else:
                # mid is good; first bad is in [mid+1..right]
                left = mid + 1
        return left

# @lc code=end
