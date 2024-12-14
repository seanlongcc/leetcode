#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

from typing import List
# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # its less than or equal to account for searching the same index
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

        # @lc code=end


Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9)
