#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List
# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        # catch edge cases of sorted arrays or arrays of length 1
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = (right + left)//2
            # the sorted side is the side that contains mid
            # look at unsorted side, which is left window pointer is greater than right window pointer
            if nums[left] > nums[mid]:
                # we cant do mid - 1 here since it can be the answer, unlike problem 704, where we check if mid is the target
                right = mid
            # this can just be an else
            elif nums[mid] > nums[right]:
                left = mid
            # check if right - left = 1, the right will always be the minimum
            if right - left == 1:
                print(nums[right])
                return nums[right]
                # @lc code=end


Solution().findMin(nums=[1])
