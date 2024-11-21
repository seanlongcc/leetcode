#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List
# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, num in enumerate(nums):
            # three positive numbers cant add up to 0 so we skip
            # this is not explicitly needed for this problem
            if num > 0:
                break

            # if num is the same number as the previous skip over
            if i > 0 and num == nums[i - 1]:
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                current_sum = num + nums[left] + nums[right]
                if current_sum == 0:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # these pre-check the future iterations of the current value
                    # it checks for duplicates so future iterations skip them by incrementing/decrementing the iterator
                    # this is not checking previous values, but future values as the line before we just incremented/decrementd our iterators
                    # so this means we are checking if the next value is the same as the value we just added
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return output
        # @lc code=end


Solution().threeSum(nums=[-2, 0, 1, 1, 2])
