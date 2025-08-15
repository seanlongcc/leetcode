#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import List
# @lc code=start


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # think of left and right as boundaries
        # next slot for 0; next slot for 2 from the end
        left, right = 0, len(
            nums) - 1
        # the actual iterator/index for scanning
        i = 0

        # stop when unknown region is exhausted
        while i <= right:
            if nums[i] == 0:
                # Put this 0 into the 0s region at the 'left' variable
                nums[i], nums[left] = nums[left], nums[i]
                left += 1                # expand the 0s region
                # the swapped-in value at i is a 1 or 0 already handled
                # we can increment because the current index could never be 2
                i += 1
            elif nums[i] == 2:
                # Put this 2 into the 2s region at 'right'
                nums[i], nums[right] = nums[right], nums[i]
                # expand the 2s region
                right -= 1
                # IMPORTANT: do NOT increment i here.
                # We must re-check nums[i] because we just swapped in a new value
                # from the right end; it could be 0, 1, or 2.
            else:  # nums[i] == 1
                # 1s belong in the middle; nothing to do
                i += 1

        # the one i came up with :D, but its probably not whats wanted :(
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]


        # @lc code=end
Solution().sortColors(nums=[2, 0, 2, 1, 1, 0])
