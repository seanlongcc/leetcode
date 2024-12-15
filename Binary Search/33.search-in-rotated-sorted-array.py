#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                print(mid)
                return mid
            # is the left side sorted
            # its <= since nums[left] and nums[mid] can be the same value
            # the sorted side is the side that contains mid
            if nums[left] <= nums[mid]:
                # is the target in the sorted right side
                # its <= since the target value may be equal to nums[left] or nums[mid]
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # if not, our new array is the unsorted right side
                else:
                    left = mid + 1
            # is the right side sorted, this can just be an else
            elif nums[mid] <= nums[right]:
                # is the target in the sorted right side
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                # if not, our new array is the unsorted left side
                else:
                    right = mid - 1

        print(-1)
        return -1

        # @lc code=end


Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
