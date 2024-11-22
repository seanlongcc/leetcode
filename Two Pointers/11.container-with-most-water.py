#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List
# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            # you want to move the pointer based on which has the smaller height
            # as the area will never be bigger than it if you don't
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)

        return max_area
# @lc code=end


Solution().maxArea(height=[1, 1])
