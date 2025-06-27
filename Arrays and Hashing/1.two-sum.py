#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # doing this with 2 pointer is more convoluted, so do it this way
        # store each number that we process
        num_map = {}

        # enumerate to get the index and current value
        for i, num in enumerate(nums):
            # get the complement of the number
            complement = target - num

            # check if the complement is in our hash map
            if complement in num_map:

                # if it is, return the index by using the value
                return [num_map[complement], i]

            # if its NOT in the hash map, add it to it
            num_map[num] = i

    # brute force
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]

# @lc code=end


Solution().twoSum(nums=[1, 2, 3, 4, 5, 6, 7, 8], target=4)
