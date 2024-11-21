#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if (current_sum == target):
                return [left+1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        # @lc code=end


Solution().twoSum(numbers=[-1, 0], target=-1)
