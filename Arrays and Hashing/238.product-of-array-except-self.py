#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
import copy
# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # NEETCODE
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer

        # O(n^2), exceeds time limit
        # answer = []
        # for i in range(len(nums)):
        #     nums_copy = copy.deepcopy(nums)
        #     nums_copy.pop(i)
        #     result = 1
        #     for num in nums_copy:
        #         result *= num
        #     answer.append(result)
        # return answer

        # @lc code=end


Solution().productExceptSelf([1, 2, 3, 4])
